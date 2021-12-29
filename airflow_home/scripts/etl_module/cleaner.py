from airflow.decorators import task

@task
def clean_dataset_1(config):
    import logging
    import time

    logging.info('clean dataset 1')
    logging.info(config['paths_config']['path1'])

    # pretend logic
    time.sleep(2)

    logging.info('data cleaning on 1 successful')
    return None


@task
def clean_dataset_2(config):
    import logging
    import time

    logging.info('clean dataset 2')
    logging.info(config['paths_config']['path1'])

    # pretend logic
    time.sleep(2)

    logging.info('data cleaning on 2 successful')
    return None