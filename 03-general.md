---
title: "03-general.Rmd"
output: html_document
---



# General

Discuss the goal of this dashboard... TO DO

## Database Type Filter

Discuss what is important to see in this chart... TO DO

### SQL query

```sql
--  Country and database type filters
SELECT source.name, 
       country.country as Country, 
       database_type as Type,
       source.slug
FROM public.data_source AS source INNER JOIN public.country 
  AS country ON source.country_id=country.id;
```

### Chart settings

TO DO

## Country Filter

Discuss what is important to see in this chart... TO DO

### SQL query

```sql
--  Country and database type filters
SELECT source.name, 
       country.country as Country, 
       database_type as Type,
       source.slug
FROM public.data_source AS source INNER JOIN public.country 
  AS country ON source.country_id=country.id;
```

### Chart settings

TO DO


## General - World Map

Discuss what is important to see in this chart... TO DO

### SQL query

```sql
--    General - World Map
SELECT  name,
        slug,
        release_date,
        database_type,
        latitude,
        longitude,
        link,
        country,
        continent
FROM public.data_source AS source INNER JOIN public.country 
  AS country ON source.country_id=country.id;
```

### Chart settings

TO DO

## General - Network Growth (Summary)

Discuss what is important to see in this chart... TO DO

### SQL query

```sql
-- 108    General - Network Growth (Summary)
SELECT data.source,
       data.country,
       data.database_type,
       --cast(stratum_1 as INTEGER )*30 AS Days,
       data.release_date - cast(stratum_1 AS INTEGER) * INTERVAL 
        '1 month' as Time,
       count_value                   AS count
FROM (
     SELECT source.name              AS source,
            achilles.analysis_id     AS analysis_id,
            achilles.stratum_1,
            achilles.stratum_2,
            achilles.stratum_3,
            achilles.stratum_4,
            achilles.stratum_5,
            achilles.count_value,
            country.country,
            source.database_type, 
            source.release_date
     FROM public.achilles_results AS achilles INNER JOIN 
      public.data_source AS source ON
      achilles.data_source_id=source.id
     INNER JOIN public.country AS country ON 
      source.country_id=country.id
     ) data
WHERE analysis_id = 108;
```

### Chart settings

TO DO



## General - Network Growth by Date

Discuss what is important to see in this chart... TO DO

### SQL query

```sql
-- 108    General - Network Growth by Date
SELECT data.source,
       data.country,
       data.database_type,
       cast(stratum_1 as Integer)*30 AS DAY,
       count_value                   AS count
FROM (
     SELECT source.name              AS source,
            achilles.analysis_id     AS analysis_id,
            achilles.stratum_1,
            achilles.stratum_2,
            achilles.stratum_3,
            achilles.stratum_4,
            achilles.stratum_5,
            achilles.count_value,
            country.country,
            source.database_type
     FROM public.achilles_results AS achilles INNER JOIN 
      public.data_source AS source ON 
      achilles.data_source_id=source.id
     INNER JOIN public.country AS country ON 
      source.country_id=country.id
     ) data
WHERE analysis_id = 108;
```

### Chart settings

TO DO

## General - Patients per Country

Discuss what is important to see in this chart... TO DO

### SQL query

```sql
-- 1    General - Patients per Country
SELECT source.name,
       country.country,
       source.database_type,
       count_value as patient_count,
       source.slug
FROM public.achilles_results AS achilles INNER JOIN 
  public.data_source AS source ON achilles.data_source_id=source.id
  INNER JOIN public.country AS country ON 
  source.country_id=country.id
WHERE analysis_id = 1;
```

### Chart settings

TO DO

## General - Database Types per Country

Discuss what is important to see in this chart... TO DO

### SQL query

```sql
-- 1    General - Database types per Country
SELECT source.name, 
       country.country as Country, 
       database_type as Type,
       count_value as "Nr_patients",
       source.slug
FROM public.achilles_results AS achilles INNER JOIN 
  public.data_source AS source ON achilles.data_source_id=source.id
  INNER JOIN public.country AS country ON 
  source.country_id=country.id
WHERE analysis_id = 1;
```

### Chart settings

TO DO

