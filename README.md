# Power Apps Sales Order Tracker

This repository contains sample data and a Dataverse schema for building a drag-and-drop sales order tracker in Microsoft Power Apps or Power Pages. The design uses ABB-themed colors and requires minimal code.

## Getting Started
1. Import the tables defined in [`DATAVERSE_SCHEMA.md`](DATAVERSE_SCHEMA.md) into Dataverse.
2. Create a new Power Apps app or Power Pages site and connect to these tables.
3. Use standard form and view controls to display **SalesOrder** and **Item** records. The schema includes fields for pushout comments, production orders, and item categories.
4. Add a calculated **Late** column to highlight items that are past their estimated ship date.
5. Optional: build a change tracking flow that writes updates to the **ChangeHistory** table.


## Sample Data
`sample_sales_orders.csv` and `sample_items.csv` provide example records that match the Dataverse schema. Import them with Power Apps or Power Query. `tasks.csv` is left from the optional Streamlit demo.

## Streamlit Preview (Optional)
A lightweight Streamlit app (`streamlit_app.py`) is included for quick prototyping. Run it with:
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
This app shows how an editable grid could look before moving to Power Apps.
