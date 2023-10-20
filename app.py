import streamlit as st
import seaborn as sns
import sklearn as sk
import numpy as np
import seaborn as sns
sns.set_theme(style="darkgrid")

# Load an example dataset with long-form da



def main_page():
    st.title("Data Science for Marketing")


def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()