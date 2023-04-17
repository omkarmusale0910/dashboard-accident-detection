import pandas as pd
import numpy as np
import streamlit as st


NUMBER_OF_ROWS=10000

path_us_accident='/home/omkar/Desktop/Accedent_detection_dashboard/dataset/US_Accidents_Dec21_updated.csv'
path_newyork_accident='/home/omkar/Desktop/Accedent_detection_dashboard/dataset/Motor_Vehicle_Collisions_-_Crashes.csv'

# tested
@st.cache_data
def get_us_accident(rows:int=NUMBER_OF_ROWS)->pd.DataFrame:
    df=pd.read_csv(path_us_accident,nrows=rows)
    return df


@st.cache_data
def get_newyork_accident(rows:int=NUMBER_OF_ROWS)->pd.DataFrame:
    df=pd.read_csv(path_newyork_accident,nrows=rows)
    return df

# tested
@st.cache_data
def get_unique_values_in_column(df:pd.DataFrame,column:str,is_sort:bool=True)->pd.DataFrame:
    unique_value=df.drop_duplicates(subset=[column])[column]
    unique_value=list(unique_value.values)
    try:
        if is_sort:
            unique_value=sorted(unique_value)
    except:
        # raise Exception(f"Error come during Sorting of {column}")
        print("Error accore during sorting")
    return unique_value

# tested
@st.cache_data
def get_max_value_columns(df:pd.DataFrame,column:str):
    series=df.groupby(column).size()
    series= series.sort_values(ascending=False)
    return str(series.index[0])

# tested 
@st.cache_data
def get_date_with_its_count_in_column(df:pd.DataFrame,column:str,is_asending:bool=None):
    dict_value_to_count={}
    series=df.groupby(column).size()
    if is_asending is not None:
        series=series.sort_values(ascending=is_asending)
    index=series.index
    dict_value_to_count={id:series[id] for id in index}
    return dict_value_to_count
    