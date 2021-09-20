### Importing packages ###

import streamlit as st
import pandas as pd
import plotly.express as px
import os
import datetime as dt

st.set_page_config(layout='wide')
### Defining global variables ###

ProductsDict = {'Mortgage': 1, 'Consumer loans': 2, 'Credit Card': 3, 'SME': 4, 'Student loans': 5, 'Auto loans': 6}
#Dir = r'C:\Users\Admin\Desktop\WEBAPPONE\data/'
#Dir = 'https://github.com/Ashotm/webappone/blob/master/data'

#print(os.path.abspath(__file__))
print(os.listdir("./app/webappone/data"))





