import gzip
import math
import string
from collections import defaultdict
import numpy as np
import pandas as pd
pd.set_option('display.float_format', lambda x: '%.5f' % x)
from plotly.offline import init_notebook_mode
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_df_rows(df):
    '''The function returns number of
    rows in a dataframe
    :params: df
    :type: pandas.dataFrame
    return: pandas.dataFrame
    '''
    return df_shape[0]


def get_graphs_from_df_of_specific_countries(df, x_title = "",y_title="",plot_title="",df2=None, df2_subj = "", allowed_countries = [],start_yr=0):
    ''' This function accepts a dataframe and returns a plotly figure
    figure object. If there are multiple columns, then plot will be done
    for each column on the same graph
    :params:
           df = The concerned dataframe,
           x_title = x-axis label,
           y_title = y-axis label,
           plot_title = Title of the plot,
           df2 = Second Dataframe in case plots from 2 dataframes are needed,
           df2_subj = "Subject for legend for dataframe 2 (df2)",
           allowed_countries = To plot only the mentioned columns
    :type:
          df = pandas.dataFrame
          x_title = str
          y_title = str
          plot_title = str
          df2 = pandas.dataFrame
          df2_subj = str
          allowed_countries = list
    :return: Figure.figure

    '''
    assert isinstance(df,pd.core.frame.DataFrame)
    assert isinstance(x_title,str)
    assert isinstance(y_title,str)
    assert isinstance(plot_title,str)

    assert isinstance(df2_subj,str)
    assert isinstance(allowed_countries,list)
    colors = px.colors.qualitative.Plotly
    df['id']=[x + start_yr for x in df.index]


    fig = make_subplots(specs=[[{"secondary_y": True}]])


    # Update plot sizing
    fig.update_layout(
        width=800,
        height=600,
        autosize=False,
        margin=dict(t=50, b=0, l=0, r=0),
        paper_bgcolor= 'white',
        plot_bgcolor= 'white',
        #xaxis_title = x_title,
        yaxis = go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text=y_title,
            font=dict(

                size=15,
                color="#757272"
            )
        )
    ),
        xaxis= go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text=x_title,
            font=dict(

                size=15,
                color="#757272"
            )
        )
    ),
        title_text=plot_title,
        title_font_size=18


    )
    country_count = len(df.columns)
    countries = df.columns
    if df2 is not None:
        country_count = country_count*2

    butts = []
    traces = {}
    i=0
    one_hot_visibility = {}
    for c in countries:

        if c not in allowed_countries and allowed_countries!=[]:
            continue

        fig.add_trace(
                go.Scatter(x=df['id'], y = df[c], mode = 'lines', line_shape='spline', name=c),
                secondary_y=False,
            )
        if df2 is not None:
            fig.add_trace(
                        go.Scatter(x=df['id'], y = df2[c], mode = 'lines', line_shape='spline', name=c + '\n' + df2_subj),
                        secondary_y=True,
                    )

        one_hot_visibility[c] = [False]*country_count

        one_hot_visibility[c][i] = True
        if df2 is not None:
            one_hot_visibility[c][i+1] = True

        butts.append(dict(label = c, method = "update", args = [{"visible": one_hot_visibility[c]}, {"title": c, "showlegend": True}]))
        i+=1
        if df2 is not None:
            i+=1
    return fig
