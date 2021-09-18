### Importing packages ###

import streamlit as st
import pandas as pd
import plotly.express as px
import os
import datetime as dt

### Defining global variables ###

ProductsDict = {'Mortgage': 1, 'Consumer loans': 2, 'Credit Card': 3, 'SME': 4, 'Student loans': 5, 'Auto loans': 6}
#Dir = r'C:\Users\Admin\Desktop\WEBAPPONE\data/'
Dir = 'https://raw.githubusercontent.com/Ashotm/WebappOne/tree/main/data/'

### Making Streamlit app layout and setting up app controls ###

st.set_page_config(layout='wide')
st.title('WebApp One')
#if i in [j.replace('.csv', '') for j in os.listdir(Dir)]:
st.write(os.listdir(Dir))
