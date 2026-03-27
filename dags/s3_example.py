from airflow import DAG
from airflow.sdk import task
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime
import pandas as pd
from io import StringIO

# ---------------------------
# DAG definition
# ---------------------------
with DAG(
    dag_id="read_csv_s3_head",
    start_date=datetime(2026, 3, 27),
    schedule=None,  # manual trigger
    catchup=False,
    tags=["example", "s3", "minio"],
) as dag:
    @task
    def read_csv_from_s3():
        hook = S3Hook(aws_conn_id="aws_onyxia")
    
        obj = hook.get_key(
            key="airflow/titanic.csv",
            bucket_name="lmarti"
        )
    
        df = pd.read_csv(obj.get()["Body"])
        print(df.head())
        
    # Define task execution
    read_csv_from_s3()
