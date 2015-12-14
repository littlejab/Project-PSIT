"""Project PSIT gasohol 91"""
def gas91_2015():
    """show bar graph of gasohol 91 in 2015"""
    import plotly.plotly as py
    import plotly.graph_objs as go
    py.sign_in('littlejab', 'yblima8sc3')
    chart_min = go.Bar(x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],\
                       y=[26.57, 27.15, 28.03, 27.23, 26.81, 28.75],name='Min')
    chart_avg = go.Bar(x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],\
                       y=[26.57, 27.18, 28.04, 27.24, 28.27, 28.76],name='Average')
    chart_max = go.Bar(x=['Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15'],\
                       y=[26.57, 27.35, 28.07, 27.30, 28.31, 28.82],name='Max')
    data = [chart_min, chart_avg, chart_max]
    layout = go.Layout(barmode='group')
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Gasohol91 2015')

gas91_2015()
