from airflow.providers.amazon.aws.hooks.s3 import S3Hook

@task
def read_csv_from_s3():
    hook = S3Hook(aws_conn_id="aws_onyxia")

    obj = hook.get_key(
        key="airflow/titanic.csv",
        bucket_name="lmarti"
    )

    df = pd.read_csv(obj.get()["Body"])
    print(df.head())
