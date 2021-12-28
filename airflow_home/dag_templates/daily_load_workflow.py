from datetime import datetime
from airflow.decorators import dag, task
import yaml
import sys
import logging

from airflow_home.scripts.etl_module import extract_from_api_to_s3, clean_data, load_to_db

DAG_CONFIG_YAML = 'airflow_home/branch_configs/ENVSUFFIX.yaml'
config = None
with open(DAG_CONFIG_YAML, 'r') as data:
    config = yaml.load(data, Loader=yaml.SafeLoader)
    if 'daily_load_workflow' in config.keys():
        config = config['daily_load_workflow']
    else:
        logging.warn('Dedicated config file for DAG not available. Using template config.')
        config = config['template']

@dag(
    schedule_interval=config['dag_config']['schedule'], 
    start_date=config['dag_config']['start_date'],
    catchup=config['dag_config']['catch_up'], 
    tags=['ENVSUFFIX'],
    )
def ENVSUFFIX_daily_load_workflow():
    (
        extract_from_api_to_s3.extract(config) >>
        clean_data.transform(config) >>
        load_to_db.load(config)
    )

ENVSUFFIX_daily_load_workflow = ENVSUFFIX_daily_load_workflow()


