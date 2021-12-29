from airflow import DAG

## <replacement-free-zone>
PLACEHOLDER = 'ENVSUFFIX'
## </replacement-free-zone>

ENV = 'ENVSUFFIX'
ENV = ENV if ENV != PLACEHOLDER else 'local'

## ------------------------------ DO NOT CHANGE ABOVE THIS LINE ------------------------------ ##

from airflow_home.scripts.etl_module import extract_from_api_to_s3, cleaner, load_to_db
from airflow_home.scripts.utils import utils


# Set DAG's base name
base_dag_id = 'daily_load_workflow'
dag_id = f'{ENV}_{base_dag_id}'

# Get configs for the dag in the current environment
config = utils.get_env_configs_for_dag(ENV, base_dag_id)
tags = config['dag_config'].pop('tags').append(ENV)

with DAG(dag_id, tags=tags, **config['dag_config']) as dag:
    (
        extract_from_api_to_s3.extract(config) >>
        [cleaner.clean_dataset_1(config), cleaner.clean_dataset_2(config)] >>
        load_to_db.load(config)
    )

