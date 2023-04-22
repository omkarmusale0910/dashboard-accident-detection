import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from dashboard import send_data


st.set_page_config(layout='wide')

df=send_data()

with st.sidebar:
    show_line_chart=st.checkbox(label="Line Chart",value=True)
    show_bar_chart=st.checkbox(label="Bar Chart",value=False)
    show_heat_map=st.checkbox("Heat Map",value=False)
    select_color=st.color_picker("**Choose Color For Plots**",value='#5252E2')
    select_col=st.multiselect(label="**Select param for Pie/Bar chart**",options=['State','County','City'],default={'City':True})
    select_types_of_chart=st.multiselect("**Select Type of Chart Pie/Bar**",options=['bar','pie'],default={'bar':True})
    select_num_of_unique_values=st.number_input("**Select Number of Top(cities/states/county)**",min_value=1, value=10)
# st.dataframe(df)

# format of chats
# header and fig

start_day=df['Start_Time'].min()
end_day=df['Start_Time'].max()

# tested
def get_number_of_acc_per_day_plot(df:pd.DataFrame)->go.Figure:
    daily_accidents=df.copy()
    daily_accidents["Start_Time"] = pd.to_datetime(daily_accidents["Start_Time"]).dt.tz_localize(None)
    daily_accidents = daily_accidents.groupby(pd.Grouper(key="Start_Time", freq="D")).size().reset_index(name="count")
    # daily_accidents=daily_accidents[['Start_Time','count']]
    bar=go.Figure()
    bar.add_trace(go.Bar(x=daily_accidents["Start_Time"],y=daily_accidents['count'],hovertext=daily_accidents['count']))
    bar.update_traces(marker_color=select_color)
    bar.update_layout(
        title="Accidents Count/Days Bar Chart",
        xaxis_title="Date",
        yaxis_title="Count",
        height=600)
    line=go.Figure()
    line.add_trace(go.Scatter(x=daily_accidents['Start_Time'],y=daily_accidents['count'],mode='lines+markers',name='lines+markers',marker_color=select_color,hovertext=daily_accidents['count']))

    line.update_layout(
        title="Accidents Count/Days Line Chart",
        xaxis_title="Date",
        yaxis_title="Count",
        height=600
    )

    heat_map = go.Figure(go.Histogram2d(
            x=daily_accidents['Start_Time'],
            y=daily_accidents['count'],
            colorscale=[[0, 'rgb(12,51,131)'], [0.25, 'rgb(10,136,186)'], [0.5, 'rgb(242,211,56)'], [0.75, 'rgb(242,143,56)'], [1, 'rgb(217,30,30)']]
        ))
    return line,bar,heat_map



def barplot(df:pd.DataFrame,column:str,num:int):
    key_value=df[column].value_counts()[:num]
    key=key_value.index
    value=key_value.values
    fig=go.Bar(x=key,y=value)
    return fig

def barplots(df:pd.DataFrame,coloum_list:list,num:int):
    for col in coloum_list:
        fig=go.Figure()
        fig.add_trace(barplot(df,col,num))
        fig.update_layout(
            title=f"{col} Bar Plot",
            xaxis_title=f"{col}",
            yaxis_title="Count",
            height=500)
        st.plotly_chart(fig,use_container_width=True)

        
def pieplot(df:pd.DataFrame,column:str,num:int):
    key_value=df[column].value_counts()[:num]
    key=key_value.index
    value=key_value.values
    fig=go.Pie(labels=key,values=value,textinfo='label+percent',
                             insidetextorientation='radial',hole=.3)
    
    return fig




def pieplots(df:pd.DataFrame,coloum_list:list,num:int):
    for col in coloum_list:
        fig=go.Figure(data=[pieplot(df,col,num)])
        fig.update_layout(title_text=f"{col} Pie Plot",)
        st.plotly_chart(fig,use_container_width=True)

        
    

if any([show_line_chart,show_bar_chart,show_heat_map]):st.header(f"**:violet[Accident Frequency over Time]**")
line_char,bar_chart,heat_map=get_number_of_acc_per_day_plot(df)
if show_line_chart: st.plotly_chart(line_char,use_container_width=True)
if show_bar_chart: st.plotly_chart(bar_chart,use_container_width=True)
if show_heat_map:st.plotly_chart(heat_map,use_container_width=True)

if 'bar' in select_types_of_chart : barplots(df,select_col,select_num_of_unique_values)
if 'pie' in select_types_of_chart: pieplots(df,select_col,select_num_of_unique_values)






