from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import polars as pl

def polars_test_task():
    # Create a simple DataFrame
    df = pl.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "score": [85, 92, 78]
    })
    
    # Add a new column
    df = df.with_columns((pl.col("score") * 1.1).alias("adjusted_score"))
    
    # Filter rows
    filtered = df.filter(pl.col("adjusted_score") > 80)
    
    print("Original DataFrame:")
    print(df)
    print("\nFiltered DataFrame (adjusted_score > 80):")
    print(filtered)

# Define the DAG
with DAG(
    dag_id="polars_test_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,  # Run manually
    catchup=False,
    tags=["test", "polars"]
) as dag:

    run_polars = PythonOperator(
        task_id="run_polars_test",
        python_callable=polars_test_task
    )
