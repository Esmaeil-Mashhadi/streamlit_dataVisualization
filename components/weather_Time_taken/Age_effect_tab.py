import streamlit as st
import pandas as pd 
import plotly.express as px 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np


@st.cache_data 
def Age_effect_tab() : 
    st.write('Here, we will explore how age affects delivery time, working hours, and ratings.')
    age_df = pd.read_csv('./data/visualizations_df/age_df.csv')
    st.subheader('Sample of Age Raw Data Frame')
    st.dataframe(age_df.sample(frac=.001))

    st.subheader("Let's see the number of employees within different age groups in this business.")
    Employees_df= age_df.drop_duplicates(subset='ID')
    Employees_df.replace("NaN " , np.nan , inplace=True)
    Employees_df.dropna(inplace=True)
    bins =[20 , 25 , 30 , 35, 40]
    labels= ['20-25' , '25-30' , '30-35' ,'35-40']
    Employees_df['age_group'] = pd.cut(Employees_df['Delivery_person_Age'] , bins=bins , labels=labels , right=False)
    Employees_count = Employees_df['age_group'].value_counts().reset_index().sort_values('age_group')
    fig = px.line(Employees_count , 'age_group' , 'count', markers='o')
    st.plotly_chart(fig)
    st.info(
    """ 
    Here, we can see that most of the employees in this business are around 
    the age of 30 to 40. Hiring individuals over 30 is more common in this 
    business, indicating that they value personal maturity and experience.
    """)


    st.subheader("Let's see if different age groups are more available during certain time periods.")
    frequent_age_df = age_df.groupby('time_periods')['Delivery_person_Age'].agg(lambda x: x.mode()[0]).reset_index()
    time_order = ['07:00-10:00', '10:00-13:00', '13:00-16:00', '16:00-19:00', '19:00-22:00', '22:00-23:59', '00:00-04:00']
    frequent_age_df['time_periods'] = pd.Categorical(frequent_age_df['time_periods'], categories=time_order , ordered=True)
    fig = px.bar(frequent_age_df , 'time_periods' , 'Delivery_person_Age')
    st.plotly_chart(fig)
    st.info(
        "Here, we can observe that younger individuals under 25 are more available during midnight or in the afternoons. "
        "In contrast, married individuals who are over 25 or 30 seem to be less available."
    )

    st.subheader('here we show the colaboration between age and rating')
    age_vs_rating_df = pd.DataFrame(age_df.groupby('Delivery_person_Age')['Delivery_person_Ratings'].mean()).reset_index()
    rate_age_fig = px.line(age_vs_rating_df , 'Delivery_person_Age' , 'Delivery_person_Ratings')
    st.plotly_chart(rate_age_fig) 
    

    st.subheader('now lets see how is age collaboration with delivery time')
    age_vs_timeTaken_df = pd.DataFrame(age_df.groupby('Delivery_person_Age')['Time_taken(min)'].mean()).reset_index()
    delivery_age_fig = px.line(age_vs_timeTaken_df , 'Delivery_person_Age' , 'Time_taken(min)')
    st.plotly_chart(delivery_age_fig)
    st.info(""" 
        It is evident that longer delivery times lead to decreased ratings. 
        Additionally, younger delivery personnel tend to be faster in their deliveries. 
        This speed contributes to their higher ratings, as they are able to deliver more efficiently.
    """)
    st.warning(""" 
      While ratings slightly decrease with age, it's important to consider
     the number of employees in each age group and other influencing factors.
    """)

    fig = plt.figure() 
    fig.set_facecolor(color='#455261')
    st.subheader('lets see the colaboration of ratings and time taken here')
    plt.gca().set_facecolor('#0E1117')
    sns.scatterplot(data=age_df, x='Time_taken(min)', y='Delivery_person_Ratings' , color='#8AD5FF' , edgecolor='#8AD5FF')
    st.pyplot(plt) 
    st.info(""" 
        The analysis reveals a clear negative correlation between rating and delivery time. 
        the longer it takes to deliver food , the chance of getting less rating increase
    """)
    
    st.subheader('lets see heatmap between time_taken , rating and age')
    age_df_group = pd.read_csv('./data/visualizations_df/age_df_group.csv')
    fig , ax = plt.subplots()
    fig.set_facecolor('#455261')
    pivot_table = age_df_group.pivot_table(values='Delivery_person_Ratings', index='Age_Group', columns='Time_Group')
    sns.heatmap(pivot_table , cmap='viridis').invert_yaxis()
    st.pyplot(fig)
    st.info("""
    This heatmap illustrates that while age is not a significant factor in delivery ratings, 
    the speed of delivery plays a crucial role. The data suggests that delivering food in under 
    30 minutes leads to higher customer satisfaction and happier customers.
    """)

  