from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_test():
    print("Check if sync")

dag = DAG(
    "github_sync_test",
    description = "github_sync_test",
    schedule_interval = "0 0 * * *",
    start_date = datetime(2023,1,1),
    catchup = False
)

print_test_task = PythonOperator(
    task_id = "github_sync_test",
    python_callable = print_test,
    dag = dag
)

print_test_task