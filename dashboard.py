import numpy as np
import pandas as pd
import datetime as dt
import streamlit as st
from utils.map import us_map_data
from utils.params import MIN_DATE,MAX_DATE,MIN_TIME,MAX_TIME,STATE_LIST,COUNTY_LIST,COUNTY_LIST,CITY_LIST,ZIPCODE_LIST,filter_param_disable,filter_severity_disable
from utils.get_data import get_us_accident,get_newyork_accident,get_unique_values_in_column,get_max_value_columns,get_date_with_its_count_in_column
from utils.filter import filter_on_severity,filter_on_severity_low_mid_high,filter_on_column,filter_out_null_value_rows


US_accident_df=get_us_accident(20000)
US_accident_df.info()

# MIN_DATE=dt.date(2016,1,1)
# MAX_DATE=dt.date(2020,12,31)
# MIN_TIME=dt.time(0,0,0)
# MAX_TIME=dt.time(23,59,59)
# STATE_LIST=get_unique_values_in_column(US_accident_df,'State')
# COUNTY_LIST=get_unique_values_in_column(US_accident_df,'County')
# CITY_LIST=get_unique_values_in_column(US_accident_df,'City')
# ZIPCODE_LIST=get_date_with_its_count_in_column(US_accident_df,'Zipcode')


# tested
def OnChangeFilter():
    for k in filter_param_disable.keys():
        filter_param_disable[k]=True
    filter_param_disable[st.session_state.selected_filter]=False
    # print(st.session_state.selected_filter)


def OnChangeSeverityFilter():
    for k in filter_severity_disable.keys():
        filter_severity_disable[k]=True
    filter_severity_disable[st.session_state.severity_state]=False

# input
with st.sidebar:
    input_start_date=st.date_input("**Enter the start date** :calendar:",value=dt.date(2019,1,1),min_value=MIN_DATE,max_value=MAX_DATE)
    input_start_time=st.time_input("**Select Start Time** :clock10:",value=MIN_TIME)
    input_end_date=st.date_input("**Select End date** :calendar:",value=dt.date(2020,1,1),min_value=MIN_DATE,max_value=MAX_DATE)
    input_end_time=st.time_input("**Select End Time** :clock10:",value=MAX_TIME)
    input_country=st.multiselect("**Select Country** :flag-lr:",options=['US'],default='US')
    input_filter=st.radio("**Select Filter**",options=[k for k,v in filter_param_disable.items()],key="selected_filter",on_change=OnChangeFilter,horizontal=True)
    input_state=st.multiselect("**Select States**",options=STATE_LIST,default={"OH":True},disabled=filter_param_disable['State'])
    input_county=st.multiselect("**Select County**",options=COUNTY_LIST,disabled=filter_param_disable['County'])
    input_city=st.multiselect("**Select cities**",options=CITY_LIST,disabled=filter_param_disable['City'])
    input_zipcode=st.multiselect("**Select Zipcode**",options=ZIPCODE_LIST,disabled=filter_param_disable['Zipcode'])
    input_severity_filter=st.radio("**Select Filter**",options=[k for k,v in filter_severity_disable.items()],key="severity_state",on_change=OnChangeSeverityFilter,horizontal=True)
    





st.write(US_accident_df.shape)
st.dataframe(US_accident_df)
US_accident_df=filter_on_column(US_accident_df,'State',['CA'])
st.dataframe(US_accident_df)
# st.dataframe(US_accident_df.info())
st.write(list(US_accident_df.columns))

st.write(get_unique_values_in_column(US_accident_df,'Street'))
st.write(get_max_value_columns(US_accident_df,'State'))

# US_accident_df=filter_on_state(US_accident_df,"OH")
us_accident_coorinate=us_map_data(US_accident_df)
# st.dataframe(us_accident_coorinate.info())
# st.dataframe(us_accident_coorinate)
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


# st.snow()