-- KPI 1: Average length of hospital stay

SELECT
    COUNT(*) AS total_encounters,
    ROUND(AVG(time_in_hospital), 2) AS average_length_of_stay,
    MIN(time_in_hospital) AS minimum_stay,
    MAX(time_in_hospital) AS maximum_stay
FROM hospital_operations.hospital_encounters_verified;
-- KPI 2: Readmission within 30 days

SELECT
    COUNT(*) AS total_encounters,

    SUM(CASE
        WHEN readmitted = '<30' THEN 1
        ELSE 0
    END) AS readmitted_within_30_days,

    ROUND(
        100.0 * SUM(CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS readmission_percentage

FROM hospital_operations.hospital_encounters_verified;
-- KPI 3: Medication utilization per encounter

SELECT
    COUNT(*) AS total_encounters,
    ROUND(AVG(num_medications), 2) AS average_medications,
    MIN(num_medications) AS minimum_medications,
    MAX(num_medications) AS maximum_medications
FROM hospital_operations.hospital_encounters_verified;
-- KPI 4: Previous emergency department utilization

SELECT
    COUNT(*) AS total_encounters,

    SUM(CASE
        WHEN number_emergency > 0 THEN 1
        ELSE 0
    END) AS encounters_with_prior_emergency_visits,

    ROUND(AVG(number_emergency), 2) AS average_prior_emergency_visits,

    MAX(number_emergency) AS maximum_prior_emergency_visits

FROM hospital_operations.hospital_encounters_verified;
-- KPI 5: Previous inpatient utilization

SELECT
    COUNT(*) AS total_encounters,

    SUM(CASE
        WHEN number_inpatient > 0 THEN 1
        ELSE 0
    END) AS encounters_with_prior_inpatient_visits,

    ROUND(
        100.0 * SUM(CASE
            WHEN number_inpatient > 0 THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS prior_inpatient_percentage,

    ROUND(AVG(number_inpatient), 2) AS average_prior_inpatient_visits,

    MAX(number_inpatient) AS maximum_prior_inpatient_visits

FROM hospital_operations.hospital_encounters_verified;
-- KPI 6: Medication utilization

SELECT
    COUNT(*) AS total_encounters,

    ROUND(AVG(num_medications), 2) AS average_medications,

    MIN(num_medications) AS minimum_medications,

    MAX(num_medications) AS maximum_medications

FROM hospital_operations.hospital_encounters_verified;
-- KPI 6: Laboratory procedure utilization

SELECT
    COUNT(*) AS total_encounters,
    ROUND(AVG(num_lab_procedures), 2) AS average_lab_procedures,
    MIN(num_lab_procedures) AS minimum_lab_procedures,
    MAX(num_lab_procedures) AS maximum_lab_procedures
FROM hospital_operations.hospital_encounters_verified;
-- KPI 7: Average length of stay by age group

SELECT
    age,
    COUNT(*) AS total_encounters,
    ROUND(AVG(time_in_hospital), 2) AS average_length_of_stay
FROM hospital_operations.hospital_encounters_verified
GROUP BY age
ORDER BY age;
-- KPI 8: Readmission percentage by age group

SELECT
    age,
    COUNT(*) AS total_encounters,

    SUM(CASE
        WHEN readmitted = '<30' THEN 1
        ELSE 0
    END) AS readmitted_within_30_days,

    ROUND(
        100.0 * SUM(CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS readmission_percentage

FROM hospital_operations.hospital_encounters_verified

GROUP BY age
ORDER BY age;
-- KPI 9: Average length of stay by readmission category

SELECT
    readmitted,
    COUNT(*) AS total_encounters,
    ROUND(AVG(time_in_hospital), 2) AS average_length_of_stay,
    ROUND(AVG(num_medications), 2) AS average_medications,
    ROUND(AVG(num_lab_procedures), 2) AS average_lab_procedures
FROM hospital_operations.hospital_encounters_verified
GROUP BY readmitted
ORDER BY average_length_of_stay DESC;
-- KPI 10: Hospital utilization by admission type

SELECT
    admission_type_id,
    COUNT(*) AS total_encounters,
    ROUND(AVG(time_in_hospital), 2) AS average_length_of_stay,
    ROUND(AVG(num_medications), 2) AS average_medications,
    ROUND(AVG(num_lab_procedures), 2) AS average_lab_procedures
FROM hospital_operations.hospital_encounters_verified
GROUP BY admission_type_id
ORDER BY total_encounters DESC;
-- KPI 11: Readmission percentage by admission type

SELECT
    admission_type_id,
    COUNT(*) AS total_encounters,

    SUM(CASE
        WHEN readmitted = '<30' THEN 1
        ELSE 0
    END) AS readmitted_within_30_days,

    ROUND(
        100.0 * SUM(CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS readmission_percentage

FROM hospital_operations.hospital_encounters_verified

GROUP BY admission_type_id
ORDER BY readmission_percentage DESC;
-- KPI 12: Readmission percentage by gender

SELECT
    gender,
    COUNT(*) AS total_encounters,

    SUM(CASE
        WHEN readmitted = '<30' THEN 1
        ELSE 0
    END) AS readmitted_within_30_days,

    ROUND(
        100.0 * SUM(CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS readmission_percentage

FROM hospital_operations.hospital_encounters_verified

GROUP BY gender
ORDER BY readmission_percentage DESC;
-- KPI 13: Readmission by previous inpatient utilization

SELECT
    CASE
        WHEN number_inpatient = 0 THEN 'No prior inpatient visits'
        ELSE 'One or more prior inpatient visits'
    END AS prior_inpatient_group,

    COUNT(*) AS total_encounters,

    SUM(CASE
        WHEN readmitted = '<30' THEN 1
        ELSE 0
    END) AS readmitted_within_30_days,

    ROUND(
        100.0 * SUM(CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS readmission_percentage

FROM hospital_operations.hospital_encounters_verified

GROUP BY
    CASE
        WHEN number_inpatient = 0 THEN 'No prior inpatient visits'
        ELSE 'One or more prior inpatient visits'
    END

ORDER BY readmission_percentage DESC;
-- KPI 14: Readmission by previous emergency utilization

SELECT
    CASE
        WHEN number_emergency = 0 THEN 'No prior emergency visits'
        ELSE 'One or more prior emergency visits'
    END AS prior_emergency_group,

    COUNT(*) AS total_encounters,

    SUM(CASE
        WHEN readmitted = '<30' THEN 1
        ELSE 0
    END) AS readmitted_within_30_days,

    ROUND(
        100.0 * SUM(CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS readmission_percentage

FROM hospital_operations.hospital_encounters_verified

GROUP BY
    CASE
        WHEN number_emergency = 0 THEN 'No prior emergency visits'
        ELSE 'One or more prior emergency visits'
    END

ORDER BY readmission_percentage DESC;
-- KPI 15: Readmission by number of previous inpatient visits

SELECT
    CASE
        WHEN number_inpatient = 0 THEN '0 visits'
        WHEN number_inpatient = 1 THEN '1 visit'
        WHEN number_inpatient = 2 THEN '2 visits'
        WHEN number_inpatient = 3 THEN '3 visits'
        ELSE '4 or more visits'
    END AS prior_inpatient_visits,

    COUNT(*) AS total_encounters,

    SUM(CASE
        WHEN readmitted = '<30' THEN 1
        ELSE 0
    END) AS readmitted_within_30_days,

    ROUND(
        100.0 * SUM(CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS readmission_percentage

FROM hospital_operations.hospital_encounters_verified

GROUP BY prior_inpatient_visits

ORDER BY
    CASE prior_inpatient_visits
        WHEN '0 visits' THEN 1
        WHEN '1 visit' THEN 2
        WHEN '2 visits' THEN 3
        WHEN '3 visits' THEN 4
        ELSE 5
    END;
    -- KPI 16: Readmission by number of previous emergency visits

SELECT
    CASE
        WHEN number_emergency = 0 THEN '0 visits'
        WHEN number_emergency = 1 THEN '1 visit'
        WHEN number_emergency = 2 THEN '2 visits'
        WHEN number_emergency = 3 THEN '3 visits'
        ELSE '4 or more visits'
    END AS prior_emergency_visits,

    COUNT(*) AS total_encounters,

    SUM(CASE
        WHEN readmitted = '<30' THEN 1
        ELSE 0
    END) AS readmitted_within_30_days,

    ROUND(
        100.0 * SUM(CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS readmission_percentage

FROM hospital_operations.hospital_encounters_verified

GROUP BY prior_emergency_visits

ORDER BY
    CASE prior_emergency_visits
        WHEN '0 visits' THEN 1
        WHEN '1 visit' THEN 2
        WHEN '2 visits' THEN 3
        WHEN '3 visits' THEN 4
        ELSE 5
    END;