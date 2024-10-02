import streamlit as st
import pandas as pd 
import plotly.express as px 
import datetime


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
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Weather", "Vehicle", "Age-Date", "Date-Orders", "Festival"])

    with tab1:
        st.write("Weather effects on food delivery time")

    with tab2:
        st.write("Type of vehicle effects on delivery time")

    with tab3:
        st.write("Relation between age and date")

    with tab4:
        st.write("Date effect on the number of orders")

    with tab5:
        st.write("Age interest in festivals")







