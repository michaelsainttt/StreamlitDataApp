import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Electric Vehicle Population Data Explorer")


@st.cache_data
def load_data(path):
    return pd.read_csv(path)

data = load_data("Electric_Vehicle_Population_Data.csv")
tabs = st.tabs(["Overview", "Data Display", "Insights"])

#overview tab
with tabs[0]:
    st.header("Overview")
    st.markdown("""
    This app explores electric vehicle population data by state and year.  
    You can select a state, view raw data, and analyze trends over time with interactive charts.
    """)

#data tab
with tabs[1]:
    st.header("Data Display")
    if st.checkbox("Show raw data"):
        st.dataframe(data)

    if "State" in data.columns:
        states = data["State"].unique()
        selected_state = st.selectbox("Select a State", states, key="state_select")
        filtered_data = data[data["State"] == selected_state]
    else:
        filtered_data = data
        selected_state = "All States"

    st.subheader(f"Data for {selected_state}")
    st.dataframe(filtered_data)

#insight tab
with tabs[2]:
    st.header("EVs by Model Year")

    year_counts = data["Model Year"].value_counts().sort_index().reset_index()
    year_counts.columns = ["Model Year", "Number of Vehicles"]

    fig1 = px.line(
        year_counts,
        x="Model Year",
        y="Number of Vehicles",
        title="Electric Vehicles by Model Year",
        labels={
            "Model Year": "Model Year",
            "Number of Vehicles": "Number of Registered EVs"
        }
    )

    st.plotly_chart(fig1)