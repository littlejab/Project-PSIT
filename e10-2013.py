"""e10 2013 graph"""
def graph_e10_2013():
    """show graph of gas e10 price in year 2013 by min, avg, max"""
    import plotly.plotly as py
    import plotly.graph_objs as go
    py.sign_in('littlejab', 'yblima8sc3')
    chart_min = go.Bar(
        x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
        'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
        y=[38.07, 39.78, 39.61, 37.81, 37.57, 38.65, 39.88, 39.42, 39.06, 38.57, 38.43, 39.74],
        name='Min'
    )

    chart_avg = go.Bar(
        x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
            'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
        y=[38.1, 39.83, 39.61, 37.83, 37.58, 38.67, 40.09, 39.45, 39.25, 38.57, 38.78, 39.76],
        name='Average'
    )

    chart_max = go.Bar(
        x=['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
            'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
        y=[38.18, 39.96, 39.61, 37.94, 37.63, 38.75, 40.16, 39.58, 39.3, 38.58, 38.81, 39.81],
        name='Max'
    )
    data = [chart_min, chart_avg, chart_max]
    layout = go.Layout(
        barmode='group'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='E10 2013')
graph_e10_2013()
