import plotly.figure_factory as ff
import statistics 
import pandas as pd
import random
import csv
import plotly.graph_objects as go
df=pd.read_csv("medium_data.csv")
data=df["id"].tolist()
totalmeanpopulation=statistics.mean(data)
print("population mean=",totalmeanpopulation)



def randommean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)  
    mean=statistics.mean(dataset)
    return mean
def showfig(meanlist):
    df=meanlist
    mean=statistics.mean(meanlist)
    print("mean of sampling ditribution",mean)
    
def setup():
    meanlist=[]
    for i in range(0,1000):
        means=randommean(100)
        meanlist.append(means)       
    showfig(meanlist)
setup()        
