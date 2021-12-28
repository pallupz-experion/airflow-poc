from airflow.decorators import task

@task
def transform(config):
    import logging
    import time

    logging.info('transform / enrich data')
    logging.info(config['paths_config']['path1'])

    # pretend logic
    time.sleep(2)

    logging.info('data transformation successful')
    return None


if __name__== '__main__':
    transform()
