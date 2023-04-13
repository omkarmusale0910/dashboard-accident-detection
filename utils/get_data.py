import pandas as pd
import numpy as np


NUMBER_OF_ROWS=10000

path_us_accident='/home/omkar/Desktop/Accedent_detection_dashboard/dataset/US_Accidents_Dec21_updated.csv'
path_newyork_accident='/home/omkar/Desktop/Accedent_detection_dashboard/dataset/Motor_Vehicle_Collisions_-_Crashes.csv'


def get_us_accident(rows:int=NUMBER_OF_ROWS)->pd.DataFrame:
    df=pd.read_csv(path_us_accident,nrows=rows)
    return df


def get_newyork_accident(rows:int=NUMBER_OF_ROWS)->pd.DataFrame:
    df=pd.read_csv(path_newyork_accident,nrows=rows)
    return df


