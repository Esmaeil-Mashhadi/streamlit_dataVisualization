import streamlit as st
import pandas as pd 
import plotly.express as px 
import seaborn as sns 
import matplotlib.pyplot as plt 


@st.cache_data 
def Age_effect_tab() : 
    st.write('Here, we will explore how age affects delivery time, working hours, and ratings.')
    age_df = pd.read_csv('./data/visualizations_df/age_df.csv')
    st.subheader('Sample of Age Raw Data Frame')
    st.dataframe(age_df.sample(frac=.001))
    st.subheader('here we show the colaboration between age and rating')
    age_vs_rating_df = pd.DataFrame(age_df.groupby('Delivery_person_Age')['Delivery_person_Ratings'].mean()).reset_index()
    rate_age_fig = px.line(age_vs_rating_df , 'Delivery_person_Age' , 'Delivery_person_Ratings')
    st.plotly_chart(rate_age_fig) 
    
    st.info(""" 
        As observed, the ratings tend to decrease slightly with an increase in age. 
    """)

    st.subheader('now lets see how is age collaboration with delivery time')
    age_vs_timeTaken_df = pd.DataFrame(age_df.groupby('Delivery_person_Age')['Time_taken(min)'].mean()).reset_index()
    delivery_age_fig = px.line(age_vs_timeTaken_df , 'Delivery_person_Age' , 'Time_taken(min)')
    st.plotly_chart(delivery_age_fig)
    st.info(""" 
        It is evident that longer delivery times lead to decreased ratings. 
        Additionally, younger delivery personnel tend to be faster in their deliveries. 
        This speed contributes to their higher ratings, as they are able to deliver more efficiently.
    """)

    fig = plt.figure() 
    fig.set_facecolor(color='#455261')
    st.subheader('lets see the colaboration of ratings and time taken here')
    plt.gca().set_facecolor('#0E1117')
    sns.scatterplot(data=age_df, x='Time_taken(min)', y='Delivery_person_Ratings' , color='#8AD5FF' , edgecolor='#8AD5FF')
    st.pyplot(plt) 
    st.info(""" 
        The analysis reveals a clear negative correlation between age and delivery time. 
        This suggests that younger delivery personnel tend to achieve faster delivery times, 
        which is also associated with higher ratings. 
    """)
    

 