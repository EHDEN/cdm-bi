---
output: html_document
---



# Visit

<!-- Discuss the goal of this dashboard... TO DO -->

In this dashboard is present the ''Database Type Filter'', that was detailed in the Chapter General.

## Visit - Types

<!-- Discuss what is important to see in this chart... TO DO -->

### SQL query

```sql
-- 201  Visit - Types
SELECT source.name, 
       concept_name AS "Observation", 
       count_value AS "Nr_Observations",
       source.slug
FROM public.achilles_results AS achilles 
	INNER JOIN public.data_source AS source ON 
	  achilles.data_source_id=source.id
	INNER JOIN public.concept ON 
	  stratum_1 = CAST(concept_id AS text)
WHERE analysis_id = 201;
```

### Chart settings

The main characteristics of this chart are presented in Figure \@ref(fig:visitTypes), being the following:

- **Data Tab**:
    - **Visualization Type**: Bar Chart
    - **Time range**: No filter
    - **Metrics**: MAX(Nr_Observations) as Observations
    - **Filters**: Empty
    - **Series**: name
    - **Breakdowns**: Observation
    - **Row limit**: Empty
    - **Contribution**: Not checked
- **Costumize Tab**:
    - **Y Axis Label**: Empty
    - **X Axis Label**: Databases
    - **Legend**: Checked
    - **Stacked Bars**: Checked
    - **Bar Values**: Not checked
    - **Sort Bars**: Checked
    - **Extra Controls**: Checked
    - **Reduce X ticks**: Checked

<div class="figure">
<img src="images/visitTypes.png" alt="Settings for creating chart representing the types of visit in the databases (bar chart). Image changed to contain information hidden in the customize menu." width="100%" />
<p class="caption">(\#fig:visitTypes)Settings for creating chart representing the types of visit in the databases (bar chart). Image changed to contain information hidden in the customize menu.</p>
</div>

