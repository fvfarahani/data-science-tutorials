# import the packages
import requests as rq
import bs4
import pandas as pd
import plotly.express as px

# read the web page into data
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
page = rq.get(url)

# read the page into bs4
bs4page = bs4.BeautifulSoup(page.text, 'html.parser')

# find the table in the page
tables = bs4page.find('table',{'class':"wikitable"})

# convert the tables to strings, then read it into pandas (grab a single-index header)
GDP = pd.read_html(str(tables), header=[1])[0]

# rename the header properly
GDP.columns=["Country","Region","IMF_Estimate","IMF_Year","UN_Estimate","UN_Year","WB_Estimate","WB_Year"]

# no need to have year's columns
GDP = GDP[['Country','Region', "IMF_Estimate", "UN_Estimate", "WB_Estimate"]]

# First stacked barplot -> based on IMF_Estimate
fig = px.bar(GDP, x="Region", y="IMF_Estimate", color="Country", barmode = 'stack')
fig.update_layout(title_text='IMF Estimate', title_x=0.5)
fig.show()

# Second stacked barplot -> based on UN_Estimate
fig = px.bar(GDP, x="Region", y="UN_Estimate", color="Country", barmode = 'stack')
fig.update_layout(title_text='United Nations Estimate', title_x=0.5)
fig.show()

# Third stacked barplot -> based on WB_Estimate
fig = px.bar(GDP, x="Region", y="WB_Estimate", color="Country", barmode = 'stack')
fig.update_layout(title_text='World Bank Estimate', title_x=0.5)
fig.show()