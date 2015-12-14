"""Project PSIT gasohol 91"""
def gas91_2013to2015():
    """show bar graph of gasohol 91 in 2013-2015"""
    import plotly.plotly as py
    import plotly.graph_objs as go
    py.sign_in('littlejab', 'yblima8sc3')
    chart_min = go.Bar(x=['2012', '2013', '2014', '2015'], \
                       y=[35.88, 36.33, 36.53, 27.42], name='Min')

    chart_avg = go.Bar(x=['2012', '2013', '2014', '2015'], \
                       y=[35.94, 36.45, 36.55, 27.68], name='Average')

    chart_max = go.Bar(x=['2012', '2013', '2014', '2015'], \
                       y=[36.00, 36.50, 36.60, 27.74], name='Max')
    data = [chart_min, chart_avg, chart_max]
    layout = go.Layout(barmode='group')
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Gasohol91 All Year')

gas91_2013to2015()
