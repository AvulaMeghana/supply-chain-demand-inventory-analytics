
import pandas as pd
from pathlib import Path

# Find the project folder and dataset
PROJECT_DIR = Path(__file__).resolve().parent.parent
file_path = PROJECT_DIR / "data" / "sales_data.csv"

# Load the original dataset
df = pd.read_csv(file_path)

print("--- ORIGINAL DATA TYPES ---")
print(df.dtypes)

# Convert Date from text to an actual date format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print("\n--- DATE RANGE ---")
print("First date:", df["Date"].min())
print("Last date:", df["Date"].max())
print("Invalid dates:", df["Date"].isna().sum())

# Count stores, products, and categories
print("\n--- DATASET OVERVIEW ---")
print("Unique stores:", df["Store ID"].nunique())
print("Unique products:", df["Product ID"].nunique())
print("\nProduct categories:")
print(df["Category"].value_counts())

# Check for negative values in important numeric columns
numeric_columns = [
    "Inventory Level",
    "Units Sold",
    "Units Ordered",
    "Price",
    "Discount",
    "Competitor Pricing",
    "Demand"
]

print("\n--- NEGATIVE VALUE CHECK ---")
for column in numeric_columns:
    print(column, ":", (df[column] < 0).sum())

# Count records with zero inventory or zero sales
print("\n--- ZERO VALUE CHECK ---")
print("Zero inventory records:", (df["Inventory Level"] == 0).sum())
print("Zero sales records:", (df["Units Sold"] == 0).sum())
print("Zero demand records:", (df["Demand"] == 0).sum())

# Check repeated store-product-date combinations
key_columns = ["Date", "Store ID", "Product ID"]
print("\n--- STORE-PRODUCT-DATE CHECK ---")
print(
    "Repeated combinations:",
    df.duplicated(subset=key_columns).sum()
)

# Compare recorded demand and units sold
print("\n--- DEMAND AND SALES COMPARISON ---")
print("Correlation:", df["Demand"].corr(df["Units Sold"]))
print("Records where demand differs from sales:",
      (df["Demand"] != df["Units Sold"]).sum())

# Save a prepared copy without changing the original file
output_path = PROJECT_DIR / "data" / "sales_data_prepared.csv"
df.to_csv(output_path, index=False)

print("\nPrepared dataset saved to:", output_path)
