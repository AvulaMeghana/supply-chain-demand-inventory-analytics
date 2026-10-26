
import sqlite3
from pathlib import Path
import pandas as pd

# Locate the database
PROJECT_DIR = Path(__file__).resolve().parent.parent
db_path = PROJECT_DIR / "data" / "supply_chain.db"

connection = sqlite3.connect(db_path)

# QUERY 1: Total demand and total sales
query1 = """
SELECT
    SUM(Demand) AS Total_Demand,
    SUM("Units Sold") AS Total_Units_Sold
FROM sales_inventory;
"""

print("\n--- OVERALL DEMAND AND SALES ---")
print(pd.read_sql_query(query1, connection).to_string(index=False))


# QUERY 2: Demand and sales by category
query2 = """
SELECT
    Category,
    SUM(Demand) AS Total_Demand,
    SUM("Units Sold") AS Total_Units_Sold
FROM sales_inventory
GROUP BY Category
ORDER BY Total_Demand DESC;
"""

print("\n--- CATEGORY-WISE PERFORMANCE ---")
print(pd.read_sql_query(query2, connection).to_string(index=False))


# QUERY 3: Top 10 products by units sold
query3 = """
SELECT
    "Product ID",
    SUM(Demand) AS Total_Demand,
    SUM("Units Sold") AS Total_Units_Sold
FROM sales_inventory
GROUP BY "Product ID"
ORDER BY Total_Units_Sold DESC
LIMIT 10;
"""

print("\n--- TOP 10 PRODUCTS BY SALES ---")
print(pd.read_sql_query(query3, connection).to_string(index=False))


connection.close()
print("\nSQL analysis completed!")
