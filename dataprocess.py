import pandas as pd
import datetime as dt
import pytz
import streamlit as st


start_day=st.date_input('Start day')
start_time=st.time_input("enter start time")
end_day=st.date_input('end day')
end_time=st.time_input("enter end time")


def process_input_date_and_time(input_date,input_time,timezone:str='US/Eastern',is_convert_to_utc:bool=False):
    input_date_time=dt.datetime.combine(date=input_date,time=input_time)
    tz=pytz.timezone(timezone)
    input_date_time_with_tz=tz.localize(input_date_time)
    if is_convert_to_utc:
        input_date_time_with_tz=input_date_time_with_tz.astimezone(pytz.utc)
    return input_date_time_with_tz
    
def process_input_data(df:pd.DataFrame):
    df['Start_time']=pd.to_datetime(df['Start_time'])
    df['End_time']=pd.to_datetime(df['End_time'])
    return df

start=process_input_date_and_time(start_day,start_time,is_convert_to_utc=True)
st.write(start)

