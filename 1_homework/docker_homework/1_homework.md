# Docker + Teraform

1. Docker: Which tag has the following text? - Automatically remove the container when it exits

docker run --help 

2. Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash. Now check the python modules that are installed ( use pip list ).

docker run -it --entrypoint=bash python:3.9 
pip list

3. Postgres + Docker

#Run docker-compose in detached mode
docker-compose up -d

#Run docker build
docker build -t hw_taxi_ingest:v002 .

#Upload green-taxi data
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz" 

docker run -it --network=docker_homework_default \
hw_taxi_ingest:v002 \
--user=root --password=root --host=pgdatabase --port=5432 --db=ny_taxi_hw --table=green_taxi_trips --url=${URL}

#Open Pg-Admin
localhost:8080 in browser

#Upload taxi zones through jupyter-notebook
python3 -m notebook

4.

5. Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

select
	date(lpep_pickup_datetime),
	"Borough",
	sum(total_amount) as total_amount_agg
from
	green_taxi_trips t
	join zones z on t."PULocationID"=z."LocationID"
where
	date(lpep_pickup_datetime) = '2019-09-18'
group by 1,2
having sum(total_amount)>50000


6. For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.

select
distinct
	z_pu."Zone" as zone_pu,
	z_do."Zone" as zone_do,
	t.tip_amount
from
	green_taxi_trips t
	join zones z_pu on t."PULocationID"=z_pu."LocationID"
	join zones z_do on t."DOLocationID"=z_do."LocationID"
where
	z_pu."Zone"='Astoria'
order by 3 desc