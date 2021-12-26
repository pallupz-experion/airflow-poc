# ETL development on Airflow deployed in Docker

## Rough Architecture / Workflow
### Server
 - Airflow and other satellite services (like postgres for metadata) will be deployed as Docker Containers in a remote EC2 server. Deployment on server can be done using ```docker-compose.yaml``` file.
 - *ETL Development* will focus on creating DAGs and Tasks only. DAG Repo will only contain codes for these two.
 - As part of CI/CD on DAG repo, any new pushes/merges will copy code to `/dags` folder in the Airflow Docker container.
   - ***TODO***: 
      1. How to handle different branches like DEV, QC, and such - especially when they can be on the SAME physical server?
         - Approach One:
           - Separate Airflow containers for each ENV? 
           - So, from each branch, push code to a respective container?
           - CONCERNS:
             1. Resource crunch?
             2. Only one container can point to 8080. Rest will have to be other ports.
             
         - Approach Two:
           - From each branch, rename dags dynamically as per ENV
           - Like `test_dag` should become `dev_test_dag`, `qc_test_dag`, `prod_test_dag`, and so on
           - CONCERNS:
             1. Complex to set up? May be use `DagBag`?

### Local
 - All local development is recommended on WSL2 (Windows Subsystem for Linux) with VSCode pointing to it. This is for ease of coding and it also makes running docker & airflow locally much easier.\
 Will need VSCode extension named "Remote - WSL": https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl
 - All local development first needs a python virtual environment setup
 - Steps mentioned in `local-testing-setup.sh` file
 - NOTES:
   * Any time development is resumed, make sure to ***activate*** the virtual environment by running below command. This is necessary since `local-testing-setup.sh` will create `.venv` and install airflow local dependency inside it. \
   Command :
   ```bash
   source .venv/bin/activate
   ```
   * Once development activities are done, `.venv` can be closed just by running:
   ```bash
   deactivate
   ```
   * Airflow is **required** as a local dependency in the virtualenv to validate the DAGs and test tasks.
   * To test a DAG, run:
   ```bash
   airflow dags test <dag-id> <execution-date>
   ```
   * To test a specific task in a DAG, run:
   ```bash
   airflow tasks test <dag-id> <task-id> <execution-date>
   ```
    
    