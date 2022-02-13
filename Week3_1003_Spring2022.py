import yfinance as yf
import os
import pandas as pd



#  #################### Import Tesla Stock Info ############################
tsla = yf.Ticker("TSLA")

# get historical market data
hist = tsla.history(start="2022-02-07", end="2022-02-12")
print(hist['Close'])

ave = round(hist['Close'].mean(), 2)
high = round(hist['Close'].max(), 2)
low = round(hist['Close'].min(), 2)

print('Average: {0:}, High: {1:}, Low: {2:}'.format(ave, high, low))

#  #################### Read and Clean Data ################################
path = '/Users/mau/Dropbox/Mac/Documents/Econ 103/Spring 2022/Forecast Game/Section 1003'
os.chdir(path)

Generaldata = pd.read_csv('Week 3_1003.csv', header=0)
data1 = Generaldata[['Q8_1', 'Q4', 'Q5', 'Q6']]
data1 = data1.drop([0, 1])
data1 = data1.dropna()


data1['Q4'] = data1['Q4'].str.replace(r"[a-zA-Z$,]",'')
data1['Q4'] = data1['Q4'].astype(float)

data1['Q5'] = data1['Q5'].str.replace(r"[a-zA-Z$,]",'')
data1['Q5'] = data1['Q5'].astype(float)

data1['Q6'] = data1['Q6'].str.replace(r"[a-zA-Z$,]",'')
data1['Q6'] = data1['Q6'].astype(float)
data1.rename(columns={"Q8_1": "Username", "Q4": "Average", "Q5": "High", "Q6": "Low"}, inplace=True)


gmakedtf = pd.read_csv('Week 3_Makeup.csv', header=0)
data2 = gmakedtf[['QID1_6', 'Q4', 'Q5', 'Q6']]
data2 = data2.drop([0, 1])
data2 = data2.dropna()

data2['Q4'] = data2['Q4'].str.replace(r"[a-zA-Z$,]",'')
data2['Q4'] = data2['Q4'].astype(float)

data2['Q5'] = data2['Q5'].str.replace(r"[a-zA-Z$,]",'')
data2['Q5'] = data2['Q5'].astype(float)

data2['Q6'] = data2['Q6'].str.replace(r"[a-zA-Z$,]",'')
data2['Q6'] = data2['Q6'].astype(float)

data2.rename(columns={"QID1_6": "Username", "Q4": "Average", "Q5":"High", "Q6":"Low"}, inplace=True)
data = pd.concat([data1, data2]).drop_duplicates(subset=['Username'])
print(data.info())
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
for value in data['Average']:
    if minave <= value <= maxave:
        # print(value, 'ave prediction is present in the range.')
        list.append(3)
    else:
        # print(value, 'ave prediction is not present in the range.')
        list.append(0)
list1 = []
for value in data['High']:
    if minhigh <= value <= maxhigh:
        # print(value, 'high prediction is present in the range.')
        list1.append(2)
    else:
        # print(value, 'high prediction is not present in the range.')
        list1.append(0)

list2 = []
for value in data['Low']:
    if minlow <= value <= maxlow:
        # print(value, 'low prediction is present in the range.')
        list2.append(2)
    else:
        # print(value, 'low prediction is not present in the range.')
        list2.append(0)
lt = []
for value in data['Average']:
    diffa = round(value-ave, 0)
    lt.append(diffa)


lt1 = []
for value in data['High']:
    diffh = round(value-high, 0)
    lt1.append(diffh)


lt2 = []
for value in data['Low']:
    diffl = round(value-low, 0)
    lt2.append(diffl)

#
# print(len(lt))
print(len(list))
data['Ave Score'] = list
data['High Score'] = list1
data['Low Score'] = list2
data['Total'] = data['Ave Score']+data['High Score']+data['Low Score']

# #### CHANGE THE WEEK #######

data['Ave Accuracy'] = lt
data['High Accuracy'] = lt1
data['Low Accuracy'] = lt2
data['Overall Accuracy'] = data['Ave Accuracy']+data['High Accuracy']+data['Low Accuracy']
data['Absolute Value'] = abs(data['Overall Accuracy'])
data['Week'] = 'Week 3'
sorteddata = data.sort_values(by='Total', ascending=False)
print(sorteddata)
sorteddata.to_csv('Results_Week3_1003.csv', index=False)
