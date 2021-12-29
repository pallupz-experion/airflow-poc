import yaml
import logging

def get_env_configs_for_dag(ENV, base_dag_id):
    DAG_CONFIG_YAML = f'airflow_home/branch_configs/{ENV}.yaml'
    
    try:
        with open(DAG_CONFIG_YAML, 'r') as data:
            config = yaml.load(data, Loader=yaml.SafeLoader)
            if base_dag_id in config.keys():
                config = config[base_dag_id]
            else:
                logging.warn('Dedicated config file for DAG not available. Using template config.')
                config = config['template']
    
    except:
        logging.warn('No valid configs available!')
        return {}
    
    else:
        return config