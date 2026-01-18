import pandas as pd
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

DATA_DIR = settings.BASE_DIR.parent / 'data' / 'processed'

def load_data():
    """Load data from Parquet files with caching."""
    data = cache.get('dashboard_data')
    if data:
        return data

    try:
        education_data = pd.read_parquet(DATA_DIR / 'education_data.parquet')
        income_data = pd.read_parquet(DATA_DIR / 'income_data.parquet')
        mental_health_data = pd.read_parquet(DATA_DIR / 'mental_health_data.parquet')
        crime_path = DATA_DIR / 'crime_data.parquet'
        crime_data = pd.read_parquet(crime_path) if crime_path.exists() else pd.DataFrame()
    except (FileNotFoundError, Exception) as e:
        # Fallback for dev/testing if ETL hasn't run
        print(f"Error loading Parquet data: {e}. returning empty.")
        return {}, {}, {}, {}

    data = (crime_data, education_data, income_data, mental_health_data)
    cache.set('dashboard_data', data, timeout=3600) # Cache for 1 hour
    return data

def index(request):
    return render(request, 'visualizations/index.html')

def get_data(request):
    crime_data, education_data, income_data, mental_health_data = load_data()

    if isinstance(education_data, dict) and not education_data:
        return JsonResponse({'error': 'Data not available. Please run ETL pipeline.'}, status=503)

    # Convert data to JSON format, replacing NaN with None for valid JSON
    crime_json = crime_data.astype(object).where(pd.notnull(crime_data), None).to_dict(orient='records')
    education_json = education_data.astype(object).where(pd.notnull(education_data), None).to_dict(orient='records')
    income_json = income_data.astype(object).where(pd.notnull(income_data), None).to_dict(orient='records')
    mental_health_json = mental_health_data.astype(object).where(pd.notnull(mental_health_data), None).to_dict(orient='records')

    # Return JSON response
    return JsonResponse({
        'crime': crime_json,
        'education': education_json,
        'income': income_json,
        'mental_health': mental_health_json
    })

def filter_data(request):
    # This endpoint seems redundant if frontend does filtering or if we move to API parameters.
    # For now, let's keep it minimal or deprecate it.
    # The existing implementation re-read CSVs on every request.
    return JsonResponse({'message': 'Endpoint deprecated. Use /get_data and filter on client or implement specific query params.'})
