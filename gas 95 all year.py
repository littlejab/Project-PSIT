import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[46.27, 46.41, 46.43, 34.87],
    name='Min'
)

chart_avg = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[46.42, 46.66, 46.73, 35.17],
    name='Average'
)

chart_max = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[47.19, 46.91, 46.92, 35.37],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Gasoline 95 All Year')