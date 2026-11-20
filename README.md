# cars-data-cleaning

Cleans **10,921 real used-car listings from Jordan** (2024) with **pandas**,
and saves a clean version (`cars_clean.csv`).

## Problems found and how they were fixed
| Problem | Fix |
|---|---|
| 699 duplicate listings | Removed with `drop_duplicates()` |
| 1,182 cars with no price | Removed |
| Fake prices (999,999 or 7,000,000 JOD) | Kept only prices between 500 and 200,000 JOD |
| Year written as text (`Older than 1970`) or missing | Converted to numbers, unknown years removed |
| **Hidden meaning:** empty `mileage_km` + `mileage_text = "200,000"` | Means 200,000 km or more, filled with 200,000 (1,775 cars) |

## How to run
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python explore.py
python clean.py
```

## Results
10,921 rows before, **9,691** after.

| Finding | Value |
|---|---|
| Most expensive brands (top 10) | Mercedes Benz and BMW (~21,800 JOD average) |
| Cheapest fuel type | Gasoline (~9,855 JOD average) |
| Electric vs gasoline | Electric cars cost ~5,400 JOD more on average |

## Limitation
Averages can mislead: groups with few cars (like Mild Hybrid) give unstable numbers.
The 200,000 JOD price limit is a judgment call.

## Data source
Jordan used-car listings, [Mendeley Data](https://data.mendeley.com/datasets/ddcz486x5t), licensed **CC BY 4.0**.
