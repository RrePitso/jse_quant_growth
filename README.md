# JSE Quant Growth Model 🚀

This project builds a data-driven stock-picking system for the Johannesburg Stock Exchange (JSE).
It focuses on identifying **small and mid-cap stocks** with **high growth potential**, using a combination
of **momentum**, **volatility**, and **fundamental indicators**.

## 💼 Stack
- **Colab** → development & model training  
- **GitHub Actions** → automation  
- **Streamlit** → visualization dashboard  

## ⚙️ Workflow
1. Collects JSE stock data daily via Yahoo Finance (`yfinance`)
2. Engineers growth & momentum features
3. Trains a LightGBM model to predict next-week returns
4. Updates predictions daily via GitHub Actions
5. Displays insights in Streamlit dashboard

## 🧠 Strategy
The model mimics a hybrid investor:
- Prefers **small tech** and **mining** stocks
- Seeks **fast-growing** yet **relatively stable** performers
- Balances short-term opportunity with long-term potential

## 🔮 Future Work
- Add fundamental & sentiment signals
- Deploy a REST API for prediction serving
- Add portfolio optimization & risk metrics
