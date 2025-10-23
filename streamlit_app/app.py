import streamlit as st
import pandas as pd

st.title("📈 JSE Quant Growth Model Dashboard")
st.write("Model-predicted top-performing small-cap & growth stocks on the JSE")

df = pd.read_csv("../data/predictions/predictions_latest.csv")
st.dataframe(df)

top_stock = df.iloc[0]
st.metric("Top Pick", top_stock["Symbol"], f"{top_stock['Predicted_Return']:.2f}%")
st.line_chart(df.set_index("Symbol")["Predicted_Return"])
