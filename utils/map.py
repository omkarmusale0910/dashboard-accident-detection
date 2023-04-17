import pandas as pd
from geopy.distance import distance, Point

# tested
def us_map_data(df:pd.DataFrame)->pd.DataFrame:
    map_df=df[['Start_Lat','Start_Lng']]
    map_df=map_df.rename(columns={'Start_Lat':'lat','Start_Lng':'lon'})
    return map_df

# tesred
def get_distance_between_geo_coordinate(lat1,lon1,lat2,lon2,is_meter:bool=True):
    point1=Point(lat1,lon1)
    point2=Point(lat2,lon2)

    dist_between_points=distance(point1,point2).meters
    # convert to km
    if not(is_meter):
        dist_between_points=dist_between_points/1000.0
    return dist_between_points






if __name__ == "__main__":
    lat1,lon1=16.740485,74.365020 # atigre
    lat2,lon2=16.742003, 74.349219 # chokak
    print(get_distance_between_geo_coordinate(lat1,lon1,lat2,lon2,False)) # in km 