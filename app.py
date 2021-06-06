#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Final App

import plotly.graph_objects as go # We are only importing the 'graph_objects' module from plotly here
import pandas as pd
import numpy as np 
import plotly as py
import plotly.io as pio
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.offline import iplot


#df = pd.read_excel('/Users/antoniopsalgueiro/Google Drive/Pós-Graduação/2º semestre/Data Visualization/Projeto2_Grupo/DataSet_python_v0.5.xlsx').sort_values(by=['Year'])

df = pd.read_csv('https://raw.githubusercontent.com/apsalgueiro/DVNovaIMS/master/DataSet_python_v0.6.csv').sort_values(by=['Year'])

df_scatter = pd.melt(df, id_vars=['Year', 'Country', 'CountryCode'], var_name='Indicator Name', value_name='Value')

matcorr = df.corr('pearson').drop(index=['Year'], columns=['Year'])

available_indicators = df_scatter['Indicator Name'].unique()
available_countries = df_scatter['Country'].unique()

RadioItemsCountry = dcc.RadioItems(
                id='country_Radio',
                options=[{'label': i, 'value': i} for i in available_countries],
                value='Portugal',
                labelStyle={'display': 'inline-block'}
            )

Dropdown1Scatter = dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Internal Tourists Check-in'
            )

RadioItems1Scatter =  dcc.RadioItems(
                   id='xaxis-type',
                   options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                   value='Linear',
                   labelStyle={'display': 'inline-block'}
            )

Dropdown2Scatter = dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Internal Tourists Check-in'
            )

RadioItems2Scatter = dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
           )

ChecklistCorr = dcc.Checklist(
        id='variables',
        options=[{'label': x, 'value': x} for x in matcorr.columns],
        value=matcorr.columns.tolist())

animations = {
    'Scatter': px.scatter(
        df, x="Tourists Accommodation Facilities", y="Tourism Employees", animation_frame="Year", 
        size="Total Tourists Check-in", color="Country", 
        hover_name="Country", log_x=False, size_max=55, 
        range_x=[0,60000], range_y=[0,600000]),
    
    'Bar': px.bar(
        df, x="Country", y="Percent of Tourism for Total GDP", color="Country", 
        animation_frame="Year",
        range_y=[0,0.3]),
             }

RadioItemsAnimation =   dcc.RadioItems(
        id='selection',
        options=[{'label': x, 'value': x} for x in animations],
        value='Scatter'
    )

year_options = [
    {'label': 'Year 2001', 'value': 2001},
    {'label': 'Year 2002', 'value': 2002},
    {'label': 'Year 2003', 'value': 2003},
    {'label': 'Year 2004', 'value': 2004},
    {'label': 'Year 2005', 'value': 2005},
    {'label': 'Year 2006', 'value': 2006},
    {'label': 'Year 2007', 'value': 2007},
    {'label': 'Year 2008', 'value': 2008},
    {'label': 'Year 2009', 'value': 2009},
    {'label': 'Year 2010', 'value': 2010},
    {'label': 'Year 2011', 'value': 2011},
    {'label': 'Year 2012', 'value': 2012},
    {'label': 'Year 2013', 'value': 2013},
    {'label': 'Year 2014', 'value': 2014},
    {'label': 'Year 2015', 'value': 2015},
    {'label': 'Year 2016', 'value': 2016},
    {'label': 'Year 2017', 'value': 2017},
    {'label': 'Year 2018', 'value': 2018},
    {'label': 'Year 2019', 'value': 2019}
]

tourism_options = [
    {'label': 'Internal Tourists Check-in', 'value': 'Internal Tourists Check-in'},
    {'label': 'External Tourists Check-in', 'value': 'External Tourists Check-in'},
    {'label': 'Total Tourists Check-in', 'value': 'Total Tourists Check-in'}
]

mapdropdown = dcc.Dropdown(
              id ='year_drop',
              options=year_options,
              value=2001,
              multi=False
              )
    
mapradio = dcc.RadioItems(
           id='tourism_radio',
           options=tourism_options,
           value='Internal Tourists Check-in',
           labelStyle={'display': 'inline-block'}
           )

