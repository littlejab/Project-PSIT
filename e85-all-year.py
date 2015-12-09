import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[22.22, 22.73, 24.11, 22.92],
    name='Min'
)

chart_avg = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[22.23, 22.74, 24.11, 22.92],
    name='Average'
)

chart_max = go.Bar(
    x=['2012', '2013', '2014', '2015'],
    y=[22.23, 22.74, 24.11, 22.92],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='E85 All Year')