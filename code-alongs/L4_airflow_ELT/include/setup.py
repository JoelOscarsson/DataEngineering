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
    pass





