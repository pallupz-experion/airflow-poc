from airflow.decorators import task

@task
def load(config):
    import logging
    import time

    logging.info('final touch-ups / enrichments')
    logging.info(config['paths_config']['path1'])
    
    # pretend logic
    time.sleep(2)

    logging.info('data catalog write successful')
    return None


if __name__== '__main__':
    load()
