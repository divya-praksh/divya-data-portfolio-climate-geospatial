import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

os.makedirs('assets/data', exist_ok=True)

# GPS sample: 500 rows along a route
np.random.seed(0)
n = 500
start = datetime(2025,1,1,8,0)
times = [start + timedelta(seconds=30*i) for i in range(n)]
lats = 12.95 + np.cumsum(np.random.normal(0, 0.0005, n))
lons = 80.15 + np.cumsum(np.random.normal(0, 0.0005, n))
speeds = np.abs(np.random.normal(40, 8, n))

gps = pd.DataFrame({
    'timestamp': times,
    'latitude': lats,
    'longitude': lons,
    'speed_kmph': speeds
})
gps.to_csv('assets/data/gps_sample.csv', index=False)

# Crop sample: yearly district-level rainfall and yield (10 districts x 6 years)
districts = [f'District_{i}' for i in range(1,11)]
years = list(range(2018, 2024))
rows = []
for d in districts:
    base_yield = np.random.uniform(1.5, 3.5)
    for y in years:
        rainfall = np.random.normal(900, 200)
        yield_val = base_yield + 0.002*(rainfall-900) + np.random.normal(0,0.15)
        rows.append({'district': d, 'year': y, 'annual_rainfall_mm': max(0, rainfall),
                     'crop_yield_ton_per_ha': max(0, yield_val)})

crop = pd.DataFrame(rows)
crop.to_csv('assets/data/crop_rainfall_sample.csv', index=False)

print("Sample data created in assets/data/")