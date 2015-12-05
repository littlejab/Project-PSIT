import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['Jan 12', 'Feb 12', 'Mar 12', 'Apr 12', 'May 12', 'Jun 12', 'Jul 12', 'Aug 12', \
    'Sep 12', 'Oct 12', 'Nov 12', 'Dec 12'],
    y=[41.65, 43.79, 45.82, 47.16, 45.85, 44.34, 45.9, 48.08, 47.94, 48.22, 47.96, 48.48],
    name='Min'
)

chart_avg = go.Bar(
    x=['Jan 12', 'Feb 12', 'Mar 12', 'Apr 12', 'May 12', 'Jun 12', 'Jul 12', 'Aug 12', \
        'Sep 12', 'Oct 12', 'Nov 12', 'Dec 12'],
    y=[41.79, 43.94, 45.97, 47.31, 46, 44.5, 46.03, 48.22, 48.09, 48.37, 48.11, 48.67],
    name='Average'
)

chart_max = go.Bar(
    x=['Jan 12', 'Feb 12', 'Mar 12', 'Apr 12', 'May 12', 'Jun 12', 'Jul 12', 'Aug 12', \
        'Sep 12', 'Oct 12', 'Nov 12', 'Dec 12'],
    y=[42.54, 44.72, 46.77, 48.13, 46.82, 45.31, 46.75, 48.95, 48.89, 49.19, 48.91, 49.32],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Gasoline 95 2012')
