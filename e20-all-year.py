import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[34.34, 33.79, 34.37, 26.26],
    name='Min'
)

chart_avg = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[34.35, 33.82, 34.35, 26.26],
    name='Average'
)

chart_max = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[34.36, 33.87, 34.43, 26.32],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='E20 All Year')