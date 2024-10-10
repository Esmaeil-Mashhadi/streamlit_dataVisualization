import streamlit as st
import pandas as pd 
import plotly.express as px 
import seaborn as sns 
import matplotlib.pyplot as plt 

@st.cache_data
def Traffic_effect_tab(): 
    st.write('collaboration of trafic , time periods and ordercount')
    mean_trafic_df = pd.read_csv('./data/visualizations_df/mean_traffic_df.csv')
    traffic_df = pd.read_csv('./data/visualizations_df/traffic.csv')
    st.write('mean trafic data frame')
    st.dataframe(mean_trafic_df) 
    st.info('delivery time collaboration with trafic density ,as expceted lower trafic density makes delivery time faster')
    fig = px.bar(mean_trafic_df , x='Road_traffic_density' , y='Time_taken(min)')
    st.plotly_chart(fig)

    st.info("""
    let see how does vehicle type , collaborat with delivery time and trafic with heat map
    """)
    st.subheader("Traffic Density and Delivery Time Analysis")

    st.write('Traffic Data Frame Sample')
    st.dataframe(traffic_df.sample(frac=.001))

    st.write("Heatmap showing the relationship between bike type, traffic density, and delivery time.")
    order = ['Low', 'Medium', 'High', 'Jam'][::-1]
    traffic_df['Road_traffic_density'] = pd.Categorical(traffic_df['Road_traffic_density'], categories=order)

    heatmap_data = traffic_df.pivot_table(values='Time_taken(min)', index='Road_traffic_density', columns='Type_of_vehicle')
    fig, ax = plt.subplots()
    fig.set_facecolor(color='#455261')
    sns.heatmap(heatmap_data, cmap='viridis', ax=ax)
    st.pyplot(fig)

    st.info("""
    As observed, scooters and electric scooters perform better in higher traffic density situations, leading to improved delivery times. 
    By replacing motorcycles with scooters, we can potentially enhance delivery efficiency. 
    However, it is essential to consider other factors that may also impact delivery performance.
    """)

    st.subheader("Traffic and Order Density Analysis")


    order = ['Low' , "Medium" , 'High', "Jam"][::-1]
    time_trafic_df =pd.read_csv('./data/visualizations_df/time_traffic.csv')
    trafic_fig =px.line(time_trafic_df, x='time_periods' , y='Road_traffic_density' , markers=True  ,category_orders={'Road_traffic_density' : order} )
    traffic_df_order = pd.DataFrame(traffic_df['time_periods'].value_counts()).reset_index()
    order_fig = px.line(traffic_df_order  , x= 'time_periods' , y='count' , labels={'count' : 'total_orders'} )
    st.plotly_chart(trafic_fig) 
    st.plotly_chart(order_fig)
    st.info("""
    As we can see, there is a peak in traffic density between 19:00 and 22:00, which aligns with dinner time. 
    This period also sees the highest number of total orders.

    Additionally, around lunchtime, from 13:00 to 15:00, there is a significant increase in traffic, 
    and while the number of total orders is high, it is still lower than during the dinner period.
    """)

    st.subheader('lets see if trafic spread in month')

    date_df = pd.read_csv('./data/visualizations_df/date_df.csv')
    st.write('sample raw data')
    st.dataframe(date_df.sample(frac=.001))
    
    st.subheader('lets see total orders on each time period')
    
    count_df = date_df.groupby(['Order_Date_period', 'Road_traffic_density']).size().reset_index(name='count')
    pivot_df = pd.DataFrame(count_df.pivot_table(index='Order_Date_period', columns='Road_traffic_density', values='count')).reset_index()
    st.write('sample data frame')
    st.dataframe(pivot_df) 
    st.write('chart')
    fig =px.bar(pivot_df,
                x=['High', 'Jam', 'Low', 'Medium'],
                y='Order_Date_period' ,
                color_discrete_map={'High': 'orange', 'Jam': 'red', 'Low': 'green', 'Medium': 'blue'},  # Custom colors for categories
                orientation='h')
    st.plotly_chart(fig)
    st.info("""
    My understanding is that we have significantly high traffic congestion, 
    which affects delivery times. Bikes that perform better in heavy traffic 
    can help increase customer satisfaction.
    """)





    


