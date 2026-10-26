# Supply Chain Demand & Inventory Analytics

## Project Overview

This project analyzes retail demand, sales, and inventory data using Python, SQL, and Microsoft Excel. The objective is to identify demand patterns, understand category-wise performance, identify top-selling products, and flag records where demand exceeds available inventory.

The analysis demonstrates how data analytics can support inventory monitoring, demand planning, and business decision-making.

## Objectives

- Inspect and validate retail sales and inventory data.
- Analyze demand and sales trends over time.
- Compare performance across product categories.
- Identify top-selling products.
- Flag potential inventory risks by comparing demand with inventory levels.
- Use SQL queries and Excel visualizations to summarize findings and support business recommendations.

## Tools and Technologies

- **Python:** pandas, NumPy, Matplotlib
- **SQL:** SQLite
- **Microsoft Excel:** PivotTables, clustered bar/column charts, summaries, and reports
- **Git and GitHub:** Version control and project sharing

## Dataset

The project uses a retail store inventory and demand forecasting dataset obtained from Kaggle.

**Dataset:** [Retail Store Inventory and Demand Forecasting](https://www.kaggle.com/dsv/11895299)

The dataset contains 76,000 records and 16 original columns, including:

- Date
- Store ID
- Product ID
- Category
- Region
- Inventory Level
- Units Sold
- Units Ordered
- Price
- Discount
- Demand

The dataset covers the period from January 2022 to January 2024.

**Note:** The results describe the supplied dataset and should not be interpreted as actual business performance from a real retailer.

## Project Workflow

### 1. Data Inspection and Validation — Python

- Loaded and inspected the dataset using pandas.
- Checked column types, missing values, duplicate records, and negative numeric values.
- Converted the date column to a date format.
- Saved the prepared dataset for subsequent analysis.

**Validation results:**
- Total records: 76,000
- Missing values: 0 in the inspected columns
- Exact duplicate records: 0
- Invalid dates: 0
- Repeated store-product-date combinations: 0

### 2. Demand and Sales Analysis — Python

Analyzed demand and sales at monthly, category, and product levels.

Generated outputs:
- Monthly demand summary
- Category-wise demand and sales summary
- Top 10 products by units sold
- Charts for monthly demand, category demand, and top-selling products

### 3. Inventory Risk Analysis — Python

Created a screening indicator to flag records where:

`Demand > Inventory Level`

This indicator highlights records that may require further inventory investigation. It does not independently confirm stockouts or lost sales.

### 4. SQL Analysis — SQLite

Loaded the prepared dataset into a SQLite database and performed queries to analyze:

- Overall demand and units sold
- Category-wise demand and sales
- Top 10 products by sales
- Potential inventory risk by category
- Products with higher potential inventory risk percentages

### 5. Excel Analysis and Reporting

Created Excel PivotTables, charts, and written summaries for:

- Category Analysis: demand and units sold by category
- Top Products: products ranked by units sold
- Inventory Risk: records flagged for potential inventory risk by category

These outputs make the findings easier to compare and communicate.

## Key Findings

### Overall Performance

- Total recorded demand: **7,928,104**
- Total units sold: **6,750,876**
- Records flagged for potential inventory risk: **10,394 out of 76,000 (13.68%)**

### Category Analysis

- Groceries recorded the highest total demand at **3,677,684**.
- Clothing recorded the second-highest total demand at **1,369,456**.
- Electronics recorded the lowest total demand at **889,036** among the five categories.

### Product Analysis

- Product **P0007** had the highest total units sold among the products in the dataset, at **379,709**.
- Product **P0009** recorded total demand of **450,324**.

### Potential Inventory Risk

- Clothing had the highest category-level risk percentage at **19.42%** (2,362 of 12,160 records).
- Toys followed at **14.97%** (1,593 of 10,640 records).
- Furniture had the lowest risk percentage at **7.84%** (1,073 of 13,680 records).

## Business Recommendations

- Monitor inventory levels more closely for categories with higher potential risk percentages.
- Review demand and replenishment patterns for products frequently flagged by the screening indicator.
- Use monthly demand summaries to support planning and resource allocation.
- Investigate records where demand exceeds inventory before concluding that a stockout occurred.
- Reassess inventory policies using additional business information, such as lead times, reorder points, and supplier constraints, where available.

## Limitations

- The analysis is based on the supplied dataset and may not represent the operations of a real retailer.
- The `Demand` field and `Units Sold` field are not interchangeable.
- The potential inventory risk indicator is a screening measure, not proof of stockouts.
- The analysis does not establish causal relationships between demand and factors such as promotions, weather, or seasonality.
- No forecasting model or Power BI dashboard is included in the completed project scope.

## Project Structure

```text
Supply_Chain_Analytics/
├── data/
│   ├── sales_data.csv
│   ├── sales_data_prepared.csv
│   └── supply_chain.db
├── python/
│   ├── 01_inspect_data.py
│   ├── 02_validate_data.py
│   ├── 03_demand_analysis.py
│   ├── 04_inventory_analysis.py
│   ├── 05_load_data_to_sqlite.py
│   ├── 06_sql_analysis.py
│   └── 07_sql_inventory_risk.py
├── sql/
├── excel/
│   └── Supply_Chain_Analysis.xlsx
├── outputs/
└── README.md
```

*The structure above describes the intended organization; ensure the listed files and folders exist in your final repository before publishing.*

## How to Run

1. Install Python.
2. Install the required packages:

   ```bash
   python -m pip install pandas numpy matplotlib
   ```

3. Place the dataset at `data/sales_data.csv`.
4. Run the Python scripts from the project root in numerical order:

   ```bash
   python python/01_inspect_data.py
   python python/02_validate_data.py
   python python/03_demand_analysis.py
   python python/04_inventory_analysis.py
   python python/05_load_data_to_sqlite.py
   python python/06_sql_analysis.py
   python python/07_sql_inventory_risk.py
   ```

5. Open `excel/Supply_Chain_Analysis.xlsx` to view the Excel analysis, PivotTables, charts, and summaries.

## Conclusion

This project demonstrates a practical analytics workflow using Python, SQL, and Excel to inspect retail data, analyze demand and sales, rank products, and identify potential inventory risks. The findings can help prioritize further investigation and support data-informed inventory planning.