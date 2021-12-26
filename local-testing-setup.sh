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
export AIRFLOW_HOME=$(pwd)

# Initialize airflow db
airflow db reset

# Confirm DAGs are being detected
airflow dags list