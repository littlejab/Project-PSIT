import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
    'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[35.58, 35.58, 35.81, 35.94, 36.07, 35.85, 35.67, 34.94, 33.98, 33.11, 31.67, 28.20],
    name='Min'
)

chart_avg = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
        'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[35.74, 35.22, 35.81, 35.94, 36.07, 35.87, 35.68, 34.94, 33.98, 33.11, 31.67, 28.20],
    name='Average'
)

chart_max = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
        'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[35.76, 35.58, 35.81, 35.94, 36.15, 36.08, 35.81, 34.94, 33.98, 33.11, 31.73, 28.23],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='E20 2014')