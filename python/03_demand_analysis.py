
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Find the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Load the prepared dataset
file_path = PROJECT_DIR / "data" / "sales_data_prepared.csv"
df = pd.read_csv(file_path)

# Convert Date into a proper date format
df["Date"] = pd.to_datetime(df["Date"])

# Create an output folder for tables and charts
output_folder = PROJECT_DIR / "outputs"
output_folder.mkdir(exist_ok=True)

# -----------------------------------------
# ANALYSIS 1: MONTHLY DEMAND AND SALES
# -----------------------------------------

# Create a month column
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Calculate monthly totals
monthly_summary = (
    df.groupby("Month")
    .agg(
        Total_Demand=("Demand", "sum"),
        Total_Units_Sold=("Units Sold", "sum"),
        Average_Inventory=("Inventory Level", "mean")
    )
    .reset_index()
)

print("\n--- MONTHLY DEMAND AND SALES ---")
print(monthly_summary.to_string(index=False))

# Save the monthly summary
monthly_summary.to_csv(
    output_folder / "monthly_demand_summary.csv",
    index=False
)

# Plot monthly demand
plt.figure(figsize=(12, 5))
plt.plot(
    monthly_summary["Month"],
    monthly_summary["Total_Demand"],
    marker="o"
)
plt.title("Monthly Demand Trend")
plt.xlabel("Month")
plt.ylabel("Total Recorded Demand")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(output_folder / "monthly_demand.png")
plt.close()

# -----------------------------------------
# ANALYSIS 2: CATEGORY PERFORMANCE
# -----------------------------------------

category_summary = (
    df.groupby("Category")
    .agg(
        Total_Demand=("Demand", "sum"),
        Total_Units_Sold=("Units Sold", "sum"),
        Average_Inventory=("Inventory Level", "mean")
    )
    .sort_values("Total_Demand", ascending=False)
    .reset_index()
)

print("\n--- CATEGORY PERFORMANCE ---")
print(category_summary.to_string(index=False))

category_summary.to_csv(
    output_folder / "category_summary.csv",
    index=False
)

# Plot category demand
plt.figure(figsize=(9, 5))
plt.bar(
    category_summary["Category"],
    category_summary["Total_Demand"]
)
plt.title("Total Recorded Demand by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Recorded Demand")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(output_folder / "category_demand.png")
plt.close()

# -----------------------------------------
# ANALYSIS 3: TOP 10 PRODUCTS
# -----------------------------------------

product_summary = (
    df.groupby("Product ID")
    .agg(
        Total_Demand=("Demand", "sum"),
        Total_Units_Sold=("Units Sold", "sum")
    )
    .sort_values("Total_Units_Sold", ascending=False)
    .head(10)
    .reset_index()
)

print("\n--- TOP 10 PRODUCTS BY UNITS SOLD ---")
print(product_summary.to_string(index=False))

product_summary.to_csv(
    output_folder / "top_10_products.csv",
    index=False
)

# Plot top 10 products
plt.figure(figsize=(10, 5))
plt.bar(
    product_summary["Product ID"],
    product_summary["Total_Units_Sold"]
)
plt.title("Top 10 Products by Units Sold")
plt.xlabel("Product ID")
plt.ylabel("Total Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_folder / "top_10_products.png")
plt.close()

print("\nAnalysis completed successfully!")
print("Summary tables and charts saved in:", output_folder)
