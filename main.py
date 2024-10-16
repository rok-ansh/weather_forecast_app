import streamlit as st
import plotly_express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of Forecast Days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

dates, temperature = get_data(place, days, option)

figure = px.line(x=dates, y=temperature,
                 labels={'x': 'Date', 'y': 'Temperature(C)'})
st.plotly_chart(figure)
