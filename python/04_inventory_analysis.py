
import pandas as pd
from pathlib import Path

# Locate the project and load the data
PROJECT_DIR = Path(__file__).resolve().parent.parent
file_path = PROJECT_DIR / "data" / "sales_data_prepared.csv"

df = pd.read_csv(file_path)

# Create an output folder if it does not exist
output_folder = PROJECT_DIR / "outputs"
output_folder.mkdir(exist_ok=True)

# -----------------------------------------
# ANALYSIS 1: ZERO INVENTORY AND ZERO SALES
# -----------------------------------------

zero_inventory = df["Inventory Level"] == 0
zero_sales = df["Units Sold"] == 0

print("\n--- ZERO INVENTORY AND SALES ---")
print("Zero inventory records:", zero_inventory.sum())
print("Zero sales records:", zero_sales.sum())

print("Both zero inventory and zero sales:",
      (zero_inventory & zero_sales).sum())

print("Zero inventory but positive sales:",
      (zero_inventory & (df["Units Sold"] > 0)).sum())

print("Zero inventory but positive demand:",
      (zero_inventory & (df["Demand"] > 0)).sum())

# -----------------------------------------
# ANALYSIS 2: POTENTIAL INVENTORY RISK
# -----------------------------------------

# Screening indicator, not proof of a stockout
df["Potential_Risk"] = (
    df["Demand"] > df["Inventory Level"]
)

df["Zero_Inventory"] = zero_inventory

print("\n--- POTENTIAL INVENTORY RISK ---")
print("Records where demand exceeds inventory:",
      df["Potential_Risk"].sum())

print("Percentage of records flagged:",
      round(df["Potential_Risk"].mean() * 100, 2), "%")

# Summarize potential risk by category
category_risk = (
    df.groupby("Category")
    .agg(
        Total_Records=("Product ID", "size"),
        Risk_Records=("Potential_Risk", "sum"),
        Zero_Inventory_Records=("Zero_Inventory", "sum")
    )
    .reset_index()
)

category_risk["Risk_Percentage"] = (
    category_risk["Risk_Records"]
    / category_risk["Total_Records"] * 100
).round(2)

category_risk = category_risk.sort_values(
    "Risk_Percentage", ascending=False
)

print("\n--- INVENTORY RISK BY CATEGORY ---")
print(category_risk.to_string(index=False))

category_risk.to_csv(
    output_folder / "inventory_risk_by_category.csv",
    index=False
)

# -----------------------------------------
# ANALYSIS 3: PRODUCTS TO INVESTIGATE
# -----------------------------------------

product_risk = (
    df.groupby("Product ID")
    .agg(
        Total_Records=("Demand", "size"),
        Total_Demand=("Demand", "sum"),
        Total_Units_Sold=("Units Sold", "sum"),
        Risk_Records=("Potential_Risk", "sum"),
        Zero_Inventory_Records=("Zero_Inventory", "sum")
    )
    .reset_index()
)

product_risk["Risk_Percentage"] = (
    product_risk["Risk_Records"]
    / product_risk["Total_Records"] * 100
).round(2)

product_risk = product_risk.sort_values(
    "Risk_Percentage", ascending=False
)

print("\n--- TOP 10 PRODUCTS BY RISK PERCENTAGE ---")
print(product_risk.head(10).to_string(index=False))

product_risk.to_csv(
    output_folder / "inventory_risk_by_product.csv",
    index=False
)

print("\nInventory analysis completed!")
print("Results saved in:", output_folder)