##################################################APP###################################################################

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    
html.H1('Evolution of tourism and the impact on macroeconomics'),
html.H5("In 2019, tourism activities have contributed to more than 2 billion euros to the European GDP and are an important source of income for countries."
"This visualization explores the economic tourism data of six European countries: France, Germany, Hungary, Portugal, Slovakia and Spain between the years of 2001 to 2019, concerning the evolution of the number of tourists, accommodations, jobs related to tourism and the impact on countries’ GDP."),
   
    html.Div([
   
      html.Div([
      html.H6("Map Chart - Tourism check-ins per type and year", style={"font-weight": "bold"}),

      html.P("Evolution of the number of check-ins, from resident and non-resident tourists, on tourism accommodations, for the selected countries during the range period of 19 years." )
      ],style={'display': 'inline-block', 'width': "100%", 'height':"20%"}, className="control_label"),
       
       html.Div([
       
            html.Div([
            html.Label('Choose the year:'),
            mapdropdown,
            ], style={'display': 'inline-block', 'width': "30%", 'height':"100%"},className='box_space'),
     
            html.Div([
            html.Label('Choose the data:'),
            mapradio,
            ], style={'display': 'inline-block', 'width': "70%", 'height':"100%"},className='box_space'),
    
       ], style={'display': 'flex', 'width': "100%", 'height':"100%", "text-align": "center"}),

       html.Div([
       dcc.Graph(id='graph_example')
       ], style={'display': 'inline-block', 'width': "100%", 'height':"100%"}),

   ],style={'display': 'inline-block','width': "100%", 'height':"100%"}),
 
   html.Div([],style={'display': 'inline-block', 'width': "100%", 'height':"100%"},className='box_line'),
    
   html.Div([
      html.Div([
      html.H6("Scatter Chart – Tourism related jobs and accommodations", style={"font-weight": "bold"}),
      html.P("Comparison between Number of Tourism Employees, Tourists Accommodation Facilities and Total check-ins per country and how these indicators evolved during 2001 until 2019."),
      html.H6("Bar Chart – Impact of tourism activities on the countries’ economy", style={"font-weight": "bold"}),
      html.P("Percentage of tourism activities for the total of countries’ GDP and how they perform from 2001 to 2019."),
      ],style={'display': 'inline-block', 'width': "100%", 'height':"100%"}, className="control_label"),
   
   html.P("Choose the chart:"),
   RadioItemsAnimation,
    
   dcc.Graph(id="graph"),
   ],style={'display': 'inline-block', 'width': "100%", 'height':"100%"}),

   html.Div([],style={'display': 'inline-block', 'width': "100%", 'height':"100%"},className='box_line'),
    
   html.Div([
       
      html.Div([
      html.H6("Scatter Chart - Comparison of tourism and macroeconomic indicators", style={"font-weight": "bold"}),

      html.P("Behavior comparison between the total economic and tourism variables chosen for each country in linear and logarithm scales related to the period range." )
      ],style={'display': 'inline-block', 'width': "100%", 'height':"20%"}, className="control_label"),
    
      html.Div([
        
      html.Label('Choose a country:'),
      RadioItemsCountry,
        
      html.Br(),

            html.Div([
            html.Label('Choose a variable:'),
            Dropdown1Scatter,
            
            RadioItems1Scatter,
            ],
            style={'width': '48%', 'display': 'inline-block'}),

            html.Div([
            html.Label('Choose a variable:'),
            Dropdown2Scatter,
            
            RadioItems2Scatter,
            
            ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
      ]),

   dcc.Graph(id='indicator-graphic'),
   
   ],style={'display': 'inline-block', 'width': "100%", 'height':"100%"}),
    
   html.Div([],style={'display': 'inline-block', 'width': "100%", 'height':"100%"},className='box_line'),
    
   html.Div([
      html.Div([
      html.H6("Heatmap chart - Correlation between variables", style={"font-weight": "bold"}),

      html.P("Direct correlation between the indicators to illustrate how they perform together.")
      ],style={'display': 'inline-block', 'width': "100%", 'height':"20%"}, className="control_label"),
     
     html.Div([
       html.Div([
    
       html.Label('Choose variables:'),
   
       ChecklistCorr,
        
       ],style={'width': "20%",'height':"100%",'width': "20%"}),

      html.Div([
      dcc.Graph(id='heatmap')],style={'width': "80%",'height':"100%"}),
      
      ], style={'display': 'flex'}),
         
      ], style={'display': 'inline-block','width': "100%", 'height':"100%"}),
    
   html.Div([],style={'display': 'inline-block', 'width': "100%", 'height':"100%"},className='box_line'),
   
  html.Div([
     html.Div(
            [
                html.H6("Authors", style={"font-weight": "bold"}),
                dcc.Markdown(
                    """\
                         Ana Pereira: M20200418 | António Salgueiro: M20200449 | Carla Lopes: M20200369
                        """
                ,style={"font-size":"12pt",'display': 'inline-block', 'width': "100%", 'height':"100%"}),
                
            ],
            className="control_label2"
        ),
    
     html.Div(
            [
                html.H6("Sources", style={"font-weight": "bold"}),
                dcc.Markdown(
                    """\
                         - Pordata Tourism: https://www.pordata.pt/en/Theme/Europe/Tourism-60
                         - Pordata Macroeconomics: https://www.pordata.pt/en/Theme/Europe/Macroeconomics-32
                         - ILOSTAT: https://www.ilo.org/shinyapps/bulkexplorer10/?lang=en&segment=indicator&id=EAP_2EAP_SEX_AGE_NB_A
                         - Statista: https://www.statista.com/topics/3848/travel-and-tourism-in-europe/
                        """
                ,style={"font-size":"12pt",'display': 'inline-block', 'width': "100%", 'height':"100%","text-align" : "left"}),
                
            ],
            className="control_label2"
        )
     ], style={'display': 'inline-block','width': "100%", 'height':"100%"})
])    
######################################################Callbacks#########################################################

