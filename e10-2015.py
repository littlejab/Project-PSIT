"""e10 2015 graph"""
def graph_e10_2015():
    """show graph of gas e10 price in year 2015 by min, avg, max"""
    import plotly.plotly as py
    import plotly.graph_objs as go
    py.sign_in('littlejab', 'yblima8sc3')
    chart_min = go.Bar(
        x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
        y=[28.04, 28.47, 29.35, 28.1, 29.08, 29.57],
        name='Min'
    )

    chart_avg = go.Bar(
        x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
        y=[28.04, 28.53, 29.36, 28.11, 29.08, 29.59],
        name='Average'
    )

    chart_max = go.Bar(
        x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],
        y=[28.04, 28.67, 29.39, 28.17, 29.13, 29.64],
        name='Max'
    )
    data = [chart_min, chart_avg, chart_max]
    layout = go.Layout(
        barmode='group'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='E10 2015')
graph_e10_2015()
