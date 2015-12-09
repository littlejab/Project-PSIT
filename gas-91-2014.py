import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
    'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[38.08, 38.08, 38.31, 38.44, 38.52, 38.33, 38.17, 37.37, 35.78, 34.79, 32.97, 29.57],
    name='Min'
)

chart_avg = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
        'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[38.23, 38.08, 38.31, 38.44, 38.58, 38.38, 38.19, 37.37, 35.78, 34.73, 32.97, 29.57],
    name='Average'
)

chart_max = go.Bar(
    x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
        'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
    y=[38.26, 38.08, 38.31, 38.44, 38.71, 38.58, 38.31, 37.37, 35.78, 34.73, 32.97, 29.61],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Gasohol91 2014')
