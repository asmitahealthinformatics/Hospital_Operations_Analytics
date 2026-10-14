# Project: Hospital Operations & Patient Utilization Analytics
# Script: 01_data_exploration.py
# Purpose: Explore and understand the hospital dataset

# Step 1: Import libraries
import pandas as pd
from pathlib import Path

# Step 2: Locate the dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "Data" / "diabetic_data.csv"

# Step 3: Load the dataset
# Convert "?" into missing values and treat payer_code as text
df = pd.read_csv(
    file_path,
    na_values=["?"],
    dtype={"payer_code": "string"}
)

print("\nDATASET LOADED SUCCESSFULLY!")

# Step 4: Check dataset size
print("\nDATASET OVERVIEW")
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])

# Step 5: Display first five hospital encounters
selected_columns = [
    "encounter_id",
    "patient_nbr",
    "race",
    "gender",
    "age",
    "admission_type_id",
    "time_in_hospital",
    "num_lab_procedures",
    "num_medications",
    "readmitted"
]

print("\nFIRST FIVE HOSPITAL ENCOUNTERS")
print(df[selected_columns].head().to_string(index=False))

# Step 6: Display all column names
print("\nCOLUMN NAMES")

for number, column in enumerate(df.columns, start=1):
    print(f"{number}. {column}")

# Step 7: Check data types
print("\nDATA TYPES")
print(df.dtypes.to_string())

# Step 8: Identify missing values
print("\nMISSING VALUES")

missing_values = df.isnull().sum().sort_values(ascending=False)
print(missing_values.to_string())

# Step 9: Calculate missing value percentages
print("\nMISSING VALUE PERCENTAGES")

missing_percentage = (df.isnull().sum() / len(df)) * 100
missing_percentage = missing_percentage.sort_values(ascending=False)

# Display only columns containing missing values
missing_percentage = missing_percentage[missing_percentage > 0]
print(missing_percentage.round(2).to_string())

# Step 10: Count unique patients
print("\nUNIQUE PATIENTS")

unique_patients = df["patient_nbr"].nunique()
print("Total unique patients:", unique_patients)

# Step 11: Count unique hospital encounters
print("\nUNIQUE HOSPITAL ENCOUNTERS")

unique_encounters = df["encounter_id"].nunique()
print("Total unique encounters:", unique_encounters)

# Step 12: Check duplicate encounter IDs
print("\nDUPLICATE ENCOUNTER CHECK")

duplicate_encounters = df["encounter_id"].duplicated().sum()
print("Duplicate encounter IDs:", duplicate_encounters)

# Step 13: Generate descriptive statistics
# Focus on meaningful numerical hospital measures
numerical_columns = [
    "time_in_hospital",
    "num_lab_procedures",
    "num_procedures",
    "num_medications",
    "number_outpatient",
    "number_emergency",
    "number_inpatient",
    "number_diagnoses"
]

print("\nDESCRIPTIVE STATISTICS")
print(
    df[numerical_columns]
    .describe()
    .round(2)
    .T
    .to_string()
)

# Step 14: Explore readmission categories
# NO = No recorded readmission
# <30 = Readmission within 30 days
# >30 = Readmission after 30 days

print("\nREADMISSION CATEGORIES")
print(df["readmitted"].value_counts(dropna=False).to_string())

# Step 15: Display final dataset summary
print("\nFINAL DATASET SUMMARY")

print("Total hospital encounters:", len(df))
print("Unique patients:", unique_patients)
print("Unique encounter IDs:", unique_encounters)
print("Total columns:", df.shape[1])
print("Duplicate encounter IDs:", duplicate_encounters)

print("\nINITIAL DATA EXPLORATION COMPLETED SUCCESSFULLY!")