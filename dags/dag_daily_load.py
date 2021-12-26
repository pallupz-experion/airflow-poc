from datetime import datetime
from airflow.decorators import dag, task
from task_definitions import load_tasks


@dag(schedule_interval=None, start_date=datetime(2021, 12, 1), catchup=False, tags=['test'])
def test_taskflow_api_etl():
    extract = task(load_tasks.extract)
    transform = task(load_tasks.transform)
    load = task(load_tasks.load)

    extract() >> transform() >> load()

test_taskflow_api_etl = test_taskflow_api_etl()