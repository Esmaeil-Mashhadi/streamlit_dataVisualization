import streamlit as st
from components.weather_Time_taken.weather_effect_tab import weather_effects_tab
from components.weather_Time_taken.Traffic_effect_tab import Traffic_effect_tab
from components.weather_Time_taken.Age_effect_tab import Age_effect_tab
from components.weather_Time_taken.Show_map import show_map
from streamlit_navigation_bar import st_navbar



page = st_navbar(["Data Analytics Overview", "Geospatial Map", "AI Predictions", "Source Code & Contact"])


if page == 'Data Analytics Overview' : 
    st.subheader('Data Analytics Overview') 

    tab1, tab2, tab3 = st.tabs(["Weather Effects", "Traffic Impact", "Age Correlations"])    
    with tab1: 
        weather_effects_tab()

    with tab2:
        Traffic_effect_tab()

    with tab3:
       Age_effect_tab()


if  page == 'Geospatial Map': 
    show_map() 
      
if page =="AI Predictions": 
    st.info('comming soon')

import streamlit as st

if page == 'Source Code & Contact':
    st.subheader("Source Code & Contact Information")

    st.write("Here are the relevant links to my projects and profiles:")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button('GitHub Profile'):
            st.write('[My GitHub Profile](https://github.com/Esmaeil-mashhadi)')

    with col2:
        if st.button('Jupyter Notebook'):
            st.write('[Data Cleaning Source](https://github.com/Esmaeil-Mashhadi/streamlit_dataVisualization/blob/main/dataCleaning.ipynb)')

    with col3:
        if st.button('Streamlit Source'):
            st.write('[Streamlit Source Code](https://github.com/Esmaeil-Mashhadi/streamlit_dataVisualization/blob/main/main.py)')

    with col4: 
        if st.button('phone & email'): 
            st.write('+989136038055')
            st.write('codealchemy.esi@gmail.com')








