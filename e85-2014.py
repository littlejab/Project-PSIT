"""Oil price graph"""
import plotly.plotly as py
import plotly.graph_objs as go
def e85_2014():
    """E85 year 2014 price graph"""
    py.sign_in("littlejab", "yblima8sc3")
    chart_min = go.Bar(
        x = ["Jan 14", "Feb 14", "Mar 14", "Apr 14", "May 14", "Jun 14", "Jul 14", "Aug 14", \
            "Sep 14", "Oct 14", "Nov 14", "Dec 14"],
        y = [24.45, 24.38, 24.52, 24.57, 24.70, 24.61, 24.51, 24.28, 24.28, 23.48, 22.88, 22.65],
        name = "Min"
    )

    chart_avg = go.Bar(
     x = ["Jan 14", "Feb 14", "Mar 14", "Apr 14", "May 14", "Jun 14", "Jul 14", "Aug 14", \
        "Sep 14", "Oct 14", "Nov 14", "Dec 14"],
     y = [24.45, 24.38, 24.52, 24.56, 24.67, 24.61, 24.51, 24.28, 24.28, 23.48, 22.88, 22.65],
     name = "Average"
    )

    chart_max = go.Bar(
        x = ["Jan 14", "Feb 14", "Mar 14", "Apr 14", "May 14", "Jun 14", "Jul 14", "Aug 14", \
            "Sep 14", "Oct 14", "Nov 14", "Dec 14"],
        y = [24.45, 24.38, 24.38, 24.52, 24.57, 24.70, 24.61, 24.51, 24.28, 23.48, 22.88, 22.65],
        name = "Max"
    )
    data = [chart_min, chart_avg, chart_max]
    layout = go.Layout(
        barmode = "group"
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename = "E85 2014")

e85_2014()
