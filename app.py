import streamlit as st
import seaborn as sns
import sklearn as sk
import numpy as np
st.title("Jose Luna")
import seaborn as sns
sns.set_theme(style="darkgrid")

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
st.dataframe(
    fmri.head())
