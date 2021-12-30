import os
import argparse
import shutil
import errno
import yaml
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IXUSR, S_IXGRP, S_IXOTH


parser = argparse.ArgumentParser()
parser.add_argument('--branch', type=str)
args = parser.parse_args()

def create(branch='local'):
    """
    This function is used to dynamically generate DAGs - based on templates created under dag_templates folder - 
    for the respective environments. The environment to run for is passed as the argument. 
    
    DAGs are generated only if the corresponding configuration file exists.

    Parameters
    ----------
    branch : str
        The suffix for the environment. Default value: local.
    """

    with open(f'setup/project_config.yaml', 'r') as data:
        config = yaml.load(data, Loader=yaml.SafeLoader)
    
    DAG_TEMPLATES_PATH = config['common-paths']['template_dags_path'].format(airflow_home=config['common-paths']['airflow_home'])
    DAG_PATH = config['common-paths']['airflow_dags_path'].format(airflow_home=config['common-paths']['airflow_home'])
    DAG_CONFIGS_PATH = config['common-paths']['branch_config_path'].format(airflow_home=config['common-paths']['airflow_home'])

    DAG_files = [filename for filename in os.listdir(DAG_TEMPLATES_PATH) if not filename.startswith('_')]
    config_files = [filename for filename in os.listdir(DAG_CONFIGS_PATH) if not filename.startswith('_')]

    # Fail Dynamic DAG Creation if the configuration file does not exist for the environment
    if f'{branch}.yaml' not in config_files: 
        raise FileNotFoundError(errno.ENOENT, "MISSING CONFIG FILE: DAGs cannot be created without relevant configuration files", f'{DAG_CONFIGS_PATH}/{branch}.yaml')

    print(f"Clearing '{DAG_PATH}/{branch}' folder")
    shutil.rmtree(f'{DAG_PATH}/{branch}', ignore_errors=True)

    print(f'Creating new DAGs with suffix: {branch}')
    # Create DAGs from template
    for dag_filename in DAG_files:
        
        # Generate complete path for template
        dag_file = f'{DAG_TEMPLATES_PATH}/{dag_filename}'

        # Generate complete path for output file
        new_dag_file = f"{DAG_PATH}/{branch}/{branch}_{dag_filename}"
        
        # Create output path, if not exists
        os.makedirs(os.path.dirname(new_dag_file), exist_ok=True)

        # Copy data from tempate file to output file
        shutil.copyfile(dag_file, new_dag_file)
        print(f'File Created: {new_dag_file}')

        # Replace ENVSUFFIX with respective value in the dag definition inside contents
        skipping_replacement = False
        with open(dag_file, "rt") as fin:
            with open(new_dag_file, "wt") as fout:
                for line in fin:
                    # print(skipping_replacement, line)
                    if line.strip() == "## <replacement-free-zone>":
                        skipping_replacement = True
                    elif line.strip() == "## </replacement-free-zone>":
                        skipping_replacement = False
                    
                    out = line.replace('ENVSUFFIX', branch) if skipping_replacement == False else line
                    fout.write(out)

        # To prevent accidental edits, make the file read and execute only
        os.chmod(new_dag_file, S_IREAD | S_IRGRP | S_IROTH | S_IXUSR | S_IXGRP | S_IXOTH)


if __name__ == '__main__':
    if args.branch:
        create(args.branch)
    else:
        create()
    