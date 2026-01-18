import pandas as pd
import glob
import os
import re

DATA_RAW = "data/raw"
DATA_PROCESSED = "data/processed"

def clean_number(x):
    if isinstance(x, str):
        if x.strip().lower() in {"np", "na", "n/a", ""}:
            return None
        # Remove commas and convert to float/int
        clean_str = x.replace(',', '')
        try:
            return float(clean_str)
        except ValueError:
            return x
    return x

def process_generic_year_columns(df, value_name="Value"):
    # Identify year columns (4 digits)
    year_cols = [c for c in df.columns if re.match(r'^\d{4}$', str(c)) or c in ['2,019']] 
    # specific fix for "2,019" in mental_health
    
    # Rename "2,019" to "2019" if present
    df = df.rename(columns={"2,019": "2019"})
    year_cols = [c.replace("2,019", "2019") for c in year_cols]
    
    # Melt
    id_vars = [c for c in df.columns if c not in year_cols and c != "Year total"]
    
    df_melted = df.melt(id_vars=id_vars, value_vars=[c for c in year_cols if c in df.columns], 
                        var_name="Year", value_name=value_name)
    
    df_melted["Value"] = df_melted[value_name].apply(clean_number)
    df_melted["Year"] = df_melted["Year"].astype(int)
    return df_melted

def load_crime_data():
    # Crime data is messy: Row 1 has states, Row 2 has header.
    # We might need to iterate through states.
    # For MVP, let's try to read it assuming it's flat or just take the first state (NSW) as sample
    # or try to parse the structure.
    
    # Looking at the head:
    # Row 0: "Victimisation rates..."
    # Row 1: Offence, 1993... 2023
    # Row 2: ,New South Wales...
    
    # Let's read with header=1 to get years.
    df = pd.read_csv(f"{DATA_RAW}/crime_data.csv", header=1, encoding="cp1252", encoding_errors="replace")
    
    # The first column is Offence.
    # The rows contain data.
    # The State row (Row 0 in this new df) has "New South Wales" in Col 1.
    # It implies the block below is NSW.
    # A robust parser would look for state names. 
    # For now, let's assume the first block is NSW and filter out non-data.
    
    # Fill forward state? No, it's likely blocks.
    # Let's add a "State" column and populate it.
    
    df['State'] = None
    current_state = None
    
    # This loop is slow but safe for small data
    rows = []
    headers = df.columns.tolist() # Offence, 1993...
    
    # Iterate and detect States
    # We need to re-read without header maybe to scan correctly?
    # Or just iterate the dataframe.
    
    # Actually, simpler approach:
    # 1. Read the file raw.
    # 2. Find row indices where column 1 is a State Name.
    # 3. Slice blocks.
    
    # For now, I'll restrict to just standardising it if it's simple.
    # If it's too complex, I might skip detailed parsing for the first pass and just return raw-ish.
    # BUT we need 2019-2023 data for the dashboard.
    
    # Let's try to clean the existing dataframe structure
    # Drop the first row which is just the state name in the second column?
    # Actually, if the CSV is exactly as shown in `head`:
    # Row 3 (Index 0) is "Homicide...", "3.4", ...
    
    # Let's regex the Offence column. If it's NaN, maybe it's a State header row?
    # Unnamed: 1 is New South Wales.
    
    state = "New South Wales" # Default
    
    # Filter out rows where Offence is NaN
    data_rows = df[df['Offence'].notna()].copy()
    data_rows['State'] = state # Hardcoded for this file snippet if it only contains NSW
    
    # Melt years
    year_cols = [c for c in headers if re.match(r'^\d{4}$', str(c))]
    df_melted = data_rows.melt(id_vars=['State', 'Offence'], value_vars=year_cols, var_name='Year', value_name='Rate')
    df_melted['Rate'] = df_melted['Rate'].apply(clean_number)
    df_melted['Rate'] = pd.to_numeric(df_melted['Rate'], errors='coerce')
    
    return df_melted

def load_education_data():
    df = pd.read_csv(f"{DATA_RAW}/education_data.csv")
    df = process_generic_year_columns(df, value_name="Count")
    return df

def load_income_data():
    df = pd.read_csv(f"{DATA_RAW}/income_data.csv")
    df = process_generic_year_columns(df, value_name="Count")
    return df

def load_mental_health_data():
    df = pd.read_csv(f"{DATA_RAW}/mental_health_data.csv")
    # Fix column names if needed. "Year Total" vs "Year total"
    df = process_generic_year_columns(df, value_name="Count")
    return df

def run_pipeline():
    os.makedirs(DATA_PROCESSED, exist_ok=True)
    
    print("Processing Crime Data...")
    try:
        df_crime = load_crime_data()
        df_crime.to_parquet(f"{DATA_PROCESSED}/crime_data.parquet")
    except Exception as e:
        print(f"Error processing crime data: {e}")

    print("Processing Education Data...")
    try:
        df_edu = load_education_data()
        df_edu.to_parquet(f"{DATA_PROCESSED}/education_data.parquet")
    except Exception as e:
        print(f"Error processing education data: {e}")

    print("Processing Income Data...")
    try:
        df_inc = load_income_data()
        df_inc.to_parquet(f"{DATA_PROCESSED}/income_data.parquet")
    except Exception as e:
        print(f"Error processing income data: {e}")

    print("Processing Mental Health Data...")
    try:
        df_mh = load_mental_health_data()
        df_mh.to_parquet(f"{DATA_PROCESSED}/mental_health_data.parquet")
    except Exception as e:
        print(f"Error processing mental health data: {e}")
        
    print("ETL Complete.")

if __name__ == "__main__":
    run_pipeline()
