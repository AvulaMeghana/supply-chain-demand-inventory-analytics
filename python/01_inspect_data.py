
import pandas as pd
from pathlib import Path

# 1. Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# 2. Locate the CSV dataset
file_path = PROJECT_DIR / "data" / "sales_data.csv"

# 3. Check whether the file exists
if not file_path.exists():
    print("Dataset file not found!")
    print("Expected location:", file_path)
else:
    # 4. Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # 5. Display the first 5 rows
    print("\n--- FIRST 5 ROWS ---")
    print(df.head())

    # 6. Display the number of rows and columns
    print("\n--- DATASET SHAPE ---")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    # 7. Display all column names
    print("\n--- COLUMN NAMES ---")
    print(df.columns.tolist())

    # 8. Display data types and missing values
    print("\n--- DATA INFORMATION ---")
    df.info()

    # 9. Count missing values in each column
    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    # 10. Count duplicate rows
    print("\n--- DUPLICATE ROWS ---")
    print(df.duplicated().sum())

    # 11. Display summary statistics
    print("\n--- NUMERICAL SUMMARY ---")
    print(df.describe())
