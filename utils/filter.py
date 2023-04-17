import pandas as pd

# tested
def filter_on_severity(df:pd.DataFrame,low:int=1,high:int=4):
    mask1=df['Severity']>=low
    mask2=df['Severity']<=high
    df=df[mask1 & mask2]
    return df


# tested in our data severity==1 no data point present may be
def filter_on_severity_low_mid_high(df:pd.DataFrame,severity:str='high')->pd.DataFrame:
    category_of_impact=['low','mid','high']
    if(severity in category_of_impact):
        if(severity==category_of_impact[0]):
            mask=df['Severity']<=1
            df=df[mask]
        elif(severity==category_of_impact[1]):
            mask1=df['Severity']>=2
            mask2=df['Severity']<=3
            df=df[mask1 & mask2]
        else:
            mask=df['Severity']==4
            df=df[mask]
        return df
    else:
        print("input value as severity is not valid")
        return df
    

def filter_on_column(df:pd.DataFrame,column_name:str,value_list:list)->pd.DataFrame:
    mask=df[column_name].isin(value_list)
    df=df[mask]
    return df


def filter_out_null_value_rows(df:pd.DataFrame,list_columns:list)->pd.DataFrame:
    df=df.dropna(subset=list_columns,how=any)
    return df


def filter_on_start_end_datetime(df:pd.DataFrame,start_dt,end_dt)->pd.DataFrame:
    pass
















'''
def filter_on_country(df:pd.DataFrame,country_name:str)->pd.DataFrame:
    mask=df['Country']==country_name
    df=df[mask]
    return df

def filter_on_state(df:pd.DataFrame,state_name:str)->pd.DataFrame:
    mask=df['State']==state_name
    df=df[mask]
    return df

def filter_on_county(df:pd.DataFrame,county_name:str)->pd.DataFrame:
    mask=df['County']==county_name
    df=df[mask]
    return df

def filter_on_zipcodes(df:pd.DataFrame,zipscode_list:list)->pd.DataFrame:
    mask=df['Zipcode'].isin(zipscode_list)
    df=df[mask]
    return df

'''