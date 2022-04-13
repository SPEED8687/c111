import pandas as pd
import random
import statistics as st
import plotly.figure_factory as ff
df=pd.read_csv('data.csv')
average=df['temp'].tolist()
finalData=[]
def sampling():
    data=[]
    for i in range(0,100):
        rp=random.randint(0,len(average)-1)
        rv=average[rp]
        data.append(rv)
    mean=st.mean(data)
    finalData.append(mean)

for i in range(0,1000):
    sampling()

graph=ff.create_distplot([finalData],['data'],show_hist=False)
graph.show()