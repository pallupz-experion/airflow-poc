from airflow.decorators import task

@task
def transform(config):
    import logging
    import time

    logging.info('clean dataset 2')
    logging.info(config['paths_config']['path1'])

    # pretend logic
    time.sleep(2)

    logging.info('data cleaning on 2 successful')
    return None


if __name__== '__main__':
    transform()
