import streamlit as st
import pandas as pd 
import plotly.express as px 
import datetime
from components.weather_Time_taken.weather_effect_tab import weather_effects_tab
from components.weather_Time_taken.Traffic_effect_tab import Traffic_effect_tab
from components.weather_Time_taken.Age_effect_tab import Age_effect_tab


st.header('Exploring Food Delivery Insights through Interactive Data Visualizations')

def load_dataFrame():
    return pd.read_csv("./data/clean_data.csv")

food_df= load_dataFrame() 
 
def display_map(location_data):
    pass


st.sidebar.title('Options')  


if st.sidebar.toggle('show whole data set'): 
    st.dataframe(food_df)


if st.sidebar.toggle('Data Interaction Overview'):
    st.write('relation menu')
    tab1, tab2, tab3 = st.tabs(["Weather Effects", "Traffic Impact", "Age Correlations"])

    with tab1: 
        weather_effects_tab()

    with tab2:
        Traffic_effect_tab()

    with tab3:
       Age_effect_tab()

if st.sidebar.toggle('show map') :
       st.date_input('pick a date', 
       value=datetime.date(2022 , 3, 1) ,
       min_value=datetime.date(2022, 3, 1),
       max_value=datetime.date(2022, 3, 31) 
     )








