import mysql.connector
import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title = 'Dashboard of employees and clients')
st.title('Dashboard of employees and clients')

YY = px.bar([1,2,2,3,3,4,4,4,4,4,44],
title = '<b>Sex</b>')
st.plotly_chart(YY)


