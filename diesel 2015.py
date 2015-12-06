import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
    y=[25.83, 26.22, 26.76, 25.26, 26.07, 25.9],
    name='Min'
)

chart_avg = go.Bar(
    x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
    y=[25.83, 26.27, 26.77, 25.26, 26.07, 25.9],
    name='Average'
)

chart_max = go.Bar(
    x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
    y=[25.83, 26.4, 26.84, 25.28, 26.09, 25.9],
    name='Max'
)

data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Diesel 2015')