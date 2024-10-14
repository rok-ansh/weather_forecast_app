import streamlit as st
import plotly_express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of Forecast Days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2024-20-10", "2024-21-10", "2024-22-10"]
    temperature = [12, 15, 20]
    temperature = [days * i for i in temperature]
    return dates, temperature


dates, temperature = get_data(days)

figure = px.line(x=dates, y=temperature,
                 labels={'x': 'Date', 'y': 'Temperature(C)'})
st.plotly_chart(figure)
