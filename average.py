import pandas as pd
import plotly.figure_factory as ff
df=pd.read_csv('data.csv')
average=df['temp'].tolist()
graph=ff.create_distplot([average],['data'],show_hist=False)
graph.show()