import streamlit as st
import pandas as pd 
import plotly.express as px 

@st.cache_data
def weather_effects_tab():
        st.write("Weather effects on food delivery time")
        weather_df=pd.read_csv('./data/visualizations_df/weather_timeTaken.csv')
        st.dataframe(weather_df)
        fig = px.bar(weather_df ,
                      x='Time_taken(min)', y='Weatherconditions',
                      text='total_orders', color_continuous_scale='teal' , color='Time_taken(min)', orientation='h')
        st.plotly_chart(fig)
        st.info("the correlation between weather conditions and total orders")
        fig = px.bar(weather_df ,x='total_orders',  y='Time_taken(min)' ,
                     color_continuous_scale='teal' , color='Weatherconditions' )
        st.plotly_chart(fig)
             

        with st.expander('Read my understanding of the chart'): 
                st.write("""
                    This chart illustrates how various weather conditions affect the time taken for food deliveries. 
                    It also shows the total number of orders placed under each weather condition. 
                    Understanding these factors can help in optimizing delivery times and improving customer satisfaction. 

                    Here are my takeaways from the chart:
                    1. **Sunny** weather has the shortest average delivery time of **22.14 minutes**, indicating efficient conditions for deliveries.
                    2. In contrast, **Cloudy** and **Fog** conditions lead to longer delivery times of **29.14** and **29.17 minutes**, respectively.
                    4. There is a notable correlation: as the **total orders** increase, the time taken for deliveries tends to increase as well.
                    5. The highest number of orders (**7116**) occurred during **Cloudy** weather, suggesting that this condition is favorable for customers to place orders.
                    7. The data implies that increased order volume during bad weather may lead to significant delays.
                """)
                st.warning("""Adverse weather conditions, such as **Sandstorms** and **Stormy** weather, result in increased delivery times of **26.11 minutes**. 
                               This is quite unusual, as these times are lower than those for **Cloudy** and **Foggy** conditions. 
                               One contributing factor may be the total number of orders, but we should also consider other influencing factors.
                """)