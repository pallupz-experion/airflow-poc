from datetime import datetime
from airflow.decorators import dag, task
from airflow_home.scripts.etl_module import extract_from_api_to_s3, clean_data, load_to_db
from airflow_home.scripts.utils import utils


base_dag_id = 'daily_load_workflow'
config = utils.get_config('ENVSUFFIX', base_dag_id)

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
