import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from dbhelper import DB
import pandas as pd

db=DB()
def show_about():
    st.title("✈️ Flight Data Explorer – About the Project")

    st.markdown("""
    ### 🔍 Overview
    **Flight Data Explorer** is a data-driven web app that lets users analyze flight data using interactive visualizations and filters.

    This project is powered by:
    - **Streamlit** for frontend UI
    - **Python (MySQL Connector)** for backend logic
    - **MySQL (via XAMPP)** as the database
    - **Flight booking CSV** as the data source

    ### 🧩 Features
    - 🔎 **Search Flights** by Source and Destination
    - 📊 **Airline Frequency Analysis**
    - 📅 **Daily Journey Frequency**
    - 🧭 **Most Busy Airports Detection**
    - 📥 **Direct CSV import into MySQL**

    ### 🛠️ Tech Stack
    | Component   | Technology |
    |-------------|------------|
    | Frontend    | Streamlit |
    | Backend     | Python + MySQL Connector |
    | Database    | MySQL (via XAMPP) |
    | Data Format | CSV |

    ### 👨‍💻 Developer Note
    Built to demonstrate MySQL integration, data querying, and visualization in real-time.

    """)
st.sidebar.title("Flights analytics")
user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])
if user_option == 'Check Flights':
    st.title('Check Flights')
    col1, col2 = st.columns(2)

    city = db.fetch_city_names()
    with col1:
        source = st.selectbox('Source', sorted(city))
    with col2:
        destination = st.selectbox('Destination', sorted(city))
    if st.button('Search'):
        rows, columns = db.fetch_all_flights_df(source, destination)
        st.dataframe(pd.DataFrame(rows, columns=columns))

elif user_option == 'Analytics':
    airline,frequency=db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    date, frequency2 = db.daily_frequency()

    print(len(date))
    print(len(frequency2))
    fig = px.line(
        x=date,
        y=frequency2
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:
    show_about()

