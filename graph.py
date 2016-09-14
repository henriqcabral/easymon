import plotly
from plotly.graph_objs import Scatter, Layout

class graph(object):
    def __init__(self, graph_title, b):
        self.graph_title = graph_title

    def ploty_cpu_graph(self):
        plotly.offline.plot({
        "data": [
            Scatter(x=[1, 2, 3, 4], y=[4, 1, 3, 7])
        ],
        "layout": Layout(
            title="hello world"
        )
        })
    def olha():
        print("Olha eu ai")

