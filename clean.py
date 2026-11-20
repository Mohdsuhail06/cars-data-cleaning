import pandas as pd

df = pd.read_csv("cars_raw.csv")
rows_before = len(df)

# 1. Remove exact duplicate rows
df = df.drop_duplicates()

# 2. A car with no price can't teach us anything: drop it
df = df.dropna(subset=["price_value_JOD"])

# 3. Fake prices (like 999,999 or 7,000,000): keep only realistic ones
df = df[(df["price_value_JOD"] >= 500) & (df["price_value_JOD"] <= 200_000)]

# 4. Year: turn text into numbers ("Older than 1970" becomes empty), then drop empty
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df = df.dropna(subset=["year"])
df["year"] = df["year"].astype(int)

# 5. Hidden meaning: empty mileage + text "200,000" means 200,000 km or more
hidden_200k = df["mileage_km"].isna() & (df["mileage_text"] == "200,000")
df.loc[hidden_200k, "mileage_km"] = 200_000

# 6. New column: car age (the data was collected in 2024)
df["car_age"] = 2024 - df["year"]

df.to_csv("cars_clean.csv", index=False)

print(f"Rows before: {rows_before}, rows after: {len(df)}")
print(f"Filled hidden mileage for {hidden_200k.sum()} cars")

print("\n--- Average price by brand (top 10 brands by count) ---")
top_brands = df["make"].value_counts().head(10).index
avg_price = df[df["make"].isin(top_brands)].groupby("make")["price_value_JOD"].mean()
print(avg_price.sort_values(ascending=False).round(0))
print("\n--- Average price by fuel type ---")
avg_fuel = df.groupby("fuel_type")["price_value_JOD"].mean()
print(avg_fuel.sort_values(ascending=False).round(0))