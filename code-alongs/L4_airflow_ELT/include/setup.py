from airflow.operators.bash import BashOperator
from pathlib import Path
from airflow.decorators import task_group


## think about this filepath, and use it myself later
data_path = Path(__file__).parents[1] / "data"
datalake_path = data_path / "datalake"
data_warehouse_path = data_path / "data_warehouse"


# kan innehålla flera task i denna grupp
@task_group(group_id="setup_data_directories")
def setup_directories():
    create_directories = BashOperator(task_id = "create_directories",
                                       bash_command=f"mkdir -p {datalake_path} {data_warehouse_path}")
    success_setup = BashOperator(task_id = "setup_success",
                                 bash_command="echo 'Setup data directories successfull'")

    create_directories >> success_setup
    
