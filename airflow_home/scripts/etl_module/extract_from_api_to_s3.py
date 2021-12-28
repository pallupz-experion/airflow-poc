from airflow.decorators import task

@task
def extract(config):
    import logging
    import time

    logging.info('extracting data')
    logging.info(config['paths_config']['path1'])
    logging.info(config['paths_config']['common_path1'])

    # pretend logic
    time.sleep(2)

    logging.info('data extraction successful')
    return None


if __name__== '__main__':
    extract()