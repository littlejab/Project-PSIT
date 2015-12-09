import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
    y=[25.12, 25.75, 26.63, 25.83, 26.86, 27.35],
    name='Min'
)

chart_avg = go.Bar(
    x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
    y=[25.12, 25.78, 26.63, 25.83, 26.86, 27.35],
    name='Average'
)

chart_max = go.Bar(
    x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
    y=[25.12, 25.95, 26.67, 25.87, 26.91, 27.42],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='E20 2015')
