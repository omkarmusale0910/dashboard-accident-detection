import pandas as pd
import streamlit as st


state_columns=['Temperature(F)','Humidity(%)','Wind_Speed(mph)']
state_params=['min','max','mean','std','25%','75%']
weather_params=['Clear','Cloudy','Rain','Snow','Fog']

def get_states(df:pd.DataFrame):
    state_df=df.describe()
    states={}
    for column in state_columns:
        column_state={}
        for param in state_params:
            column_state[param]=state_df[column][param]
        else:
            states[column]=column_state
    return states


def get_weather_condition_state(df:pd.DataFrame):
    weatherType_value=df['Weather_Condition'].value_counts()
    weather_ct={}
    total=0
    for wp in weather_params:
        sum=0
        for item in weatherType_value.iteritems():
            if wp in item[0]:
                sum+=item[1]
        else:
            weather_ct[wp]=sum
            total+=sum
    weather_per={}
    for k,v in weather_ct.items():
        weather_per[k]=(v/total)*100
    return weather_per


def get_day_night_state(df:pd.DataFrame):
    days_acc=df['Sunrise_Sunset'].value_counts()['Day']
    night_acc=df['Sunrise_Sunset'].value_counts()['Night']
    total_acc=days_acc+night_acc
    days_acc_per=(days_acc/total_acc)*100
    night_acc_per=(night_acc/total_acc)*100
    return {'Day':days_acc_per,'Night':night_acc_per}


def get_state_page_info(df:pd.DataFrame):
    start_day=df['Start_Time'].min()
    last_day=df['Start_Time'].max()
    weather_param_states=get_states(df)
    weather_condition_state=get_weather_condition_state(df)
    day_night_state=get_day_night_state(df)
    return start_day,last_day,weather_param_states,weather_condition_state,day_night_state

def diplay_col(col,param,thw_state):
    col.write(f"**:violet[{param}]**")
    c1,c2,c3=col.columns(3)
    c1.write(":blue[MIN]")
    c1.write(f"{thw_state[param]['min']}")
    c2.write(":blue[MAX]")
    c2.write(f"{thw_state[param]['max']}")
    c3.write(":blue[AVG]")
    c3.write(f"{thw_state[param]['mean']:0.2f}")

def display_dn(col,obj):
    col.subheader("**:violet[Road Accident D/N]**")
    c1,c2=col.columns(2)
    c1.write(f"**:violet[Day]**")
    c1.write(f"**:violet[{obj['Day']:0.2f}]%**")
    c2.write(f"**:violet[Night]**")
    c2.write(f"**:violet[{obj['Night']:0.2f}]%**")

def diplay_ws(col,obj:dict):
    col.subheader("**:violet[Weather States]**")
    list_col=col.columns(len(weather_params))
    ct=0
    for k,v in obj.items():
        list_col[ct].write(f"**:violet[{k}]**")
        list_col[ct].write(f"**:violet[{v:0.2f}]%**")
        ct+=1

def display_states(df:pd.DataFrame):
    sd,ld,thw_state,wc_state,dn_state=get_state_page_info(df)
    with st.container():
        st.subheader("**Statistical Report on Accidents**")
        st.write("**:violet[Accident data Time Range]**")
        st.write(sd,ld)
        col1,col2,col3=st.columns(3)
        diplay_col(col1,'Temperature(F)',thw_state)
        diplay_col(col2,'Humidity(%)',thw_state)
        diplay_col(col3,'Wind_Speed(mph)',thw_state)
        st.markdown("---")
        col1,col2=st.columns(2)
        display_dn(col1,dn_state)
        diplay_ws(col2,wc_state)
        st.markdown("---")





