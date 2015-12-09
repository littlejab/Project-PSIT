import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
    'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
    y=[32.62, 34.33, 34.46, 32.86, 32.62, 33.70, 35.12, 34.47, 34.11, 33.62, 33.83, 34.79],
    name='Min'
)

chart_avg = go.Bar(
    x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
        'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
    y=[32.62, 34.33, 34.46, 32.86, 32.62, 33.71, 35.12, 34.50, 34.34, 33.62, 33.83, 34.80],
    name='Average'
)

chart_max = go.Bar(
    x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
        'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
    y=[32.62, 34.33, 34.46, 32.86, 32.68, 33.82, 35.12, 34.73, 34.35, 33.63, 33.86, 34.86],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='E20 2013')