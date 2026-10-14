# Project: Hospital Operations & Patient Utilization Analytics
# Script: 03_import_validation.py
# Purpose: Validate the CSV before SQL import

import pandas as pd
from pathlib import Path

# Locate the cleaned dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "Data" / "diabetic_data_cleaned.csv"

# Load the cleaned dataset
df = pd.read_csv(
    file_path,
    dtype={"payer_code": "string"}
)

# Check the original CSV
print("\nCSV VALIDATION")

print("Total records:", len(df))
print("Total columns:", df.shape[1])

print("Minimum encounter ID:", df["encounter_id"].min())
print("Maximum encounter ID:", df["encounter_id"].max())

print("Duplicate encounter IDs:", df["encounter_id"].duplicated().sum())

# Check missing values
print("\nMISSING VALUES")

print(df.isnull().sum().sort_values(ascending=False).head(10))

print("\nCSV VALIDATION COMPLETED")