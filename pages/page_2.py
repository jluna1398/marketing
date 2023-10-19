import pandas as pd
import streamlit as st
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt
from math import pi
st.title(
    "Clustering Analysis"

)
# st.image('images/c.png')

# mall_data = pd.read_csv('data/Mall_Customers.csv')
# mall_data.rename({'Annual Income (k$)':'Income', \
#               'Spending Score (1-100)':'Spend_score'}, axis=1, \
#              inplace=True)
#
# st.write(mall_data.head())
#
#
#
# a = alt.Chart(mall_data).mark_bar().encode(
#     alt.X("Income", bin=True),
#     y='count()'
# )

# st.altair_chart(a, use_container_width=True)






# we can divided the gruops into 3 categories. By using age

# hypotesis is a therory of explanmation based on evidence that is not yet proved to be true





# Set data
df = pd.DataFrame({
    'group': ['A','B','C','D'],
    'var1': [38, 1.5, 30, 4],
    'var2': [29, 10, 9, 34],
    'var3': [8, 39, 23, 24],
    'var4': [7, 31, 33, 14],
    'var5': [28, 15, 32, 14]
})

# number of variable
categories=list(df)[1:]
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories, color='grey', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,40)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

# Fill area
ax.fill(angles, values, 'b', alpha=0.1)

# Show the graph
st.pyplot(ax)