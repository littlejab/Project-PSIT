import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[30.41, 29.97, 29.69, 26.01],
    name='Min'
)

chart_avg = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[30.42, 29.97, 29.69, 26.02],
    name='Average'
)

chart_max = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[30.51, 30.01, 29.73, 26.06],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Diesel All Year')