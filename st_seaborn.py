import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Iris Data Visualization')
iris = sns.load_dataset('iris')
print(iris.head())
print(iris.columns)
x = st.selectbox('x ', iris.columns)
y = st.selectbox('y ', iris.columns)
fig = sns.jointplot(x=x, y=y, data=iris) 

st.pyplot(fig)