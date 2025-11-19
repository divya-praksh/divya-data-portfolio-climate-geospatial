import pandas as pd
import os

def clean_gps(infile, outfile):
    df = pd.read_csv(infile, parse_dates=['timestamp'])
    # remove duplicates
    df = df.drop_duplicates()
    # drop invalid lat/lon
    df = df.dropna(subset=['latitude','longitude'])
    df = df[(df.latitude.between(-90,90)) & (df.longitude.between(-180,180))]
    # round coords
    df['latitude'] = df['latitude'].round(6)
    df['longitude'] = df['longitude'].round(6)
    df.to_csv(outfile, index=False)
    print(f"Saved cleaned file to {outfile}")

if __name__ == "__main__":
    os.makedirs('../assets/data/cleaned', exist_ok=True)
    clean_gps('../assets/data/gps_sample.csv', '../assets/data/cleaned/gps_sample_cleaned.csv')
