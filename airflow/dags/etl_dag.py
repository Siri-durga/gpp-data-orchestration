import sys
sys.path.append("/opt/airflow")
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from shared.etl_logic import extract_data, transform_data, load_data

default_args = {
    "retries": 2,
    "retry_delay": timedelta(seconds=10),
}

def extract(**context):
    df = extract_data(context["params"]["input_path"])
    tmp_path = "/opt/airflow/data/extracted.csv"
    df.to_csv(tmp_path, index=False)
    context["ti"].xcom_push(key="extracted_path", value=tmp_path)


def transform(**context):
    import pandas as pd

    extracted_path = context["ti"].xcom_pull(key="extracted_path")
    df = pd.read_csv(extracted_path, parse_dates=["timestamp"])

    df2 = transform_data(df, excluded_countries=["US"])

    tmp_path = "/opt/airflow/data/transformed.parquet"
    df2.to_parquet(tmp_path, index=False)
    context["ti"].xcom_push(key="transformed_path", value=tmp_path)


def load(**context):
    import pandas as pd

    transformed_path = context["ti"].xcom_pull(key="transformed_path")
    df = pd.read_parquet(transformed_path)

    load_data(df, context["params"]["output_path"])
with DAG(
    dag_id="user_activity_etl",
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=True,
    default_args=default_args,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract,
        provide_context=True,
        params={
            "input_path": "/opt/airflow/data/user_events.csv",
            "output_path": "/opt/airflow/data/airflow_output.parquet",
        },
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform,
        provide_context=True,
    )

    load_task = PythonOperator(
    task_id="load_data",
    python_callable=load,
    provide_context=True,
    params={
        "output_path": "/opt/airflow/data/airflow_output.parquet",
    },
)

    extract_task >> transform_task >> load_task
