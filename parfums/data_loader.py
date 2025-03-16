import pandas as pd
from pathlib import Path

CSV_FILE_PATH = Path(__file__).resolve().parent / 'data' / 'fragrantica_filtered_final_corrected.csv'

def load_parfums():
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        df['Year'] = df['Year'].replace("inconnu", pd.NA)
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        df['Year'] = df['Year'].fillna(0).astype('Int64')
        df.to_csv('c:/users/chella/documents/python/parfum_reco/parfums/data/fragrantica_filtered_final_cleaned_fixed.csv', index=False)
        print(df['Year'].dtype)

        return df
    except Exception as e:
        print(f"Erreur lors du charegement du fichier : {e}")
        return None
    

