import os
import argparse
import shutil
import errno


parser = argparse.ArgumentParser()
parser.add_argument('--branch', type=str, default='test')
args = parser.parse_args()
BRANCH = args.branch

def setup_dags(branch='test'):
    """
    This function is used to dynamically generate DAGs - based on templates created under dag_templates folder - 
    for the respective environments. The environment to run for is passed as the argument. 
    
    DAGs are generated only if the corresponding configuration file exists.

    Parameters
    ----------
    branch : str
        The suffix for the environment. Default value: test.
    """
    
    DAG_TEMPLATES_PATH = 'airflow/dag_templates'
    DAG_PATH = 'airflow/dags'
    DAG_CONFIGS_PATH = 'airflow/branch_configs'

    DAG_files = [filename for filename in os.listdir(DAG_TEMPLATES_PATH) if not filename.startswith('_')]
    config_files = [filename for filename in os.listdir(DAG_CONFIGS_PATH) if not filename.startswith('_')]

    # Fail Dynamic DAG Creation if the configuration file does not exist for the environment
    if f'{branch}.yaml' not in config_files: 
        raise FileNotFoundError(errno.ENOENT, "MISSING CONFIG FILE: DAGs cannot be created without relevant configuration files", f'{DAG_CONFIGS_PATH}/{branch}.yaml')

    print(f'Creating DAGs with Suffix: {branch}')
    # Create DAGs from template
    for dag_filename in DAG_files:
        
        # Generate complete path for template
        dag_file = f'{DAG_TEMPLATES_PATH}/{dag_filename}'

        # Generate complete path for output file
        new_dag_file = f"{DAG_PATH}/{branch}/{dag_filename}"
        
        # Create output path, if not exists
        os.makedirs(os.path.dirname(new_dag_file), exist_ok=True)

        # Copy data from tempate file to output file
        shutil.copyfile(dag_file, new_dag_file)
        print(f'File Created: {new_dag_file}')

        # Replace ENVSUFFIX with respective value in the dag definition inside contents
        with open(dag_file, "rt") as fin:
            with open(new_dag_file, "wt") as fout:
                for line in fin:
                    fout.write(line.replace('ENVSUFFIX', branch))


if __name__ == '__main__':
    setup_dags(BRANCH)
    