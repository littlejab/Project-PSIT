import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('littlejab', 'yblima8sc3')
chart_min = go.Bar(
    x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
    'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
    y=[35.62, 37.07, 37.16, 35.36, 35.12, 36.20, 37.43, 36.97, 36.61, 36.12, 35.98, 37.29],
    name='Min'
)

chart_avg = go.Bar(
    x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
        'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
    y=[35.64, 37.34, 37.16, 35.37, 35.13, 36.21, 37.63, 36.99, 36.84, 36.12, 36.33, 37.30],
    name='Average'
)

chart_max = go.Bar(
    x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
        'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
    y=[35.73, 37.51, 37.16, 35.45, 35.18, 36.30, 37.71, 37.13, 36.85, 36.13, 36.36, 37.36],
    name='Max'
)
data = [chart_min, chart_avg, chart_max]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Gasohol91 2013')
