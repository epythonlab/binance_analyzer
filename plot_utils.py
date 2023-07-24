
# plot_utils.py

import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_trend_plot(dates, prices, coin):
    fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
    fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines', name=coin))
    fig.update_layout(
        title_text=f"{coin} - Price Trend",
        xaxis_rangeslider_visible=False,
        template = 'plotly_dark'
    )
    return fig