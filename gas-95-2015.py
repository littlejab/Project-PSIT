"""gas95 2015 graph"""
def graph_gas95_2015():
    """show graph of gas95 price in year 2015 by min, avg, max"""
    import plotly.plotly as py
    import plotly.graph_objs as go
    py.sign_in('littlejab', 'yblima8sc3')
    chart_min = go.Bar(
        x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
        y=[35.1, 35.09, 35.2, 33.66, 34.75, 35.42],
        name='Min'
    )

    chart_avg = go.Bar(
        x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
        y=[35.38, 35.44, 35.5, 33.95, 35.03, 35.73],
        name='Average'
    )

    chart_max = go.Bar(
        x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
        y=[35.55, 35.71, 35.69, 34.15, 35.2, 35.9],
        name='Max'
    )
    data = [chart_min, chart_avg, chart_max]
    layout = go.Layout(
        barmode='group'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Gasoline 95 2015')
graph_gas95_2015()
