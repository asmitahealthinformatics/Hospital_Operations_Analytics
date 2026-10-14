# Hospital Operations & Patient Utilization Analytics

## 1. Project Overview

This project analyzes hospital encounters involving patients with
diabetes to identify patterns in patient utilization, hospital length
of stay, and 30-day readmissions.

The analysis uses Python for data cleaning, MySQL for querying and
KPI calculations, and Tableau for interactive visualizations.

## 2. Dataset Overview

Dataset: Diabetes 130-US Hospitals (1999–2008)

Source: UCI Machine Learning Repository

Total Hospital Encounters: 101,766

Unique Patients: 71,518

The dataset contains historical inpatient encounter information
from 130 US hospitals.

## 3. Key Performance Indicators

| KPI | Result |
|-----|--------|
| Total Hospital Encounters | 101,766 |
| Unique Patients | 71,518 |
| Average Length of Stay | 4.40 days |
| Encounters Readmitted Within 30 Days | 11.16% |

The readmission percentage represents the proportion of encounters
labeled as readmitted within 30 days in the dataset. It is not
a risk-adjusted hospital quality measure.

## 4. Key Findings

### Finding 1: Previous Inpatient Visits and Readmission

Patients with more previous inpatient visits showed higher
30-day readmission percentages.

- 0 previous visits: 8.44%
- 1 previous visit: 12.92%
- 2 previous visits: 17.43%
- 3 previous visits: 20.29%
- 4 or more previous visits: 30.70%

This suggests that prior inpatient utilization may help identify
groups with higher readmission percentages.

### Finding 2: Previous Emergency Visits and Readmission

The percentage of encounters readmitted within 30 days increased
across groups with more previous emergency visits.

- 0 previous visits: 10.47%
- 1 previous visit: 14.35%
- 2 previous visits: 18.27%
- 3 previous visits: 20.28%
- 4 or more previous visits: 28.54%

Patients with frequent previous emergency visits may benefit
from closer examination of their healthcare utilization patterns.

### Finding 3: Age and Hospital Length of Stay

Average hospital length of stay generally increased across
older age groups.

The 80–90 age group had the highest observed average length
of stay at approximately 4.81 days.

This finding suggests that age-related differences in hospital
utilization deserve further investigation.

### Finding 4: Admission Type and Readmission

The dashboard showed differences in 30-day readmission percentages
across admission types.

- Elective: 10.39%
- Emergency: 11.52%
- Urgent: 11.18%

These differences are descriptive and do not establish that
admission type causes readmission.

## 5. Potential Operational Applications

Based on these findings, healthcare analysts could explore:

1. Identifying patients with frequent previous hospital encounters.
2. Examining readmission patterns among high-utilization groups.
3. Reviewing discharge planning and follow-up care processes.
4. Investigating factors associated with longer hospital stays.
5. Building dashboards to track utilization and readmission trends.

These are potential applications rather than interventions
tested or proven effective by this project.

## 6. Tools and Technologies

Python:
Data exploration, cleaning, and validation.

MySQL:
Data storage, SQL queries, and KPI calculations.

Tableau:
Dashboard development and data visualization.

VS Code:
Project development and file organization.

## 7. Project Limitations

- The dataset covers hospital encounters from 1999–2008.
- The analysis focuses on encounters involving diabetes.
- Findings may not represent current US hospital performance.
- Readmission percentages are descriptive and not risk-adjusted.
- Associations do not establish causation.
- The dataset does not support direct analysis of hospital
  bed occupancy, financial performance, or staffing efficiency.

## 8. Conclusion

The analysis identified associations between previous healthcare
utilization and 30-day readmission percentages.

Higher numbers of previous inpatient and emergency visits were
associated with higher readmission percentages.

The project demonstrates how Python, SQL, and Tableau can be
combined to clean healthcare data, calculate operational KPIs,
and communicate findings through visualizations.