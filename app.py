import dash
from dash import html, dcc
from dash.dependencies import Input, Output

from fetch_data import get_binance_data, extract_data
from plot_utils import create_trend_plot

app = dash.Dash(__name__)


app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='coin-dropdown',
            options=[
                {'label': 'BTC', 'value': 'BTC'},
                {'label': 'ETH', 'value': 'ETH'},
                {'label': 'BNB', 'value': 'BNB'}
            ],
            value='BTC',
            style={'width': '50%', 'margin':'20px', 'margin-left':'30px'}
        ),
        dcc.Tabs(
            id="tabs",
            value="1d",
            children=[
                dcc.Tab(label="1 Hour", value="1h"),
                dcc.Tab(label="1 Day", value="1d"),
                dcc.Tab(label="1 Week", value="1w"),
                dcc.Tab(label="1 Month", value="1M"),
            ],
            style={'width': '100%', 'margin':'20px', 'margin-left': '10px'}
        )
    ], style={'display': 'flex'}),
    html.Div([
        dcc.Graph(id='coin-trend-graph')
    ])
])

@app.callback(
    Output('coin-trend-graph', 'figure'),
    [Input('coin-dropdown', 'value'),
     Input('tabs', 'value')]
)
def update_graph(selected_coin, selected_interval):
    data = get_binance_data(f"{selected_coin}USDT", selected_interval, 100)
    dates, prices = extract_data(data)
    fig = create_trend_plot(dates, prices, selected_coin)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
