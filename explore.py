import pandas as pd

df = pd.read_csv("cars_raw.csv")

print("Rows and columns:", df.shape)

print("\n--- Missing values (top 8) ---")
print(df.isna().sum().sort_values(ascending=False).head(8))

print("\n--- Duplicate rows ---")
print(df.duplicated().sum())

print("\n--- Price summary ---")
print(df["price_value_JOD"].describe())

print("\n--- 10 highest prices ---")
print(df["price_value_JOD"].sort_values(ascending=False).head(10))

print("\n--- Strange year values ---")
year_as_number = pd.to_numeric(df["year"], errors="coerce")
print(df.loc[year_as_number.isna(), "year"].value_counts(dropna=False))

print("\n--- mileage_text when mileage_km is missing ---")
print(df.loc[df["mileage_km"].isna(), "mileage_text"].value_counts(dropna=False))