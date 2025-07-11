import plotly.graph_objects as go
import dateutil 
import pandas_ta as pta 
import datetime 


def plotly_table(dataframe):
    dataframe.columns = [col[0] if isinstance(col, tuple) else col for col in dataframe.columns]
    dataframe.columns = [str(col).strip() for col in dataframe.columns]  # remove extra spaces
    headerColor = 'grey'
    rowEvenColor = '#f8fafd'
    rowOddColor = '#e1efff'
    fig = go.Figure(data =[go.Table(
    header = dict(
        values = ['<b><b>'] + ['<b>'+str(i)[:10]+"<b>" for i in dataframe.columns],
        line_color = '#0078ff',fill_color = '#0078ff',
        align = 'center',font = dict(color='white',size=15),height=35
    ),
    cells = dict(
        values = [['<b>'+str(i)+'<b>' for i in dataframe.index]]+[dataframe[col] for col in dataframe.columns],fill_color =[[rowOddColor,rowEvenColor]],
        align = 'left',line_color =['white'],font=dict(color=['black'],size=15)
        
    ))  
    ])
    fig.update_layout(height = 400,margin = dict(l=0,r=0,t=0,b=0))
    return fig


def filter_data(dataframe, num_period):
    if num_period == '1mo':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-1)
    elif num_period == '5d':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(days=-5)
    elif num_period == '6mo':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-6)
    elif num_period == 'ly':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta (years=-1)
    elif num_period == '5y':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta (years=-5)
    elif num_period == 'ytd':
        date = datetime.datetime(dataframe.index[-1].year, 1, 1).strftime('%Y-%m-%d')
    else:
        date = dataframe.index [0]

    return dataframe.reset_index() [dataframe.reset_index() ['Date']>date]

def close_chart(dataframe,num_period=False):
    if num_period:
        dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'],y = dataframe['Open'],
                             mode = 'lines',name = 'Open',line = dict(width =2 , color='yellow')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y = dataframe['Close'],
                             mode = 'lines',name = 'Close',line = dict(width =2 , color='black')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y = dataframe['High'],
                             mode = 'lines',name = 'high',line = dict(width =2 , color='pink')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y = dataframe['Low'],
                             mode = 'lines',name = 'Low',line = dict(width =2 , color='red')))
    fig.update_xaxes(rangeslider_visible = True)
    fig.update_layout(height = 500,margin=dict(l=0,r=0,t=0,b=0),plot_bgcolor = 'white',paper_bgcolor='#e1efff',legend=dict(
        yanchor ='top',
        xanchor = 'right'
    ))
    return fig 

def candlestick(dataframe,num_period):
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=dataframe['Date'],
                                open = dataframe['Open'], close = dataframe['Close'],
                                high = dataframe['High'], low = dataframe['Low']
                                ))
    fig.update_layout(showlegend= False,height = 500,margin=dict(l=0,r=0,t=0,b=0),plot_bgcolor = 'white',paper_bgcolor='#e1efff')
    return fig 

def RSI(dataframe,num_period):
    dataframe['rsi'] = pta.rsi(dataframe['Close'])
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['rsi'],marker_color ='orange',line=dict(
        width = 2, color = 'orange')
    ))
    fig.add_trace(go.Scatter(x=dataframe['Date'],
        y=[70]*len(dataframe),name='OverBought',marker_color ='red',line=dict(
        width = 2, color = 'red',dash = 'dash')
    ))
    fig.add_trace(go.Scatter(x=dataframe['Date'],
        y=[30]*len(dataframe),fill='tonexty',name='OverSold',marker_color ='#79da84',line=dict(
        width = 2, color = '#79da84',dash = 'dash')
    ))
    fig.update_layout(yaxis_range=[0,100],
                    height=200,margin=dict(l=0,r=0,t=0,b=0),plot_bgcolor = 'white',paper_bgcolor='#e1efff',legend=dict(orientation = 'h',
        yanchor ='top',
        y=1.02,
        xanchor = 'right',
        x=1
    )
    )
    return fig

def MovingAverage(dataframe,num_period):
    dataframe['SMA_50'] = pta.sma(dataframe['Close'],50)
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'],y = dataframe['Open'],
                             mode = 'lines',name = 'Open',line = dict(width =2 , color='yellow')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y = dataframe['Close'],
                             mode = 'lines',name = 'Close',line = dict(width =2 , color='black')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y = dataframe['High'],
                             mode = 'lines',name = 'high',line = dict(width =2 , color='pink')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y = dataframe['Low'],
                             mode = 'lines',name = 'Low',line = dict(width =2 , color='red')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y = dataframe['SMA_50'],
                             mode = 'lines',name = 'SMA_50',line = dict(width =2 , color='purple')))
    fig.update_xaxes(rangeslider_visible = True)
    fig.update_layout(height = 500,margin=dict(l=0,r=0,t=0,b=0),plot_bgcolor = 'white',paper_bgcolor='#e1efff',legend=dict(
        yanchor ='top',
        xanchor = 'right'
    ))
    return fig  

def MACD(dataframe , num_period):
    macd = pta.macd(dataframe['Close'])
    macd_line = macd['MACD_12_26_9']
    macd_signal = macd['MACDs_12_26_9']
    macd_hist = macd['MACDh_12_26_9']
    dataframe['MACD'] = macd_line
    dataframe['MACD Signal'] = macd_signal
    dataframe['MACD Hist'] = macd_hist
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x= dataframe['Date'],
        y = dataframe['MACD'], name='MACD',marker_color ='orange',line=dict(
        width = 2, color = 'orange')
    ))
    fig.add_trace(go.Scatter(
        x= dataframe['Date'],
        y = dataframe['MACD Signal'], name='MACD Signal',marker_color ='red',line=dict(
        width = 2, color = 'red',dash ='dash')
    ))
    c = ['red' if cl<0 else 'green' for cl in macd_hist]
    fig.update_layout(yaxis_range=[0,100],
                    height=200,margin=dict(l=0,r=0,t=0,b=0),plot_bgcolor = 'white',paper_bgcolor='#e1efff',legend=dict(orientation = 'h',
        yanchor ='top',
        y=1.02,
        xanchor = 'right',
        x=1
    )
    )
    return fig

def Moving_Average_forecast(forecast):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x = forecast.index[:-30],y=forecast['Close'].iloc[-30:],
        mode = 'lines',name = 'Close Price',line = dict(width = 2,color ='black' )
    ))
    fig.add_trace(go.Scatter(x = forecast.index[:-31],y=forecast['Close'].iloc[-31:],
        mode = 'lines',name = 'Future Close Price',line = dict(width = 2,color ='red')
    ))

    fig.update_xaxes(rangeslider_visible = True)
    fig.update_layout(height = 500,margin=dict(l=0,r=0,t=0,b=0),plot_bgcolor = 'white',paper_bgcolor='#e1efff',legend=dict(
        yanchor ='top',
        xanchor = 'right'
    ))
    return fig  