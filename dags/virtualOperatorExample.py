from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator

def callable_virtualenv():
    """
    Example function that will be performed in a virtual environment.
    """
    from time import sleep
    from colorama import Back, Fore, Style

    print(Fore.RED + "some red text")
    print(Back.GREEN + "and with a green background")
    print(Style.DIM + "and in dim text")
    print(Style.RESET_ALL)
    
    for _ in range(4):
        print(Style.DIM + "Please wait...", flush=True)
        sleep(1)
        
    print("Finished")

# Define the DAG
with DAG(
    dag_id="virtualenv_example_dag",
    start_date=datetime(2026, 2, 26),
    schedule=None,  # Set to your desired schedule, None = manual trigger
    catchup=False,
    tags=["example", "virtualenv"],
) as dag:

    # Define the PythonVirtualenvOperator task
    virtualenv_task = PythonVirtualenvOperator(
        task_id="virtualenv_python",
        python_callable=callable_virtualenv,
        requirements=["colorama==0.4.0"],
        system_site_packages=False,
    )

    # If you have more tasks, you can set dependencies here
    # e.g., virtualenv_task >> another_task
