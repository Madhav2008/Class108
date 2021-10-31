import csv
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("HW.csv")

graph = ff.create_displot([df["Height(Inches)"].tolist()], ["Height Weight"], show_hist = False)
graph.show()

graph1 = ff.create_displot([df["Weight(Pounds)"].tolist()], ["Height Weight"], show_hist = False)
graph1.show()
