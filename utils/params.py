import pandas as pd
import datetime as dt
from utils.get_data import get_unique_values_in_column,get_us_accident


filter_param_disable={'State':False,'County':True,'City':True,'Zipcode':True}
filter_severity_disable={'range':True,'block':False}
US_accident_df=get_us_accident(10000)
MIN_DATE=dt.date(2016,1,1)
MAX_DATE=dt.date(2020,12,31)
MIN_TIME=dt.time(0,0,0)
MAX_TIME=dt.time(23,59,59)
STATE_LIST=get_unique_values_in_column(US_accident_df,'State')
COUNTY_LIST=get_unique_values_in_column(US_accident_df,'County')
CITY_LIST=get_unique_values_in_column(US_accident_df,'City')
ZIPCODE_LIST=get_unique_values_in_column(US_accident_df,'Zipcode')
