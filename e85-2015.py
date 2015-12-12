"""Oil price graph"""
import plotly.plotly as py
import plotly.graph_objs as go
def e85_2015():
    """E85 year 2015 price graph"""
    py.sign_in("littlejab", "yblima8sc3")
    chart_min = go.Bar(
        x = ["Jan 15", "Feb 15", "Mar 15", "Apr 15", "May 15", "Jun 15"],
        y = [21.98, 22.67, 23.48, 22.81, 23.19, 23.37],
        name = "Min"
    )

    chart_avg = go.Bar(
        x = ["Jan 15", "Feb 15", "Mar 15", "Apr 15", "May 15", "Jun 15"],
        y = [21.98, 22.67, 23.48, 22.81, 23.19, 23.37],
        name = "Average"
    )

    chart_max = go.Bar(
        x = ["Jan 15", "Feb 15", "Mar 15", "Apr 15", "May 15", "Jun 15"],
        y = [21.98, 22.67, 23.48, 22.81, 23.19, 23.37],
        name = "Max"
    )
    data = [chart_min, chart_avg, chart_max]
    layout = go.Layout(
        barmode = "group"
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename="E85 2015")

e85_2015()
