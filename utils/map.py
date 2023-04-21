import pandas as pd
from geopy.distance import distance, Point
import pydeck as pdk
import streamlit as st
# tested
def us_map_data(df:pd.DataFrame)->pd.DataFrame:
    map_df=df[['lat','lon']]
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


def deck_chart(df:pd.DataFrame)->pdk.Deck:
    us_accident_coorinate=df[['lat','lon']]
    return pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=10,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
            'HexagonLayer',
            data=us_accident_coorinate,
            get_position='[lon, lat]',
            radius=300,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=us_accident_coorinate,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    )




# if __name__ == "__main__":
#     lat1,lon1=16.740485,74.365020 # atigre
#     lat2,lon2=16.742003, 74.349219 # chokak
#     print(get_distance_between_geo_coordinate(lat1,lon1,lat2,lon2,False)) # in km 