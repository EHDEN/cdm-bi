---
title: "07-death.Rmd"
output: html_document
---



# Death

## Death - By Month per Thousand People

Discuss what is important to see in this chart... TO DO

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

The main characteristics of this chart are presented in Figure \@ref(fig:visitTypes), being the following:

- **Data Tab**:
    - **Visualization Type**: Bar Chart
    - **Time range**: No filter
    - **Metrics**:
    - **Filters**: Empty
    - **Series**:
    - **Breakdowns**:
    - **Row limit**: Empty
    - **Contribution**: Not checked
- **Costumize Tab**:
    - **Y Axis Label**: 
    - **X Axis Label**: 
    - **Legend**: Checked
    - **Stacked Bars**:
    - **Bar Values**:
    - **Sort Bars**:
    - **Extra Controls**:
    - **Reduce X ticks**:

<div class="figure">
<img src="images/populationCharacteristicsObservationPeriodStartDates.png" alt="Settings for creating chart representing the number of patients at the start of their observation period (bar chart). Image changed to contain information hidden in the customize menu." width="100%" />
<p class="caption">(\#fig:visitTypes1)Settings for creating chart representing the number of patients at the start of their observation period (bar chart). Image changed to contain information hidden in the customize menu.</p>
</div>

## Death - Number of Records

Discuss what is important to see in this chart... TO DO

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

The main characteristics of this chart are presented in Figure \@ref(fig:visitTypes), being the following:

- **Data Tab**:
    - **Visualization Type**: Bar Chart
    - **Time range**: No filter
    - **Metrics**:
    - **Filters**: Empty
    - **Series**:
    - **Breakdowns**:
    - **Row limit**: Empty
    - **Contribution**: Not checked
- **Costumize Tab**:
    - **Y Axis Label**: 
    - **X Axis Label**: 
    - **Legend**: Checked
    - **Stacked Bars**:
    - **Bar Values**:
    - **Sort Bars**:
    - **Extra Controls**:
    - **Reduce X ticks**:

<div class="figure">
<img src="images/populationCharacteristicsObservationPeriodStartDates.png" alt="Settings for creating chart representing the number of patients at the start of their observation period (bar chart). Image changed to contain information hidden in the customize menu." width="100%" />
<p class="caption">(\#fig:visitTypes2)Settings for creating chart representing the number of patients at the start of their observation period (bar chart). Image changed to contain information hidden in the customize menu.</p>
</div>

