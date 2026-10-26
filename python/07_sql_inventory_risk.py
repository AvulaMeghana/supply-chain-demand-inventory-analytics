
import sqlite3
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
db_path = PROJECT_DIR / "data" / "supply_chain.db"

connection = sqlite3.connect(db_path)

# QUERY 1: Inventory risk by category
query1 = """
SELECT
    Category,
    COUNT(*) AS Total_Records,
    SUM(
        CASE
            WHEN Demand > "Inventory Level" THEN 1
            ELSE 0
        END
    ) AS Risk_Records,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN Demand > "Inventory Level" THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS Risk_Percentage
FROM sales_inventory
GROUP BY Category
ORDER BY Risk_Percentage DESC;
"""

print("\n--- INVENTORY RISK BY CATEGORY ---")
print(pd.read_sql_query(query1, connection).to_string(index=False))


# QUERY 2: Top 10 products by inventory risk percentage
query2 = """
SELECT
    "Product ID",
    COUNT(*) AS Total_Records,
    SUM(
        CASE
            WHEN Demand > "Inventory Level" THEN 1
            ELSE 0
        END
    ) AS Risk_Records,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN Demand > "Inventory Level" THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS Risk_Percentage
FROM sales_inventory
GROUP BY "Product ID"
ORDER BY Risk_Percentage DESC
LIMIT 10;
"""

print("\n--- TOP 10 PRODUCTS BY RISK PERCENTAGE ---")
print(pd.read_sql_query(query2, connection).to_string(index=False))

connection.close()

print("\nSQL inventory risk analysis completed!")
