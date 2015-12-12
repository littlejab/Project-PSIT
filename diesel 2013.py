"""Diesel Chart 2013"""
def diesel_2013():
    """Display monthly chart for diesel price in Thailand 2013."""
    import plotly.plotly as py
    import plotly.graph_objs as go
    py.sign_in('littlejab', 'yblima8sc3')
    chart_min = go.Bar(
        x = ['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
        'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
        y = [29.79, 29.95, 29.99, 29.99, 29.99, 29.99, 29.99, 29.99, 29.99, 29.99, 29.99, 29.99],
        name = 'Min'
    )
    chart_avg = go.Bar(
        x = ['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
            'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
        y = [29.79, 29.95, 29.99, 29.99, 29.99, 29.99, 29.99, 29.99, 29.99, 29.99, 29.99, 29.99],
        name='Average'
    )
    chart_max = go.Bar(
        x = ['Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', \
            'Sep 13', 'Oct 13', 'Nov 13', 'Dec 13'],
        y = [29.82, 29.98, 29.99, 30.06, 30.07, 30.1, 30.02, 30.04, 30.03, 29.99, 30.06, 30.04],
        name = 'Max'
    )
    data = [chart_min, chart_avg, chart_max]
    layout = go.Layout(barmode = 'group')
    fig = go.Figure(data = data, layout = layout)
    plot_url = py.plot(fig, filename = 'Diesel 2013')
diesel_2013()
