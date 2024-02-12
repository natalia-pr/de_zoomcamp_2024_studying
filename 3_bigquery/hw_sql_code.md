-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `de-course-2024-412715.ny_taxi.green_taxi_data_external`(
  VendorID	INT64,
  lpep_pickup_datetime INT64,
  lpep_dropoff_datetime INT64,	
  store_and_fwd_flag STRING,	
  RatecodeID FLOAT64,	
  PULocationID INT64,	
  DOLocationID INT64,	
  passenger_count FLOAT64,	
  trip_distance FLOAT64,	
  fare_amount FLOAT64,	
  extra FLOAT64,	
  mta_tax FLOAT64,	
  tip_amount FLOAT64,	
  tolls_amount FLOAT64,	
  ehail_fee INT64,	
  improvement_surcharge FLOAT64,	
  total_amount FLOAT64,	
  payment_type FLOAT64,	
  trip_type FLOAT64,	
  congestion_surcharge FLOAT64,	
  __index_level_0__ INT64	
)
OPTIONS (
  format = 'Parquet',
  uris = ['gs://mage_zoomcamp_2024/ny_green_taxi_data_module_3.parquet']
);


-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE `de-course-2024-412715.ny_taxi.green_taxi_data_non_partitioned` AS
SELECT
  VendorID,
  TIMESTAMP_MICROS(CAST(lpep_pickup_datetime / 1000 AS INT64)) lpep_pickup_datetime,
  TIMESTAMP_MICROS(CAST(lpep_dropoff_datetime / 1000 AS INT64)) lpep_dropoff_datetime,	
  store_and_fwd_flag,	
  RatecodeID,	
  PULocationID,	
  DOLocationID,	
  passenger_count,	
  trip_distance,	
  fare_amount,	
  extra,	
  mta_tax,	
  tip_amount,	
  tolls_amount,	
  ehail_fee,	
  improvement_surcharge,	
  total_amount,	
  payment_type,	
  trip_type,	
  congestion_surcharge,	
  __index_level_0__	
FROM 
  `de-course-2024-412715.ny_taxi.green_taxi_data_external`;


-- Creating a partition and cluster table
CREATE OR REPLACE TABLE `de-course-2024-412715.ny_taxi.green_taxi_data_partitioned`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID AS
SELECT
  VendorID,
  TIMESTAMP_MICROS(CAST(lpep_pickup_datetime / 1000 AS INT64)) lpep_pickup_datetime,
  TIMESTAMP_MICROS(CAST(lpep_dropoff_datetime / 1000 AS INT64)) lpep_dropoff_datetime,	
  store_and_fwd_flag,	
  RatecodeID,	
  PULocationID,	
  DOLocationID,	
  passenger_count,	
  trip_distance,	
  fare_amount,	
  extra,	
  mta_tax,	
  tip_amount,	
  tolls_amount,	
  ehail_fee,	
  improvement_surcharge,	
  total_amount,	
  payment_type,	
  trip_type,	
  congestion_surcharge,	
  __index_level_0__	
FROM 
  `de-course-2024-412715.ny_taxi.green_taxi_data_external`;


-- Question 5
select
  distinct
    PULocationID
from
  `de-course-2024-412715.ny_taxi.green_taxi_data_non_partitioned`
where
  lpep_pickup_datetime between "2022-06-01" and "2022-06-30"
--12.82 MB

select
  distinct
    PULocationID
from
  `de-course-2024-412715.ny_taxi.green_taxi_data_partitioned`
where
  lpep_pickup_datetime between "2022-06-01" and "2022-06-30"
--1.12 MB