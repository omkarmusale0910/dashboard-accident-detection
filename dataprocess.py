import pandas as pd
import datetime as dt
import pytz
from utils.params import DROP_NULL_VALUE_COL


# tested 
def process_input_date_and_time(input_date,input_time):
    input_date_time=dt.datetime.combine(date=input_date,time=input_time,tzinfo=pytz.utc)
    return input_date_time
    


# not conrrect 
def process_input_data(df:pd.DataFrame):
    df.dropna(subset=DROP_NULL_VALUE_COL,how='any',inplace=True)
    df_copy=df.copy()

    df_copy['Start_Time']=pd.to_datetime(df_copy['Start_Time'],utc=True)
    df_copy['End_Time']=pd.to_datetime(df_copy['End_Time'],utc=True)

    # sorting on based Start_Time
    df_copy.sort_values(by=['Start_Time'],ascending=True,inplace=True)

    # conerting column names for 
    df_copy.rename(columns={'Start_Lat':'lat','Start_Lng':'lon'},inplace=True)
    return df_copy


