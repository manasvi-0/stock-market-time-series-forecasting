
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
├── data/                              
|-─Time_series.ipynb
├── visuals/              
├── Stock-Market/                   
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
| ARIMA   | 4.68   | 1.84%  | Baseline model      |
| SARIMA  | 4.68   | 1.84   | Seasonal adjustment |
| Prophet | 10.1   | 3.0%   | Auto trend capture  |
| LSTM    | 6.37   | 2.59%  | Best performance    |

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
🔗 [LinkedIn](https://www.linkedin.com/in/manasvi-jindal-03aa6a278/)  
🚀 [Project Link](https://g71llzdl-8501.use2.devtunnels.ms/)



