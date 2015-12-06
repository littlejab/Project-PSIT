import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
    'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[29.99, 29.99, 29.99, 29.99, 29.99, 29.91, 29.85, 29.86, 29.99, 29.66, 29.41, 27.6],
    name='Min'
)

chart_avg = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
    'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[29.99, 29.99, 29.99, 29.99, 29.99, 29.91, 29.85, 29.86, 29.99, 29.66, 29.42, 27.64],
    name='Average'
)

chart_max = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
    'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[29.99, 29.99, 29.99, 29.99, 30.05, 30.01, 29.85, 29.86, 29.99, 29.66, 29.42, 27.91],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Diesel 2014')