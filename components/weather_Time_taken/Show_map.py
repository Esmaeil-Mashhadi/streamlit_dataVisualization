import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib as plt 
import datetime
import folium 
from streamlit_folium import folium_static

st.cache_data
def show_map():
    st.write('raw data set sample')
    food_df = pd.read_csv('./data/clean_data.csv')
    st.info("""
             In this section, you can input a date to display travel map lines 
             based on the selected date.
    """)
    date_picked =st.date_input('pick a date', 
    value=datetime.date(2022 , 3, 1) ,
    min_value=datetime.date(2022, 3, 1),
    max_value=datetime.date(2022, 3, 31) 
    ) 
    food_df['Order_Date'] = pd.to_datetime(food_df['Order_Date'])
    filtered_df = food_df[food_df['Order_Date'].dt.date == date_picked]
    st.write(f'data frame  for {date_picked}')
    st.dataframe(filtered_df)

    st.title('delivery route map')

    map_center=  [filtered_df['Restaurant_latitude'].mean() , filtered_df['Restaurant_longitude'].mean()]
    delivery_map = folium.Map(location=map_center , zoom_start=5)
    st.info(f"For better performance, we have chosen to display the locations in batches of 10. However, you can still view the entire dataset for {date_picked} if needed.")


    current_value = st.slider('choose how many rows you want', 1, len(filtered_df) , 10)

    st.subheader(f'showing map for selected {current_value} rows')
    st.warning('zoom in to see draw line between customer and resturant')

    if st.toggle('view whole data map'):
        current_value = len(filtered_df)

    for index, row in filtered_df.iloc[:current_value].iterrows():  
        start_coords = (row['Restaurant_latitude'], row['Restaurant_longitude'])
        end_coords = (row['Delivery_location_latitude'] , row['Delivery_location_longitude'])

        folium.Marker(start_coords , popup='Resturant' , icon=folium.Icon(color='blue' , icon='cutlery')).add_to(delivery_map)
        folium.Marker(end_coords, popup='Client' ,icon=folium.Icon(color='red' , icon='home')).add_to(delivery_map)
        folium.PolyLine(locations=[start_coords , end_coords], color='blue').add_to(delivery_map)

    folium_static(delivery_map)



    
    

