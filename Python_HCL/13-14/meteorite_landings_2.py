import matplotlib.pyplot as plt
import pandas
import datetime

data = pandas.read_csv('Meteorite_landings.csv')
data = data.dropna(how='any')

groups = data.groupby(['recclass']).size()
plot = groups.plot.pie()
# print(groups)
print(plot)

groups = data.loc[[datetime.datetime.strptime(date, '%m/%d/%Y %H:%M:%S %p').year for date in data['year']]>=1900].groupby(['year']).size()
print(groups)