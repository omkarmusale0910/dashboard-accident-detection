import pandas as pd


def us_map_data(df:pd.DataFrame)->pd.DataFrame:
    map_df=df[['Start_Lat','Start_Lng']]
    map_df.rename(columns={'Start_Lat':'lat','Start_Lng':'lon'},inplace=True)
    print(map_df['lon'].dtype)
    return map_df


