
# 📈 Stock Market Time Series Forecasting

This project analyzes and forecasts stock market trends using **time series analysis** techniques. We explore statistical models like **ARIMA**, **SARIMA**, and **Facebook Prophet**, as well as a deep learning-based **LSTM** model to make short- and long-term stock price predictions.

---

## 🎯 Project Objectives

- Understand time series data characteristics: trend, seasonality, noise.
- Preprocess and visualize real-world stock market data.
- Implement forecasting models (ARIMA, SARIMA, Prophet, LSTM).
- Compare model performance using evaluation metrics.
- Optionally deploy results using Streamlit.

---

## 🛠️ Tech Stack

- **Languages:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-learn, Statsmodels
- **Forecasting:** Facebook Prophet, TensorFlow/Keras (LSTM)
- **Deployment:** Streamlit (optional)
- **Visualization:** Plotly, Seaborn, Matplotlib

---

## 📁 Folder Structure

```
stock-market-time-series-forecasting/
│
├── data/                   # Contains raw and cleaned stock data
├── notebooks/              # Jupyter notebooks for each model
│   ├── 01_EDA_Preprocessing.ipynb
│   ├── 02_ARIMA_Model.ipynb
│   ├── 03_SARIMA_Model.ipynb
│   ├── 04_Prophet_Model.ipynb
│   └── 05_LSTM_Model.ipynb
│
├── visuals/                # Plots and visualizations
├── app/                    # Streamlit app
├── reports/                # Final report and presentation
│   └── Time_Series_Stock_Market_Report.pdf
├── requirements.txt
├── README.md
```

---

## 📊 Models Implemented

| Model   | Type         | Handles Seasonality | Strengths                   |
|---------|--------------|---------------------|-----------------------------|
| ARIMA   | Statistical  | ❌                  | Simple & fast               |
| SARIMA  | Statistical  | ✅                  | Seasonality support         |
| Prophet | Additive     | ✅ (auto-detects)   | Easy to tune, robust        |
| LSTM    | Deep Learning| ✅ (learned patterns)| Best for non-linear trends |

---

## 📈 Sample Forecast Comparison

| Model   | RMSE   | MAPE   | Comments            |
|---------|--------|--------|---------------------|
| ARIMA   | 11.2   | 3.5%   | Baseline model      |
| SARIMA  | 9.8    | 3.1%   | Seasonal adjustment |
| Prophet | 10.1   | 3.0%   | Auto trend capture  |
| LSTM    | 7.9    | 2.4%   | Best performance    |

---


## 📄 Report

You can find the full project report here:  
📎 [Time_Series_Stock_Market_Report.pdf](./reports/Time_Series_Stock_Market_Report.pdf)

---

## 📌 Learning Outcomes

- Mastered time series forecasting techniques.
- Gained experience with real stock market data.
- Applied both classical and neural models for prediction.
- Built visualizations and dashboards to communicate insights.

---

## 👤 Author

**Manasvi Jindal**  
📧 manasvijindal57@gmail.com  
🔗 [LinkedIn]((https://www.linkedin.com/in/manasvi-jindal-03aa6a278/))  
🔗 [Link to the project ]((https://g71llzdl-8501.use2.devtunnels.ms/))  


