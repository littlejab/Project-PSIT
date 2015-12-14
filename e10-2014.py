"""e10 2014 graph"""
def graph_e10_2014():
    """show graph of gas e10 price in year 2014 by min, avg, max"""
    import plotly.plotly as py
    import plotly.graph_objs as go
    py.sign_in('littlejab', 'yblima8sc3')
    chart_min = go.Bar(
        x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
        'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
        y=[40.53, 40.53, 40.76, 40.89, 40.97, 40.78, 40.62, 39.78, 37.8, 36.75, 34.99, 31.52],
        name='Min'
    )

    chart_avg = go.Bar(
        x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
            'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
        y=[40.66, 40.53, 40.76, 40.89, 41.04, 40.86, 40.66, 39.78, 37.8, 36.75, 35, 31.52],
        name='Average'
    )

    chart_max = go.Bar(
        x=['Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', \
            'Sep 14', 'Oct 14', 'Nov 14', 'Dec 14'],
        y=[40.71, 40.53, 40.76, 40.89, 41.16, 41.03, 40.76, 39.78, 37.8, 36.75, 35.05, 32.1],
        name='Max'
    )
    data = [chart_min, chart_avg, chart_max]
    layout = go.Layout(
        barmode='group'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='E10 2014')
graph_e10_2014()
