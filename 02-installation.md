---
title: "02-installation.Rmd"
output: html_document
---



# Installation

TO DO production and dev environments...

Make sure that you have docker and docker-compose installed in your machine. Then, please follow these steps:

- Please enter in the ''docker'' directory and create your `.env` file here, using `.env-example` as reference. For local installation, you can just copy the `.env-example` content to a new file. Note: In case of port errors in the next steps, the problem could be related to a port already in use by your system that you defined here and it is busy, chose other.

- Tip the following commands in the command line:

    1. Clone the Apache Superset repository:
    
        ```
        git clone https://github.com/apache/incubator-superset
         ../superset
        cp ../superset/contrib/docker/superset_config.py ../superset
        ```
        
    2. Init the Apache Superset (This creates a user, so it is necessary to interact with the console):
    
        ```
        docker-compose run --rm superset ./docker-init.sh
        ```
        
    3. Init the Dashboard Layout  (This creates a user, so it is necessary to interact with the console):
    
        ```
        docker-compose run --rm dashboard_viewer ./docker-init.sh
        ```
        
    4. Finally, bring up the containers 
    
        ```
        docker-compose up -d
        ```
        
To check if everything is ok, please wait 2 minutes and tip `docker ps` and the following containers need to be running: 
```
... 0.0.0.0:8088->8088/tcp   dashboard_viewer_superset_1
... 0.0.0.0:8000->8000/tcp   dashboard_viewer_dashboard_viewer_1
... 0.0.0.0:6379->6379/tcp   dashboard_viewer_redis_1
... 5432/tcp                 dashboard_viewer_postgres_1
```

Now, you have a clean setup running in your machine. To try the application using synthetic data, please continue to follow the steps in the ''Demo'' section.

## Insert Concepts

The concepts table are not in the repository due to its dimension. Therefore, to insert this table in the installation, you should perform the following steps:

1. Download concept.csv file from here (todo)

2. Copy the file to the /tmp directory inside of the postgres container

    ```sh
    docker cp concept.csv dashboard_viewer_postgres_1:/tmp/
    ```
    
3. Enter in the dashboard_viewer_postgres_1 container:

    ```sh
    docker exec -it dashboard_viewer_postgres_1 bash
    ```
    
4. Enter in the achilles database:

    ```
    psql achilles
    ```
    
5. Create the table in the database using this command:

    ```sql
        CREATE TABLE concept (
          concept_id         INTEGER        NOT NULL,
          concept_name       VARCHAR(255)   NOT NULL,
          domain_id          VARCHAR(20)    NOT NULL,
          vocabulary_id      VARCHAR(20)    NOT NULL,
          concept_class_id   VARCHAR(20)    NOT NULL,
          standard_concept   VARCHAR(1)     NULL,
          concept_code       VARCHAR(50)    NOT NULL,
          valid_start_date   DATE           NOT NULL,
          valid_end_date     DATE           NOT NULL,
          invalid_reason     VARCHAR(1)     NULL
        );
    ```
    
6. Copy the CSV file content to the table (this could take a while):

    ```sql
    COPY public.concept from '/tmp/concept.csv' WITH DELIMITER ','
        CSV HEADER;
    ```

7. Alter table ownership:

    ```sql
    -- <user> : defined in the .env file
    ALTER TABLE public.concept OWNER TO <user>;
    ```

8. Create index in table:

    ```sql
    CREATE INDEX achilles_results_analysis_id_index ON 
        achilles_results (analysis_id);
    CREATE INDEX achilles_results_source_index ON achilles_results 
        (data_source_id);
    CREATE INDEX concept_concept_id_index ON concept (concept_id);
    CREATE INDEX concept_concept_name_index ON concept 
        (concept_name);
    ```
    

## Import dashboards

TO DO

## Dummy data

TO DO
    
