import pandas as pd
import streamlit as st
import seaborn as sns
import altair as alt
st.title(
    "Clustering Analysis"

)
st.image('images/c.png')

mall_data = pd.read_csv('data/Mall_Customers.csv')
mall_data.rename({'Annual Income (k$)':'Income', \
              'Spending Score (1-100)':'Spend_score'}, axis=1, \
             inplace=True)

st.write("""

#### Data Exploration
""")

st.dataframe(mall_data.head())

a = alt.Chart(mall_data).mark_bar().encode(
    alt.X("Income", bin=True),
    y='count()'
)

st.altair_chart(a)