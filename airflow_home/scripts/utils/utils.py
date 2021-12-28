import yaml
import logging

def get_config(ENVSUFFIX, base_dag_id):
    DAG_CONFIG_YAML = f'airflow_home/branch_configs/{ENVSUFFIX}.yaml'
    
    try:
        with open(DAG_CONFIG_YAML, 'r') as data:
            config = yaml.load(data, Loader=yaml.SafeLoader)
            if base_dag_id in config.keys():
                config = config[base_dag_id]
            else:
                logging.warn('Dedicated config file for DAG not available. Using template config.')
                config = config['template']
    except:
        return {}
    
    else:
        return config