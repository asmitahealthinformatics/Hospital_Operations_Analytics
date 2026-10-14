# Project: Hospital Operations & Patient Utilization Analytics
# Script: 04_load_data_to_mysql.py
# Purpose: Load cleaned hospital data into MySQL

# Step 1: Import libraries
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from getpass import getpass

# Step 2: Locate the cleaned dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "Data" / "diabetic_data_cleaned.csv"

# Step 3: Load the cleaned dataset
df = pd.read_csv(
    file_path,
    dtype={"payer_code": "string"}
)

print("\nDATASET LOADED")
print("Total records:", len(df))
print("Total columns:", df.shape[1])

# Step 4: Get MySQL password securely
password = getpass("Enter your MySQL password: ")

# Step 5: Configure the MySQL connection
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password=password,
    host="localhost",
    port=3306,
    database="hospital_operations"
)

engine = create_engine(connection_url)

# Step 6: Test the database connection
with engine.connect() as connection:
    result = connection.execute(text("SELECT DATABASE()"))
    print("\nConnected to database:", result.scalar())

# Step 7: Import data into a new table
print("\nIMPORTING DATA INTO MYSQL...")
print("This may take several minutes.")

df.to_sql(
    name="hospital_encounters_verified",
    con=engine,
    if_exists="fail",
    index=False,
    chunksize=1000,
    method="multi"
)

print("\nDATA IMPORT COMPLETED")

# Step 8: Validate imported records
with engine.connect() as connection:
    result = connection.execute(
        text("""
            SELECT
                COUNT(*) AS total_records,
                COUNT(DISTINCT encounter_id) AS unique_encounters,
                COUNT(DISTINCT patient_nbr) AS unique_patients
            FROM hospital_encounters_verified
        """)
    )

    row = result.fetchone()

    print("\nMYSQL VALIDATION RESULTS")
    print("Total records:", row[0])
    print("Unique encounters:", row[1])
    print("Unique patients:", row[2])

# Step 9: Compare Python and MySQL record counts
if row[0] == len(df):
    print("\nSUCCESS: All records imported!")
else:
    print("\nWARNING: Record counts do not match!")

engine.dispose()