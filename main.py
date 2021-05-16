import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df  = pd.read_csv("data.csv")
data = df["temp"].tolist()
#fig = ff.create_distplot([data], ["name"], show_hist=False)
#fig.show()
pm = statistics.mean(data)
ptsd = statistics.stdev(data)
#print(pm)

#print(ptsd)
def randomsetofmean():
    dataset = []
    for i in range(0, 100):
        randomindex = random.randint(0, len(data) - 1)
        value = data[randomindex]
        dataset.append(float(value))
    mean = statistics.mean(dataset)
    return mean

def showfig(meanlist):
    df = meanlist
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()
    fmean = statistics.mean(meanlist)
    print(fmean)
    fs = statistics.stdev(meanlist)
    print(fs)

def setup():
    meanlist = []
    for i in range(0, 1000):
        setmean = randomsetofmean()
        meanlist.append(setmean)
    showfig(meanlist)

setup()