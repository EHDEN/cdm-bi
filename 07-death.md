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
FROM public.achilles_results AS achilles INNER JOIN 
	public.data_source AS source ON achilles.data_source_id=source.id
WHERE analysis_id = 502;
```

## Death - Number of Records

Discuss what is important to see in this chart... TO DO

### SQL query

```sql
-- 501  Death - Number of Records
SELECT source.name,
    count_value as count, 
    source.slug
FROM public.achilles_results AS achilles INNER JOIN 
	public.data_source AS source ON achilles.data_source_id=source.id
WHERE analysis_id = 501;
```
