import streamlit as st

st.set_page_config(
    page_title = "Trading App",
    page_icon = "heavy_dollar_sign",
    layout = "wide"
)

st.title("Trading Guide App :bar_chart:")



st.header("We provide the Greatest platform for you to collect al information prior to investing in stocks.")
st.image("app.png")

st.markdown("## We provide the following services:")

st.markdown("### :one: Stock Information")
st.page_link("pages/Stock_analysis.py", label=":bar_chart: Get to Analysis page.")
st.write("Through this page, you can see all the information about stocks. ")

st.markdown("### :two: Stock Prediction")
st.page_link("pages/Stock_prediction.py", label=":bar_chart: Get to Prediction page.")

st.write("You can explore the predicted closing prices the next 30 days based on historical stock data adn advanced forecasting.Use this tool to gain valuable insights to make trends and make informed investment decisions.")




