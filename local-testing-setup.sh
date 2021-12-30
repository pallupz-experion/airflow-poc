## BELOW COMMANDS ARE ALL ONE-TIME SETUP. 
## BEST TO RUN ONE-BY-ONE MANUALLY TO AVOID PERMISSION ISSUES!

# Install virtual environment module
python3 -m pip install virtualenv

# Create new virtual environment
python3 -m venv .venv

# Start the new vitual environment
source .venv/bin/activate

# Install dependencies into venv
pip3 install -r requirements.txt

# [OPTIONAL] Used when Airflow is hosted locally
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

# Set AIRFLOW_HOME directory so that DAGs are detected
export AIRFLOW_HOME=$(pwd)/airflow_home
export PYTHONPATH=$(pwd)
# Set AIRFLOW__CORE__LOAD_EXAMPLES to avoid loading examples
export AIRFLOW__CORE__LOAD_EXAMPLES=False

# The Standalone command will initialise the database, make a user, and start all components for you.
airflow standalone

# # Initialize airflow db
# airflow db init
# airflow users create \
#     --username admin \
#     --firstname Peter \
#     --lastname Parker \
#     --role Admin \
#     --email spiderman@superhero.org
# airflow webserver --port 8080
# airflow scheduler

# # Confirm DAGs are being detected
airflow dags list
