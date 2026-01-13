import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from prefect import flow, task
from shared.etl_logic import extract_data, transform_data, load_data

@task(retries=2, retry_delay_seconds=10)
def extract(input_path):
    return extract_data(input_path)

@task(retries=2, retry_delay_seconds=10)
def transform(df):
    return transform_data(df, excluded_countries=["US"])

@task
def load(df, output_path):
    load_data(df, output_path)

@flow
def user_activity_flow(input_path: str, output_path: str):
    df = extract(input_path)
    df2 = transform(df)
    load(df2, output_path)

if __name__ == "__main__":
    user_activity_flow(
        input_path="../data/user_events.csv",
        output_path="../data/prefect_output.parquet",
    )
