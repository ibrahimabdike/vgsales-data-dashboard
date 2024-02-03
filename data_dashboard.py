import streamlit as st
import pandas as pd
import plotly.express as px



# Read the dataset

@st.cache_data
def load_data():
    df = pd.read_csv('vgsales.csv')

    return df


data = load_data()


# Title and Introduction

st.title("Video Game Sales Dashboard")

st.write("Explore video game sales, ratings and platforms using this interactive dashboard")




if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(data)



platforms = data['Platform'].unique()

platform_filters = st.multiselect("Select Platform", platforms, default=platforms)

filtered_data = data[data['Platform'].isin(platform_filters)]


# Bar chart

st.subheader('Top N Games by Global Sales')

top_n = st.number_input("Select The Top N Games :", min_value=5, max_value=100, value=10, step=1)

top_games = filtered_data.nlargest(top_n, "Global_Sales")

fig = px.bar(top_games, x="Name", y="Global_Sales", color='Platform')
st.plotly_chart(fig)




st.subheader("Platform Market Share")
platform_share = filtered_data.groupby("Platform")["Global_Sales"].sum().reset_index()

fig2 = px.pie(platform_share, names='Platform', values='Global_Sales', title="Platform Market Share")
st.plotly_chart(fig2)



st.subheader("Year Vs Global Sales")

fig3 = px.scatter(filtered_data, x="Year", y= "Global_Sales", color="Platform", hover_name="Name", opacity=0.6)
st.plotly_chart(fig3)


