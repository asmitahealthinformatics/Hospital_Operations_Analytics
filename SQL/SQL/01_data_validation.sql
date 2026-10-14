-- Select the hospital operations database
CREATE DATABASE IF NOT EXISTS hospital_operations;

USE hospital_operations;

-- Confirm which database is currently selected
SELECT DATABASE();

-- Display all tables in the database
SHOW TABLES;

-- Check the total number of records in the original imported table
SELECT
    COUNT(*) AS total_encounters
FROM hospital_encounters;

-- Check total records, unique encounters, and unique patients
-- in the original imported table
SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT encounter_id) AS unique_encounters,
    COUNT(DISTINCT patient_nbr) AS unique_patients
FROM hospital_encounters;

-- Check the minimum and maximum encounter IDs
-- in the original imported table
SELECT
    MIN(encounter_id) AS minimum_encounter_id,
    MAX(encounter_id) AS maximum_encounter_id,
    COUNT(*) AS total_records
FROM hospital_encounters;

-- Validate the complete dataset imported using Python
SELECT
    COUNT(*) AS total_encounters,
    COUNT(DISTINCT encounter_id) AS unique_encounters,
    COUNT(DISTINCT patient_nbr) AS unique_patients
FROM hospital_encounters_verified;

-- Display the first five records
SELECT *
FROM hospital_encounters_verified
LIMIT 5;

-- Display the table structure and data types
DESCRIBE hospital_encounters_verified;

-- Check data types of columns used for KPI analysis
SELECT
    COLUMN_NAME,
    DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hospital_operations'
  AND TABLE_NAME = 'hospital_encounters_verified'
  AND COLUMN_NAME IN (
      'time_in_hospital',
      'num_lab_procedures',
      'num_procedures',
      'num_medications',
      'number_outpatient',
      'number_emergency',
      'number_inpatient',
      'readmitted'
  );
  SELECT
    COUNT(*) AS total_encounters,
    COUNT(DISTINCT encounter_id) AS unique_encounters,
    COUNT(DISTINCT patient_nbr) AS unique_patients
FROM hospital_operations.hospital_encounters_verified;