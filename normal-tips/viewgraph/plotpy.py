# More messeges can be found in link: https://plot.ly/python/

import plotly.offline as py
import numpy as np
import plotly.graph_objs as go

# plotly.offline.init_notebook_mode(connected=True)
# iplot can only run inside an IPython Notebook.

# 坐标图
N = 100
rand_x = np.linspace(0, 1, N)
rand_y0 = np.random.randn(N) + 5
rand_y1 = np.random.randn(N)
rand_y2 = np.random.randn(N) - 5

trace0 = go.Scatter(
    x=rand_x,
    y=rand_y0,
    mode='markers',
    name='markers'
)
trace1 = go.Scatter(
    x=rand_x,
    y=rand_y1,
    mode='lines+markers',
    name='lines+markers'
)
trace2 = go.Scatter(
    x=rand_x,
    y=rand_y2,
    mode='lines',
    name='lines'
)

data = [trace0, trace1, trace2]
py.plot(data)

# 散点图
trace3 = go.Scatter(
    y=np.random.randn(500),
    mode='markers',
    marker=dict(
        size=16,
        color=np.random.randn(500),
        colorscale='Viridis',
        showscale=True
    )
)
data1 = [trace3]
py.plot(data1, filename='scatter-plot-with-colorscale')







