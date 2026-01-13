import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from dagster import op, job, RetryPolicy
from shared.etl_logic import extract_data, transform_data, load_data


@op
def extract_op(context):
    return extract_data("../data/user_events.csv")


@op(
    retry_policy=RetryPolicy(
        max_retries=2,
        delay=10,
    )
)
def transform_op(context, df):
    return transform_data(df, excluded_countries=["US"])


@op
def load_op(context, df):
    load_data(df, "../data/dagster_output.parquet")


@job
def user_activity_job():
    df = extract_op()
    df2 = transform_op(df)
    load_op(df2)


if __name__ == "__main__":
    user_activity_job.execute_in_process()

