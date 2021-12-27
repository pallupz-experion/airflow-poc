from datetime import datetime
from airflow.decorators import dag, task
import yaml
import sys

sys.path.append('airflow/scripts/')
DAG_CONFIG_YAML = 'airflow/branch_configs/ENVSUFFIX.yaml'

config = None
with open(DAG_CONFIG_YAML, 'r') as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)
    if 'daily_load_workflow' in config.keys():
        config = config['daily_load_workflow']
    else:
        config = config['template']

##-------------------------- Do NOT change ABOVE this line --------------------------##

from etl_module import extract_data, load_data_catalog, transform_data

@dag(
    schedule_interval=config['dag_config']['schedule'], 
    start_date=config['dag_config']['start_date'],
    catchup=config['dag_config']['catch_up'], 
    tags=['ENVSUFFIX']
    )
def ENVSUFFIX_daily_load_workflow():
    extract = task(extract_data.extract_data)
    transform = task(load_data_catalog.load_data_catalog)
    load = task(transform_data.transform_data)

    extract() >> transform() >> load()


ENVSUFFIX_daily_load_workflow = ENVSUFFIX_daily_load_workflow()


