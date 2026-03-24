from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

# Function to test DuckDB
def test_duckdb():
    # Lazy import inside the function
    import duckdb

    # Connect to an in-memory DuckDB database
    con = duckdb.connect(database=':memory:')
    
    # Create a simple table
    con.execute("CREATE TABLE test_table (id INTEGER, name VARCHAR);")
    con.execute("INSERT INTO test_table VALUES (1, 'Alice'), (2, 'Bob');")
    
    # Query the table
    result = con.execute("SELECT * FROM test_table;").fetchall()
    
    print("DuckDB query results:", result)
    
    # Close connection
    con.close()

# Define the DAG
with DAG(
    dag_id='duckdb_test_dag',
    start_date=datetime(2026, 3, 17),
    schedule=None,  # Manual trigger
    catchup=False,
    tags=['test', 'duckdb']
) as dag:

    run_duckdb_test = PythonOperator(
        task_id='run_duckdb_test',
        python_callable=test_duckdb,
        executor_config={
            "KubernetesExecutor": {
                "image": "lancelotmarti/airflow-executor:v0.3"
            }
        }
    )
