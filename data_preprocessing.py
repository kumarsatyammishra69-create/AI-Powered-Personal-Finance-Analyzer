import pandas as pd
import os

def load_and_clean(path):
    df = pd.read_csv(path)
    
    # Drop empty rows
    df.dropna(inplace=True)
    
    # Clean column names
    df.columns = df.columns.str.lower().str.strip()
    
    # Convert date column
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    
    # Save cleaned data
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned_data.csv", index=False)
    print("✅ Data cleaned and saved!")
    
    return df