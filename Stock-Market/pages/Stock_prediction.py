import streamlit as st 
from pages.utils.model_train import get_data,stationary_check,get_rolling_mean,get_diff_order,fit_model,evaluate_model,scaling,get_forecast,inverse_scaling
import pandas as pd
from pages.utils.plotly_figure import plotly_table,Moving_Average_forecast


st.set_page_config(
    page_title = "Stock Prediction",
    page_icon = "chart_with_downwards_trend",
    layout = "wide"
)

st.title("Stock Prediction")
st.page_link("Trading_App.py", label="🏠 Back to Home")

col1,col2,col3 = st.columns(3)

with col1:
    ticker = st.text_input("Stock Ticker","AAPL")

rmse = 0 
st.subheader('Predicting Next 30 days Close Price for : ' + ticker)

close_price = get_data(ticker)
rolling_price = get_rolling_mean(close_price)

diff_order = get_diff_order(rolling_price)
scaled_data , scaler = scaling(rolling_price)
rmse = evaluate_model(scaled_data,diff_order)

st.write('**Model RMSE Score:**',rmse)

forecast = get_forecast(scaled_data, diff_order)

forecast['Close'] = inverse_scaling(scaler,forecast['Close'])
st.write("#### Forecast Data (Next 30 days)")
fig_tail = plotly_table(forecast.sort_index(ascending = True).round(3))
fig_tail.update_layout(height = 220)
st.plotly_chart(fig_tail, use_conatiner_width =True)

forecast = pd.concat([rolling_price,forecast])

st.plotly_chart(Moving_Average_forecast(forecast.iloc[150:]),use_container_width =True )                                    