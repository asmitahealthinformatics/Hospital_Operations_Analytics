# Project: Hospital Operations & Patient Utilization Analytics
# Script: 02_data_quality_cleaning.py
# Purpose: Assess data quality before applying cleaning rules

# Step 1: Import libraries
import pandas as pd
from pathlib import Path

# Step 2: Locate the original dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "Data" / "diabetic_data.csv"

# Step 3: Load the dataset
df = pd.read_csv(
    file_path,
    na_values=["?"],
    dtype={"payer_code": "string"}
)

print("\nDATA QUALITY ASSESSMENT STARTED")

# Step 4: Check dataset dimensions
print("\nDATASET DIMENSIONS")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Step 5: Check missing values
print("\nCOLUMNS WITH MISSING VALUES")

missing_count = df.isnull().sum()
missing_percent = (missing_count / len(df)) * 100

missing_summary = pd.DataFrame({
    "Missing Count": missing_count,
    "Missing Percentage": missing_percent.round(2)
})

missing_summary = missing_summary[
    missing_summary["Missing Count"] > 0
]

print(
    missing_summary
    .sort_values("Missing Percentage", ascending=False)
    .to_string()
)

# Step 6: Check duplicate rows and encounter IDs
print("\nDUPLICATE CHECK")

print("Duplicate complete rows:", df.duplicated().sum())

print(
    "Duplicate encounter IDs:",
    df["encounter_id"].duplicated().sum()
)

# Step 7: Check missing patient and encounter identifiers
print("\nMISSING IDENTIFIERS")

print("Missing patient IDs:", df["patient_nbr"].isnull().sum())

print("Missing encounter IDs:", df["encounter_id"].isnull().sum())

# Step 8: Check numerical value ranges
print("\nNUMERICAL VALUE RANGES")

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

print(
    df[numerical_columns]
    .agg(["min", "max"])
    .T
    .to_string()
)

# Step 9: Check invalid negative values
print("\nNEGATIVE VALUE CHECK")

for column in numerical_columns:
    negative_count = (df[column] < 0).sum()
    print(f"{column}: {negative_count}")

# Step 10: Examine categorical values
print("\nGENDER CATEGORIES")
print(df["gender"].value_counts(dropna=False).to_string())

print("\nAGE CATEGORIES")
print(df["age"].value_counts(dropna=False).to_string())

print("\nREADMISSION CATEGORIES")
print(df["readmitted"].value_counts(dropna=False).to_string())

print("\nADMISSION TYPE CODES")
print(
    df["admission_type_id"]
    .value_counts(dropna=False)
    .sort_index()
    .to_string()
)

# Step 11: Check missing diagnosis information
print("\nMISSING DIAGNOSIS INFORMATION")

for column in ["diag_1", "diag_2", "diag_3"]:
    print(f"{column}: {df[column].isnull().sum()}")

# Step 12: Final assessment summary
print("\nDATA QUALITY ASSESSMENT COMPLETED")

print("Total records assessed:", len(df))
print("Total columns assessed:", df.shape[1])
print("No data has been deleted or modified.")
# Step 13: Create a copy for cleaning
# Keep the original DataFrame unchanged
clean_df = df.copy()

# Step 14: Remove weight from the analysis dataset
# Weight is missing in approximately 97% of encounters
clean_df = clean_df.drop(columns=["weight"])

# Step 15: Standardize missing categorical information
# Missing values are labeled rather than deleting encounters
clean_df["race"] = clean_df["race"].fillna("Unknown")

clean_df["medical_specialty"] = (
    clean_df["medical_specialty"].fillna("Not Recorded")
)

clean_df["payer_code"] = (
    clean_df["payer_code"].fillna("Not Recorded")
)

# Step 16: Validate encounter identifiers
assert clean_df["encounter_id"].notna().all(), "Missing encounter IDs"
assert clean_df["patient_nbr"].notna().all(), "Missing patient IDs"
assert clean_df["encounter_id"].is_unique, "Duplicate encounter IDs"

# Step 17: Validate hospital stay values
assert clean_df["time_in_hospital"].between(1, 14).all(), \
    "Unexpected hospital length of stay"

# Step 18: Validate readmission categories
valid_readmission = ["NO", "<30", ">30"]

assert clean_df["readmitted"].isin(valid_readmission).all(), \
    "Unexpected readmission category"

# Step 19: Verify record counts
print("\nCLEANING VALIDATION")

print("Original records:", len(df))
print("Cleaned records:", len(clean_df))

print("Original columns:", df.shape[1])
print("Cleaned columns:", clean_df.shape[1])

print(
    "Duplicate encounter IDs:",
    clean_df["encounter_id"].duplicated().sum()
)

# Step 20: Save cleaned dataset
output_path = project_folder / "Data" / "diabetic_data_cleaned.csv"

clean_df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("File location:", output_path)