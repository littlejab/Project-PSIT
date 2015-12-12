"""Oil price graph"""
import plotly.plotly as py
import plotly.graph_objs as go
def e85_2013():
    """E85 year 2013 price graph"""
    py.sign_in("littlejab", "yblima8sc3")
    chart_min = go.Bar(
        x = ["Jan 13", "Feb 13", "Mar 13", "Apr 13", "May 13", "Jun 13", "Jul 13", "Aug 13", \
            "Sep 13", "Oct 13", "Nov 13", "Dec 13"],
        y = [21.83, 22.76, 22.91, 21.88, 21.82, 22.66, 23.57, 23.19, 23.27, 22.98, 23.19, 23.78],
        name = "Min"
    )

    chart_avg = go.Bar(
        x = ["Jan 13", "Feb 13", "Mar 13", "Apr 13", "May 13", "Jun 13", "Jul 13", "Aug 13", \
            "Sep 13", "Oct 13", "Nov 13", "Dec 13"],
        y = [21.83, 22.84, 22.91, 21.88, 21.82, 22.66, 23.57, 23.19, 23.27, 22.98, 23.19, 23.78],
        name = "Average"
    )

    chart_max = go.Bar(
        x = ["Jan 13", "Feb 13", "Mar 13", "Apr 13", "May 13", "Jun 13", "Jul 13", "Aug 13", \
            "Sep 13", "Oct 13", "Nov 13", "Dec 13"],
        y = [21.83, 22.89, 22.91, 21.88, 21.82, 22.66, 23.57, 23.19, 23.27, 22.98, 23.19, 23.78],
        name = "Max"
    )
    data = [chart_min, chart_avg, chart_max]
    layout = go.Layout(
        barmode = "group"
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename = "E85 2013")

e85_2013()
