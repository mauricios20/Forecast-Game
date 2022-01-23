import yfinance as yf
import os
import pandas as pd
import numpy as np


#  #################### Import Tesla Stock Info ############################
tsla = yf.Ticker("TSLA")

# get historical market data
hist = tsla.history(period="5d")
print(hist['Close'])

ave = round(hist['Close'].mean(), 2)
high = round(hist['Close'].max(), 2)
low = round(hist['Close'].min(), 2)

print('Average: {0:}, High: {1:}, Low: {2:}'.format(ave, high, low))

#  #################### Read and Clean Data ################################
path = '/Users/mau/Dropbox/Mac/Documents/Econ 103/Spring 2022/Forecast Game/Section 1003'
os.chdir(path)

Generaldata = pd.read_csv('Week 1 - Introduction_January 22, 2022_14.56.csv', header=0)
data = Generaldata[['QID1_6', 'Q4', 'Q5', 'Q6']]
data = data.drop([0, 1])
data = data.dropna()
print(data.info())

data['Q4'] = data['Q4'].str.replace(r"[a-zA-Z$,]",'')
data['Q4'] = data['Q4'].astype(float)

data['Q5'] = data['Q5'].str.replace(r"[a-zA-Z$,]",'')
data['Q5'] = data['Q5'].astype(float)

data['Q6'] = data['Q6'].str.replace(r"[a-zA-Z$,]",'')
data['Q6'] = data['Q6'].astype(float)


#  #################### Assign Points  ####################################
minave = ave-(ave*.05)
maxave = ave+(ave*.05)

minhigh = high-(high*.05)
maxhigh = high+(high*.05)

minlow = low-(low*.05)
maxlow = low+(low*.05)



# print(minave)
# print(maxave)
#
#
# print(minhigh)
# print(maxhigh)
#
#
# print(minlow)
# print(maxlow)



list = []
for value in data['Q4']:
    if minave <= value <= maxave:
        print(value, 'ave prediction is present in the range.')
        list.append(3)
    else:
        print(value, 'ave prediction is not present in the range.')
        list.append(0)

for value in data['Q5']:
    if minhigh <= value <= maxhigh:
        print(value, 'high prediction is present in the range.')
    else:
        print(value, 'high prediction is not present in the range.')

for value in data['Q6']:
    if minlow <= value <= maxlow:
        print(value, 'low prediction is present in the range.')
    else:
        print(value, 'low prediction is not present in the range.')

print(len(list))
data['Ave Score'] = list
print(data)
