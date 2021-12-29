## Complete steps to start up a fresh Airflow instance running in Docker container on EC2 is available here:
## https://gist.github.com/pallupz-experion/a37f7f5f687cdb21cd6d6890057d886f

## Create relevant directories
# mkdir \
#     airflow_home \
#     airflow_home/dags \
#     airflow_home/dag_templates \
#     airflow_home/logs \
#     airflow_home/branch_configs \
#     airflow_home/scripts \
#     airflow_home/data \
#     setup

## Create .env file
# echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

## Assuming Docker and Docker-Compose have already been setup locally,
## To start a local airflow instance, run below commands:
# docker-compose up airflow-init
# docker-compose up

## To stop local airflow docker container, navigate to path containing docker-compose.yaml and run below command: 
# docker-compose down
