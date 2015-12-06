import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['Jan 12', 'Feb 12', 'Mar 12', 'Apr 12', 'May 12', 'Jun 12', 'Jul 12', 'Aug 12', \
    'Sep 12', 'Oct 12', 'Nov 12', 'Dec 12'],
    y=[30.45, 31.31, 32.12, 31.99, 30.51, 29.58, 29.74, 29.89, 29.93, 29.79, 29.79, 29.79],
    name='Min'
)

chart_avg = go.Bar(
    x=['Jan 12', 'Feb 12', 'Mar 12', 'Apr 12', 'May 12', 'Jun 12', 'Jul 12', 'Aug 12', \
        'Sep 12', 'Oct 12', 'Nov 12', 'Dec 12'],
    y=[30.46, 31.31, 32.12, 32.06, 30.54, 29.58, 29.74, 29.89, 29.95, 29.79, 29.79, 29.79],
    name='Average'
)

chart_max = go.Bar(
    x=['Jan 12', 'Feb 12', 'Mar 12', 'Apr 12', 'May 12', 'Jun 12', 'Jul 12', 'Aug 12', \
        'Sep 12', 'Oct 12', 'Nov 12', 'Dec 12'],
    y=[30.51, 31.31, 32.14, 32.43, 30.7, 29.75, 29.86, 30.07, 29.99, 29.81, 29.79, 29.79],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Diesel 2012')
