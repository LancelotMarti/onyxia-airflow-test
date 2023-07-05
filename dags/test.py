from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    print("HELLO")

dag = DAG(
    "hello_dag",
    description = "Simple DAG",
    schedule_interval = "0 0 * * *",
    start_date = datetime(2023,1,1),
    catchup = False
)

print_hello_task = PythonOperator(
    task_id = "print_hello_task",
    python_callable = print_hello,
    dag = dag
)

print_hello_task