from shared.etl_logic import extract_data, transform_data, load_data

df = extract_data("data/user_events.csv")
df2 = transform_data(df, excluded_countries=["US"])
load_data(df2, "data/output.parquet")

print(df2)
