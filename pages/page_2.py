import pandas as pd
import streamlit as st
import seaborn as sns

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

a = sns.histplot(mall_data["Income"])
st.pyplot(a)