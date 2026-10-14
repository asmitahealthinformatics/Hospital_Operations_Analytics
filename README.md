# Hospital Operations & Patient Utilization Analytics

## Project Overview

This project analyzes historical hospital encounter data to explore
patient utilization patterns, length of stay, and 30-day readmissions.

The project demonstrates an end-to-end healthcare analytics workflow
using Python, MySQL, and Tableau.

## Technologies Used

- Python (Pandas, NumPy)
- MySQL
- Tableau
- Visual Studio Code
- GitHub

## Dataset

**Dataset:** Diabetes 130-US Hospitals (1999–2008)

**Source:** UCI Machine Learning Repository

The dataset includes 101,766 hospital encounters involving
71,518 unique patients across 130 US hospitals.

## Project Objectives

1. Clean and validate hospital encounter data.
2. Calculate key hospital utilization metrics.
3. Analyze 30-day readmission patterns.
4. Explore relationships between previous hospital visits and readmissions.
5. Develop an interactive Tableau dashboard.

## Key Performance Indicators

| KPI | Result |
|-----|--------|
| Total Hospital Encounters | 101,766 |
| Unique Patients | 71,518 |
| Average Length of Stay | 4.40 days |
| 30-Day Readmission Percentage | 11.16% |

The readmission percentage is the proportion of encounters
labeled as readmitted within 30 days, not a risk-adjusted rate.

## Key Findings

### Previous Inpatient Visits

The 30-day readmission percentage increased from 8.44%
among encounters with no previous inpatient visits to
30.70% among encounters with four or more previous visits.

### Previous Emergency Visits

The 30-day readmission percentage increased from 10.47%
among encounters with no previous emergency visits to
28.54% among encounters with four or more previous visits.

### Hospital Length of Stay

The overall average length of stay was 4.40 days.

The 80–90 age group had the highest observed average
length of stay at approximately 4.81 days.

## Project Structure

Hospital_Operations_Analytics/
    Data/
    Python/
    SQL/
    Tableau/
    Reports/
        project_insights.md
    README.md

## Dashboard

An interactive Tableau dashboard was developed to visualize:

- Total hospital encounters
- Unique patients
- Average length of stay
- 30-day readmission percentage
- Readmissions by previous inpatient visits
- Readmissions by previous emergency visits
- Length of stay by age group
- Readmissions by age group
- Readmissions by admission type

Dashboard link: https://public.tableau.com/views/HospitalOperationsandPatientUtilizationAnalytics/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Detailed Project Insights

See [Project Insights](Reports/project_insights.md)
for findings, potential applications, and limitations.

## Limitations

- Historical data from 1999–2008
- Diabetes-related hospital encounters
- Descriptive, unadjusted readmission percentages
- No causal conclusions

## Conclusion

This project demonstrates the ability to clean and validate
healthcare data, perform SQL-based analysis, develop Tableau
visualizations, and communicate findings relevant to
healthcare operations and patient utilization.