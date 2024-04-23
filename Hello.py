import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

stock = st.selectbox('Stock Name', ['AAPL', 'AMZN', 'NVDA', 'ORCL'])
time = st.slider('When',
                 min_value=datetime(2020, 1, 1),
                 max_value=datetime(2024, 4, 23),
                 format='YY/MM/DD')

df = yf.download(stock, start=time, end='2024-04-23')

fig, ax = plt.subplots()
plt.xticks(rotation=90)
ax.plot(df['Open'])
st.pyplot(fig)

agg = df.agg(['min', 'max'])
st.write(agg)
