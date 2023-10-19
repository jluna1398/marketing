import pandas as pd
import streamlit as st
import seaborn as sns
import altair as alt
st.title(
    "Clustering Analysis"

)
# st.image('images/c.png')

mall_data = pd.read_csv('../data/Mall_Customers.csv')
mall_data.rename({'Annual Income (k$)':'Income', \
              'Spending Score (1-100)':'Spend_score'}, axis=1, \
             inplace=True)

st.write(mall_data.head())



a = alt.Chart(mall_data).mark_bar().encode(
    alt.X("Income", bin=True),
    y='count()'
)

st.altair_chart(a, use_container_width=True)

import plotly.express as px

df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.show()


# we can divided the gruops into 3 categories. By using age

# hypotesis is a therory of explanmation based on evidence that is not yet proved to be true