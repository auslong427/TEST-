import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder

st.set_page_config(page_title="Task Editor", layout="wide")

st.title("Task Spreadsheet")

# Load existing tasks or create empty DataFrame if file missing
try:
    df = pd.read_csv("tasks.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Task", "Owner", "Due Date", "Status"])

# Configure grid for editing
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(editable=True)
grid_options = gb.build()

st.write("Edit tasks directly in the grid. Use the Save button when you're done.")

grid_response = AgGrid(
    df,
    gridOptions=grid_options,
    update_mode="MODEL_CHANGED",
    editable=True,
    fit_columns_on_grid_load=True,
)

updated_df = grid_response["data"]

# Save updated data back to CSV
if st.button("Save to CSV"):
    updated_df.to_csv("tasks.csv", index=False)
    st.success("Saved updates to tasks.csv")
