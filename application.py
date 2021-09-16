### Importing packages ###

import streamlit as st
import pandas as pd
import plotly.express as px
import os
import datetime as dt

### Defining global variables ###

ProductsDict = {'Mortgage': 1, 'Consumer loans': 2, 'Credit Card': 3, 'SME': 4, 'Student loans': 5, 'Auto loans': 6}
#Dir = r'C:\Users\Admin\Desktop\WEBAPPONE\data/'
Dir = r'https://github.com/Ashotm/WebappOne/tree/main/data/'

### Making Streamlit app layout and setting up app controls ###

st.set_page_config(layout='wide')
st.title('WebApp One')

Sidebar = st.sidebar.header('Settings')
RadioButton = Sidebar.radio(label = 'Breakdown', options = ['Products'])
EndDate = st.sidebar.date_input('Date', min_value = dt.datetime(2020,12,31), max_value = dt.datetime(2021,12,31))
Window = st.sidebar.slider('Time horizon, months', min_value = 1, max_value = 6)

ProdSelect = st.sidebar.multiselect(label = 'Products', options = ProductsDict.keys(), default = list(ProductsDict)[0])

### Defining time horizon for the analysis ###

TimeHorizon = []
for i in range(Window):
    EoPreMonth = ((dt.datetime(EndDate.year, EndDate.month, 1) - dt.timedelta(days = 1)).date())
    TimeHorizon.append(EoPreMonth)
    EndDate = EoPreMonth

TimeHorizon = sorted(TimeHorizon)
TimeHorizon = [i.strftime("%d.%m.%y") for i in TimeHorizon]

### Creating list later to be used in DataFrame ###

PortfolioTempLst, PortfolioLst, OverduePortfolioTempLst, \
    OverduePortfolioLst, OverdueRatioTempLst, OverdueRatioLst = ([] for i in range(6))

### Reading .csv files into dataframes ###

for i in TimeHorizon:
    if i in [j.replace('.csv', '') for j in os.listdir(Dir)]:
        vars()['df'+i] = pd.read_csv(Dir+i+'.csv', index_col = False)
        vars()['df'+i]['Maxoverdue'] = vars()['df'+i][['Principal overdue', 'Interest overdue']].max(axis = 1)

        for v in ProductsDict.values():
            OverduePortfolio = vars()['df'+i].loc[(vars()['df'+i]['Maxoverdue'] > 0) & (vars()['df'+i]['Loan_type'] == v), 'Amount'].sum()
            Portfolio = vars()['df'+i].loc[(vars()['df'+i]['Loan_type'] == v), 'Amount'].sum()
            OverdueRatio = OverduePortfolio/Portfolio

            PortfolioTempLst.append(Portfolio)
            OverduePortfolioTempLst.append(OverduePortfolio)
            OverdueRatioTempLst.append(OverdueRatio)

        PortfolioLst.append(PortfolioTempLst)
        OverduePortfolioLst.append(OverduePortfolioTempLst)
        OverdueRatioLst.append(OverdueRatioTempLst)

        PortfolioTempLst = []
        OverduePortfolioTempLst = []
        OverdueRatioTempLst = []

Portfoliodf = pd.DataFrame(PortfolioLst, columns = ProductsDict.keys(),  index = TimeHorizon)
OverduePortfoliodf = pd.DataFrame(OverduePortfolioLst, columns = ProductsDict.keys(),  index = TimeHorizon)
OverdueRatioLst = pd.DataFrame(OverdueRatioLst, columns = ProductsDict.keys(),  index = TimeHorizon)

### Creating line charts with Plotly ###

c1, c2, c3 = st.columns(3)
with c1, c2, c3:
    c1.subheader('Total portfolio')
    c1.plotly_chart(px.line(Portfoliodf.loc[TimeHorizon][ProdSelect]).update_traces(mode = 'lines+markers'), template = 'ggplot2', use_container_width = True)
    c2.subheader('Overdue portfolio')
    c2.plotly_chart(px.line(OverduePortfoliodf.loc[TimeHorizon][ProdSelect]).update_traces(mode = 'lines+markers'), template = 'ggplot2', use_container_width = True)
    c3.subheader('Overdue ratio')
    c3.plotly_chart(px.line(OverdueRatioLst.loc[TimeHorizon][ProdSelect]).update_traces(mode = 'lines+markers'), template = 'ggplot2', use_container_width = True)

### Creating containers with dataframes ###

st.subheader('The Data')

c4, c5, c6 = st.columns(3)
with c4, c5, c6:
    c4.expander('Mortgage').dataframe(Portfoliodf['Mortgage'])
    c5.expander('Consumer loans').dataframe(Portfoliodf['Consumer loans'].T)
    c6.expander('Credit Card').dataframe(Portfoliodf['Credit Card'].T)

c7, c8, c9 = st.columns(3)
with c7, c8, c9:
    c7.expander('SME').dataframe(Portfoliodf['SME'])
    c8.expander('Student loans').dataframe(Portfoliodf['Student loans'].T)
    c9.expander('Auto loans').dataframe(Portfoliodf['Auto loans'].T)