######################################################WorldMap#########################################################

@app.callback(
    Output('graph_example', 'figure'),
    [Input('year_drop', 'value'),
     Input('tourism_radio', 'value')]
)
    
def update_graph(years, tourism):
    scatter_data = []

    filtered_by_year_and_country_df = df.loc[df['Year'] == years]

    temp_data = dict(type='choropleth',
                     locations=filtered_by_year_and_country_df['Country'],
                     locationmode='country names',
                     z=filtered_by_year_and_country_df[tourism],
                     text=filtered_by_year_and_country_df['Country'],
                     colorscale='aggrnyl',
                     autocolorscale=False,
                     reversescale=True,
                     marker_line_color='darkgray',
                     marker_line_width=0.5,
                     )
    scatter_data.append(temp_data)

    scatter_layout = dict(geo=dict(scope='europe', 
                                   projection=dict(type='equirectangular'
                                                   ),
                                   showland=True,  # default = True
                                   landcolor='light grey',
                                   lakecolor='white',
                                   showocean=True,  # default = False
                                   oceancolor='azure'
                                   ),
                          margin = dict(t=10,r=10,b=10,l=10),
                          autosize = True
                          )

    fig = go.Figure(data=scatter_data, layout=scatter_layout)

    return fig

######################################################Dynamic#########################################################

@app.callback(
    Output("graph", "figure"), 
    [Input("selection", "value")])
def display_animated_graph(s):
    return animations[s]


######################################################Variables#########################################################
@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    Input('country_Radio', 'value'))
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 country_value):
    
    dff = df_scatter[df_scatter['Country'] == country_value]

    fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                     y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                     hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Year'])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    return fig

######################################################Heatmap#########################################################
@app.callback(
    Output('heatmap', 'figure'), 
    [Input('variables', 'value')])

def filter_heatmap(cols):
    
    data_heatmap = px.imshow(matcorr[cols],color_continuous_scale='RdBu',range_color=[-1,1])
    
    #data_heatmap.update_xaxes(side="top")

    data_heatmap.update_layout(margin = dict(t=10,r=10,b=10,l=10),
    autosize = True )
    
    return go.Figure(data=data_heatmap)

if __name__ == '__main__':
    app.run_server(debug=False, port = 9213)


# In[ ]:




