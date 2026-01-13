import pandas as pd
import random
import time

def extract_data(input_path):
    return pd.read_csv(input_path, parse_dates=["timestamp"])

def transform_data(df, excluded_countries):
    # Simulated intermittent failure
    if random.random() < 0.3:
        raise Exception("Simulated transform failure")

    df = df[~df["country"].isin(excluded_countries)]

    df["date"] = df["timestamp"].dt.date

    session = df.groupby("user_id")["timestamp"].agg(["min", "max"])
    session["session_duration"] = (session["max"] - session["min"]).dt.total_seconds()

    df = df.merge(session["session_duration"], on="user_id")

    agg = (
        df.groupby(["user_id", "date"])
        .size()
        .reset_index(name="event_count")
    )

    return agg

def load_data(df, output_path):
    df.to_parquet(output_path, index=False)
