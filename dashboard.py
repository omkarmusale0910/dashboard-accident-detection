import numpy as np
import pandas as pd
import streamlit as st
from utils.get_data import get_us_accident,get_newyork_accident
from utils.map import us_map_data


US_accident_df=get_us_accident()
st.dataframe(US_accident_df)
st.write(list(US_accident_df.columns))
US_accident_df=US_accident_df[US_accident_df['State']=='OH']

us_accident_coorinate=us_map_data(US_accident_df)
st.dataframe(us_accident_coorinate)
st.map(us_accident_coorinate)

# print(df['LOCATION'].dtype)
# print(df.head(10))
# print(df.columns)
# st.markdown(df.columns)
# st.dataframe(df)
# df=df.dropna(subset=['LATITUDE','LONGITUDE','ZIP CODE'])
# df['ZIP CODE']=df['ZIP CODE'].astype(int)
# st.dataframe(df[['LATITUDE','LONGITUDE','ZIP CODE']])
# df['ZIP CODE'].dtype
# mask1=df['ZIP CODE']>=10001 
# mask2=df['ZIP CODE']<=10100
# # df=df[mask1 & mask2]
# st.dataframe(df[['LATITUDE','LONGITUDE','ZIP CODE']])
# map_df=df[['LATITUDE','LONGITUDE']]
# map_df['LATITUDE'].dtype
# st.map(map_df)


# df1=pd.read_csv('../dataset/US_Accidents_Dec21_updated.csv',nrows=10000)
# df1.info()
# df1=df1.rename(columns={'Start_Lat':'lat','Start_Lng':'lon'})
# st.map(df1[['lat','lon']])
