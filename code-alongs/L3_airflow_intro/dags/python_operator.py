from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from pathlib import Path
import numpy as np

simulation_path = Path(__file__).parents[1] / "data" / "dice_simulations"

def _dice_rolls(number_rolls):
    return list(np.random.randint(1,7, size=number_rolls))


# xcom pull to get the data from the previous task
def _save_dice_experiment(task_instance):
    simulation_data = task_instance.xcom_pull(task_ids=["dice_rolls"])

    # validation code can be added here
    # ...

    with open(simulation_path / "dice_rolls.txt", "a") as file:
        file.write(f"Dice rolls {datetime.now()} \n")
        file.write(f"{simulation_data} \n\n")


with DAG(dag_id = "dice_simulator", start_date=datetime(2023,6,7)):
    setup_directories = BashOperator(task_id = "setup_directories",
                                      bash_command=f"mkdir -p {simulation_path}")
    dice_rolls = PythonOperator(task_id = "dice_rolls", 
                                python_callable= _dice_rolls,
                                op_args=[10], # makes array of 10 dice rolls between 1 and 6
                                do_xcom_push=True) # sparar resultatet i xcom databas
    
    save_dice_experiment = PythonOperator(task_id = "save_dice", python_callable=_save_dice_experiment)

    setup_directories >> dice_rolls >> save_dice_experiment
