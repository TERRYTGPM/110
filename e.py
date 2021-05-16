import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("e.csv")
data = df["average"]

def function1():
    e = []
    for i in range(0, 100):
        randomindex = random.randint(0, len(data) - 1)
        value = data[randomindex]
        e.append(float(value))
    mean = statistics.mean(e)
    return mean

def function2(liste):
    mean  = liste
    fig = ff.create_distplot([mean], ['e'], show_hist=False)
    fig.show()

def setup():

    eee = []
    for i in range(0, 1000):
        ee = function1()
        eee.append(ee)

    function2(eee)

setup()