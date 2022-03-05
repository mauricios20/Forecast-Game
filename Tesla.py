import yfinance as yf
import os
import pandas as pd


#  #################### Import Tesla Stock Info ############################
tsla = yf.Ticker("TSLA")

# get historical market data
hist = tsla.history(start="2022-01-24", end="2022-01-29")
print(hist['Close'])

ave = round(hist['Close'].mean(), 2)
high = round(hist['Close'].max(), 2)
low = round(hist['Close'].min(), 2)
print('Week 1 - Average: {0:}, High: {1:}, Low: {2:}'.format(ave, high, low))

####### Week 2 #######
hist = tsla.history(start="2022-01-31", end="2022-02-05")
print(hist['Close'])

ave2 = round(hist['Close'].mean(), 2)
high2 = round(hist['Close'].max(), 2)
low2 = round(hist['Close'].min(), 2)
print('Week 2 - Average: {0:}, High: {1:}, Low: {2:}'.format(ave2, high2, low2))
#  #################### Read and Clean Data ################################
lst = [['High', high, high2], ['Average', ave, ave2],
       ['Low', low, low2]]

####### Week 3 #######

hist = tsla.history(start="2022-02-07", end="2022-02-12")
print(hist['Close'])

ave3 = round(hist['Close'].mean(), 2)
high3 = round(hist['Close'].max(), 2)
low3 = round(hist['Close'].min(), 2)
print('Week 3 - Average: {0:}, High: {1:}, Low: {2:}'.format(ave3, high3, low3))

####### Week 4 #######

hist = tsla.history(start="2022-02-14", end="2022-02-19")
print(hist['Close'])

ave4 = round(hist['Close'].mean(), 2)
high4 = round(hist['Close'].max(), 2)
low4 = round(hist['Close'].min(), 2)

print('Week 4 - Average: {0:}, High: {1:}, Low: {2:}'.format(ave4, high4, low4))

####### Week 5 #######

hist = tsla.history(start="2022-02-21", end="2022-02-26")
print(hist['Close'])

ave5 = round(hist['Close'].mean(), 2)
high5 = round(hist['Close'].max(), 2)
low5 = round(hist['Close'].min(), 2)

print('Week 5 - Average: {0:}, High: {1:}, Low: {2:}'.format(ave5, high5, low5))

####### Week 6 #######

hist = tsla.history(start="2022-02-28", end="2022-03-05")
print(hist['Close'])

ave6 = round(hist['Close'].mean(), 2)
high6 = round(hist['Close'].max(), 2)
low6 = round(hist['Close'].min(), 2)

print('Week 6 - Average: {0:}, High: {1:}, Low: {2:}'.format(ave6, high6, low6))

#  #################### Read and Clean Data ################################
lst = [['High', high, high2, high3, high4, high5, high6], ['Average', ave, ave2, ave3, ave4, ave5, ave6],
       ['Low', low, low2, low3, low4, low5, low6]]
tesladtf = pd.DataFrame(lst, columns=['Value', 'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'])
print(tesladtf)

path = '/Users/mau/Dropbox/Mac/Documents/Econ 103/Spring 2022/Forecast Game'
os.chdir(path)

#  #################### Assign Points  ####################################
tesladtf.to_csv('Tesla.csv', index=False)
