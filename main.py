import streamlit as st
import pandas as pd 
import plotly.express as px 
import datetime
from components.weather_Time_taken.weather_effect_tab import weather_effects_tab
from components.weather_Time_taken.Traffic_effect_tab import Traffic_effect_tab
from components.weather_Time_taken.Age_effect_tab import Age_effect_tab


st.header('Exploring Food Delivery Insights through Interactive Data Visualizations')

@st.cache_data
def load_dataFrame():
    return pd.read_csv("./data/clean_data.csv")

food_df= load_dataFrame()

def display_map(location_data):
    pass


st.sidebar.title('Options')  


if st.sidebar.toggle('show whole data set'): 
    st.dataframe(food_df)



if st.sidebar.toggle('show map') :
       st.date_input('pick a date', 
       value=datetime.date(2022 , 3, 1) ,
       min_value=datetime.date(2022, 3, 1),
       max_value=datetime.date(2022, 3, 31) 
     )
    

if st.sidebar.toggle('check'): 
    st.write(food_df['Order_Date'].min())
    st.write(food_df['Order_Date'].max())
    start_date = '01-03-2022'
    end_date = '01-03-2022'
    filted_data =st.dataframe(food_df.loc[(food_df['Order_Date']>= start_date) & (food_df['Order_Date']<= end_date)])

if st.sidebar.toggle('Data Set Relations'):
    st.write('relation menu')
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Weather", "Traffic", "Age", "Date", "Festival"])

    with tab1:
        weather_effects_tab()

    with tab2:
        Traffic_effect_tab()

    with tab3:
       Age_effect_tab()

    with tab4:
        st.write("Date effect on the number of orders")

    with tab5:
        st.write("Age interest in festivals")






