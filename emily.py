import pandas as pd
import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
from plotly.offline import iplot
import plotly.express as px
import plotly.graph_objects as go

st.title('Streamlit assignment')
st.header(' Emily El Hajj')
st.write('Click in box to view dataset')
df = pd.read_csv(r'C:\Users\LENOVO\Desktop\country_vaccinations.csv')
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.subheader('Number of Vaccinations taken per day from December 12,2020 till February 13, 2021 all around the world')

vis = px.choropleth(df,locations ='iso_code',color='total_vaccinations',animation_frame='date',
             color_continuous_scale=px.colors.sequential.Plasma, projection='natural earth')
st.write(vis)

st.write('Click in box to view dataset')
df1 = pd.read_csv(r'C:\Users\LENOVO\Desktop\Covid19-Data.csv')
if st.checkbox('Show raw data1'):
    st.subheader('Raw data')
    st.write(df1)
st.subheader('Covid 19 cases in each continent from February 25,2020 till January 2, 2021')
vis1 = px.bar(df1, x="Continent", y="Cases", color="Continent",
  animation_frame="Date", animation_group="Entity", log_y=True)
st.write(vis1)
