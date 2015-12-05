import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[37.94, 38.8, 38.83, 28.77],
    name='Min'
)

chart_avg = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[37.96, 38.89, 38.85, 28.79],
    name='Average'
)

chart_max = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[38.01, 38.95, 38.94, 28.84],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='E10 All Year')