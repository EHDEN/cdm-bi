---
output: html_document
---



# Death

<!-- Discuss the goal of this dashboard... TO DO -->

In this dashboard is present the ''Database Type Filter'', that was detailed in the Chapter General.

## Death - By Month per Thousand People

<!-- Discuss what is important to see in this chart... TO DO -->

### SQL query

```sql
-- 502  Death - By Month per Thousand People
SELECT source.name,
       to_date(stratum_1, 'YYYYMM') as Date,
       count_value as count, 
       source.slug
FROM public.achilles_results AS achilles 
	INNER JOIN public.data_source AS source ON 
	  achilles.data_source_id=source.id
WHERE analysis_id = 502;
```

### Chart settings

The main characteristics of this chart are presented in Figure \@ref(fig:deathByMonthPerThousandPeople), being the following:

- **Data Tab**:
    - **Visualization Type**: Bar Chart
    - **Time range**: No filter
    - **Metrics**: MAX(count) as "Count"
    - **Filters**: Empty
    - **Series**: date
    - **Breakdowns**: Empty
    - **Row limit**: Empty
    - **Contribution**: Not checked
- **Costumize Tab**:
    - **Y Axis Label**: Number of Patients (in thousands)
    - **X Axis Label**: Databases
    - **Legend**: Checked
    - **Stacked Bars**: Not checked
    - **Bar Values**: Not checked
    - **Sort Bars**: Checked
    - **Extra Controls**: Not checked
    - **Reduce X ticks**: Not checked

<div class="figure">
<img src="images/deathByMonthPerThousandPeople.png" alt="Settings for creating chart show in thousands the number of death patients in the network (bar chart). Image changed to contain information hidden in the customize menu." width="100%" />
<p class="caption">(\#fig:deathByMonthPerThousandPeople)Settings for creating chart show in thousands the number of death patients in the network (bar chart). Image changed to contain information hidden in the customize menu.</p>
</div>

## Death - Number of Records

<!-- Discuss what is important to see in this chart... TO DO -->

### SQL query

```sql
-- 501  Death - Number of Records
SELECT source.name,
       count_value as count, 
       source.slug
FROM public.achilles_results AS achilles 
	INNER JOIN public.data_source AS source ON 
	  achilles.data_source_id=source.id
WHERE analysis_id = 501;
```

### Chart settings

The main characteristics of this chart are presented in Figure \@ref(fig:deathNumberOfRecords), being the following:

- **Data Tab**:
    - **Visualization Type**: Bar Chart
    - **Time range**: No filter
    - **Metrics**: MAX(count) as "Count"
    - **Filters**: Empty
    - **Series**: name
    - **Breakdowns**: Empty
    - **Row limit**: Empty
    - **Contribution**: Not checked
- **Costumize Tab**:
    - **Y Axis Label**: Number of Patients
    - **X Axis Label**: Databases
    - **Legend**: Checked
    - **Stacked Bars**: Not checked
    - **Bar Values**: Not checked
    - **Sort Bars**: Not checked
    - **Extra Controls**: Not checked
    - **Reduce X ticks**: Checked

<div class="figure">
<img src="images/deathNumberOfRecords.png" alt="Settings for creating chart show the number of death patients in each database (bar chart). Image changed to contain information hidden in the customize menu." width="100%" />
<p class="caption">(\#fig:deathNumberOfRecords)Settings for creating chart show the number of death patients in each database (bar chart). Image changed to contain information hidden in the customize menu.</p>
</div>

