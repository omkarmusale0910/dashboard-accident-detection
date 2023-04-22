import numpy as np
import pandas as pd
import datetime as dt
import streamlit as st
import pydeck as pdk
from utils.map import us_map_data,deck_chart
from utils.params import MIN_DATE,MAX_DATE,MIN_TIME,MAX_TIME,STATE_LIST,COUNTY_LIST,COUNTY_LIST,CITY_LIST,ZIPCODE_LIST,filter_param_disable,filter_severity_disable,category_of_impact,USER_TIMEZONE
from utils.get_data import get_us_accident,get_newyork_accident,get_unique_values_in_column,get_max_value_columns,get_date_with_its_count_in_column
from utils.filter import filter_on_severity,filter_on_severity_low_mid_high,filter_on_column,filter_out_null_value_rows,filter_on_start_end_datetime
from utils.states import display_states
from dataprocess import process_input_data,process_input_date_and_time
from streamlit_extras.dataframe_explorer import dataframe_explorer


st.set_page_config(layout="wide", page_title="Dashboard")
US_accident_df=get_us_accident(200000)
US_accident_df=process_input_data(US_accident_df)



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
    input_start_date=st.date_input("**Enter the start date** :calendar:",value=MIN_DATE,min_value=MIN_DATE,max_value=MAX_DATE)
    input_start_time=st.time_input("**Select Start Time** :clock10:",value=MIN_TIME)
    input_end_date=st.date_input("**Select End date** :calendar:",value=dt.date(2020,1,1),min_value=MIN_DATE,max_value=MAX_DATE)
    input_end_time=st.time_input("**Select End Time** :clock10:",value=MAX_TIME)
    input_country=st.multiselect("**Select Country** :flag-lr:",options=['US'],default='US')
    input_filter=st.radio("**Select Filter**",options=[k for k,v in filter_param_disable.items()],key="selected_filter",on_change=OnChangeFilter,horizontal=True)
    input_state=st.multiselect("**Select States**",options=STATE_LIST,default={"CA":True},disabled=filter_param_disable['State'])
    input_county=st.multiselect("**Select County**",options=COUNTY_LIST,disabled=filter_param_disable['County'])
    input_city=st.multiselect("**Select cities**",options=CITY_LIST,disabled=filter_param_disable['City'])
    input_zipcode=st.multiselect("**Select Zipcode**",options=ZIPCODE_LIST,disabled=filter_param_disable['Zipcode'])
    input_severity_filter=st.radio("**Select Filter**",options=[k for k,v in filter_severity_disable.items()],key="severity_state",on_change=OnChangeSeverityFilter,horizontal=True)
    input_range_severity=st.slider("**Select Range of Severity**",min_value=2,max_value=4,value=(2,4),disabled=filter_severity_disable['Range'])
    input_block_severity=st.selectbox("**Select Severity**",options=category_of_impact,disabled=filter_severity_disable['Block'])
    

earliest=process_input_date_and_time(input_start_date,input_start_time,)
latest=process_input_date_and_time(input_end_date,input_end_time)



# apply input paramter to dataset for filtering 
# with start end datetime
US_accident_df=filter_on_start_end_datetime(US_accident_df,earliest,latest)

# with choosen paramter like [state,country,city]
if filter_param_disable['State']==False:
    US_accident_df=filter_on_column(US_accident_df,'State',input_state)
elif filter_param_disable['County']==False:
    US_accident_df=filter_on_column(US_accident_df,'County',input_county)
elif filter_param_disable['City']==False:
    US_accident_df=filter_on_column(US_accident_df,'City',input_city)
elif filter_param_disable['Zipcode']==False:
    US_accident_df=filter_on_column(US_accident_df,'Zipcode',input_zipcode)
else:
    print("No filter apply")


# filter based on severity
if filter_severity_disable['Range']==False:
     US_accident_df=filter_on_severity(US_accident_df,input_range_severity[0],input_range_severity[1])
elif filter_severity_disable['Block']==False:
    US_accident_df= filter_on_severity_low_mid_high(US_accident_df,input_block_severity)
else:
    print("No filtering on severity")




st.header("Dashboard")
# state content
display_states(US_accident_df)

us_accident_coorinate=us_map_data(US_accident_df)
st.map(us_accident_coorinate,use_container_width=True)

st.dataframe(dataframe_explorer(US_accident_df),use_container_width=True,height=500)
# st.write(list(US_accident_df.columns))


st.pydeck_chart(deck_chart(US_accident_df))


def send_data()->pd.DataFrame:
    return US_accident_df

