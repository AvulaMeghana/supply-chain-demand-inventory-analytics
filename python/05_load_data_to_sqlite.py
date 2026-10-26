
import pandas as pd
import sqlite3
from pathlib import Path

# Locate project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent

csv_path = PROJECT_DIR / "data" / "sales_data_prepared.csv"
db_path = PROJECT_DIR / "data" / "supply_chain.db"

# Load the prepared dataset
df = pd.read_csv(csv_path)

# Create the SQLite database and table
connection = sqlite3.connect(db_path)

df.to_sql(
    "sales_inventory",
    connection,
    if_exists="replace",
    index=False
)

# Verify the number of records
result = pd.read_sql_query(
    "SELECT COUNT(*) AS total_records FROM sales_inventory",
    connection
)

print("Database created successfully!")
print("Total records loaded:", result.iloc[0]["total_records"])
print("Database location:", db_path)

connection.close()
