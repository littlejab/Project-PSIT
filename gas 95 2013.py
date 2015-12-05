import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
    'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
    y=[46.27, 48.2, 47.33, 45.03, 44.79, 45.91, 47.4, 46.94, 46.58, 46.09, 45.95, 47.26],
    name='Min'
)

chart_avg = go.Bar(
    x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
        'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
    y=[47.03, 48.41, 47.33, 45.05, 44.82, 46.02, 47.62, 46.98, 47.06, 46.4, 46.55, 47.65],
    name='Average'
)

chart_max = go.Bar(
    x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
        'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
    y=[48.27, 48.64, 47.33, 45.16, 44.88, 46.14, 47.68, 47.05, 47.38, 46.6, 46.83, 47.83],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Gasoline 95 2013')
