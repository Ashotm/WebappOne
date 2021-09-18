### Importing packages ###

import streamlit as st
import pandas as pd
import plotly.express as px
import os
import datetime as dt
import requests

### Defining global variables ###

ProductsDict = {'Mortgage': 1, 'Consumer loans': 2, 'Credit Card': 3, 'SME': 4, 'Student loans': 5, 'Auto loans': 6}
#Dir = r'C:\Users\Admin\Desktop\WEBAPPONE\data/'
#Dir = 'https://api.github.com/Ashotm/WebappOne/tree/main/data/'

user = "Ashotm"
repo = "WebappOne"

url = "https://api.github.com/repos/Ashotm/WebappOne/git/trees/master?recursive=1".format(user, repo)
r = requests.get(url)
res = r.json()

for file in res["tree"]:
    st.write((file["path"])


### Making Streamlit app layout and setting up app controls ###

st.set_page_config(layout='wide')
st.title('WebApp One')
#if i in [j.replace('.csv', '') for j in os.listdir(Dir)]:
st.write(os.listdir(Dir))
