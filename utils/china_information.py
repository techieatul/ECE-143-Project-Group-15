import pandas as pd
import numpy as np
import os
from collections import defaultdict
import plotly.express as px
import plotly.graph_objects as go


def preprocess_PPI_Info(file,save_plot=None):
    '''
    Preprocess the PPI infomation file of china
    Data in the csv have project name and year of investment
    along with the amount of investment in random order
    '''
    assert os.path.isfile(file),'file is not present'
    # Read the file and fills in the zero where the data is absent
    data=pd.read_csv(file,error_bad_lines=False).fillna(0.0)
    amount = defaultdict(float)
    nu=defaultdict(int)
    for i in range(data.shape[0]):
        s= data.loc[i]
        # converting the amount as the values are in million
        amount[int(s['InvestmentYear'])]+=s['TotalInvestment']*1e6
    #Extracting the data above 2000
    new_dict = {}
    for i in range(2000,2022):
        new_dict[str(i)]=amount[i]
    data_frame = pd.DataFrame({'Year':new_dict.keys(),'Investment':new_dict.values()})
    plot_line(data_frame,title='Private Participation in Infrastructure for [2000-2021]',
              xaxis = 'Year',
              yaxis='Investment',
              titlex='Years',
              titley='Investments in USD',
              path=save_plot)

def china_social_spending(healthcare_file,education_file,gdp_file,save_plot=None):
    '''
    Give the gdp and spending on healtcare and education spending in term of persentage of gdp
    this functions return the cleaned data in term of total amount spent for every year

    '''
    assert os.path.isfile(healthcare_file) and os.path.splitext(healthcare_file)[-1]==".csv",'Healtcare csv missing'
    assert os.path.isfile(education_file) and os.path.splitext(education_file)[-1]==".csv",'Education file missing'
    assert os.path.isfile(gdp_file) and os.path.splitext(gdp_file)[-1]==".xlsx",'GDP file missing'
    data_frame_healtcare = pd.read_csv(healthcare_file)
    data_frame_healtcare=data_frame_healtcare.set_index('Country Name')
    dic_healtcare={}
    y=2000 # year from which the data is required
    years = [i for i in range(2000,2018)]
    for i in data_frame_healtcare.loc['China'][3:-2]:
        dic_healtcare[y]=i
        y+=1
    data_frame_edu = pd.read_csv(education_file)
    data_frame_edu=data_frame_edu.set_index('Year')
    dic_edu={}

    for i in years:
        dic_edu[i]=data_frame_edu.loc[i]["Investment in GDP"]
    data_gdp = pd.read_excel(gdp_file)
    gdp_china=data_gdp[['Year','China']].set_index('Year')
    total_money = {}

    for i in years:
        yr = gdp_china.loc[i]['China']
        total_money[i] = (yr*dic_edu[i]+yr*dic_healtcare[i])/1e2
    data_frame=pd.DataFrame({'Year':total_money.keys(),'Investment in USD':total_money.values()})
    plot_line(data_frame,title='Social Spending [2000-2021]',
              xaxis = 'Year',
              yaxis='Investment in USD',
              titlex='Years',
              titley='Expenditure in USD',
              path=save_plot)

def plot_line(dataframe,title,xaxis,yaxis,titlex,titley,path):
    '''
    PLot the line plot the dataframe and saves the figure
    '''
    fig = px.line(dataframe, x=xaxis, y=yaxis)

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
                text=titley,
                font=dict(

                    size=15,
                    color="#757272"
                )
            )
        ),
            xaxis= go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text=titlex,
                font=dict(

                    size=15,
                    color="#757272"
                )
            )
        ),
        title={
            'text': title,
            'font_size':18,
            'y':1,
            'x':0.05,
            'xanchor': 'left',
            'yanchor': 'top'}

            )
    return fig
