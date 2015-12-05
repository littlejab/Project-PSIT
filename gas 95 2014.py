import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
    'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[48.22, 48.05, 48.28, 48.41, 48.99, 48.8, 48.75, 48.37, 44.86, 43.81, 42.05, 38.58],
    name='Min'
)

chart_avg = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
        'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[48.54, 48.42, 48.67, 48.78, 49.24, 49.18, 49.18, 48.67, 44.87, 43.98, 42.39, 38.85],
    name='Average'
)

chart_max = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
        'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[48.73, 48.55, 48.78, 48.91, 49.5, 49.52, 49.41, 48.85, 44.97, 44.12, 42.7, 39.03],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Gasoline 95 2014')
