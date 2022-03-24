import streamlit as st
import pandas as pd
import numpy as np


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

st.title('Uber pickups in NYC')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

hist_values = np.histogram(
data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

# hours_filtered = st.line_chart('hour', 0, 24, 10)
# filt_data = data[data[[DATE_COLUMN].dt.hour].dt.hour == hours_filtered]
# st.subheader(f'Map of deliveries {hours_filtered}:00')
# st.line_chart()

chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["30", "200", "35"])
st.subheader("Uber deliveries data")
st.bar_chart(chart_data)

import time
import datetime
from datetime import datetime, date, time


d = st.date_input(
     "Check for an Uber delivery",
     datetime(2019, 9, 14))
st.subheader('Check for an Uber delivery')
st.write('Your Uber delivery is set for:', d)


st.subheader("Party Time")
if st.button("Celebrate"):
    st.balloons()
else:
    st.write("please hold for next party")    
    