# Supply Chain Demand & Inventory Analytics

## Project Overview

This project analyzes retail sales, demand, and inventory data using Python, SQL, and Excel. The objective is to understand demand patterns, identify top-selling products, and highlight potential inventory risks to support data-driven inventory planning.

## Objectives

- Analyze demand and sales across product categories.
- Identify top-selling products.
- Examine monthly demand trends.
- Identify records where demand exceeds the recorded inventory level.
- Present key findings through charts, summary tables, and Excel analysis.

## Tools and Technologies

- **Python:** Pandas, Matplotlib
- **SQL:** SQLite
- **Excel:** PivotTables, charts, and summary analysis
- **Git and GitHub:** Version control and project hosting

## Dataset

- **Source:** [Kaggle – Retail Store Inventory and Demand](https://www.kaggle.com/dsv/11895299)
- **Records:** 76,000
- **Date range:** January 2022 – January 2024
- **Product categories:** Groceries, Clothing, Furniture, Toys, and Electronics

The dataset includes date, store, product, category, inventory level, units sold, units ordered, price, and demand.

The dataset files are not included in this GitHub repository. Download the dataset from Kaggle and place the original CSV file in the `data/` folder as `sales_data.csv` before running the scripts.

## Project Workflow

1. **Data Inspection:** Examined the dataset structure, columns, and data types.
2. **Data Validation:** Checked missing values, duplicate records, dates, and numerical values.
3. **Demand Analysis:** Analyzed category-wise demand, monthly trends, and top-selling products.
4. **Inventory Risk Analysis:** Identified records where demand exceeds the recorded inventory level.
5. **SQL Analysis:** Used SQLite queries to summarize demand, sales, and inventory patterns.
6. **Excel Analysis:** Created PivotTables, charts, and summary tables to present findings.

## Key Findings

- The dataset contains **76,000 records** across five product categories.
- Total recorded demand is **7,928,104 units**.
- Total recorded units sold is **6,750,876 units**.
- Groceries has the highest recorded demand among the five categories.
- August 2023 has the highest monthly demand in the analyzed period.
- In **10,394 records (13.68%)**, demand exceeds the recorded inventory level.
- Clothing has the highest category-level proportion of these records at approximately **19.42%**.

**Note:** Records where demand exceeds inventory are potential risk indicators. They do not independently confirm actual stockouts or lost sales.

## Project Structure

```text
Supply_Chain_Analytics/
├── dashboard/
├── data/
├── excel/
│   └── Supply_Chain_Analysis.xlsx
├── outputs/
│   ├── category_demand.png
│   ├── monthly_demand.png
│   ├── top_10_products.png
│   └── analysis summary files
├── python/
│   ├── 01_inspect_data.py
│   ├── 02_validate_data.py
│   ├── 03_demand_analysis.py
│   ├── 04_inventory_analysis.py
│   ├── 05_load_data_to_sqlite.py
│   ├── 06_sql_analysis.py
│   └── 07_sql_inventory_risk.py
├── sql/
├── .gitignore
└── README.md
```

## How to Run

1. Install Python.
2. Install the required libraries:

   ```bash
   pip install pandas matplotlib
   ```

3. Download the dataset from Kaggle and place `sales_data.csv` in the `data/` folder.
4. Run the Python scripts in sequence, starting with data inspection and validation.
5. Use the SQL scripts and Excel workbook to explore the results.

SQLite is used for database analysis.

## Limitations

- The analysis identifies patterns in the available dataset and does not establish causal relationships.
- The inventory risk indicator is a screening measure, not proof of stockouts.
- The project focuses on descriptive analytics and does not implement a production demand forecasting system.

## Conclusion

This project demonstrates how Python, SQL, and Excel can be used together to analyze retail demand, sales, and inventory data. The findings help identify demand patterns, understand product performance, and highlight areas for further inventory investigation.
