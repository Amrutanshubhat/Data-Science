#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#to increase the plot area
plt.rcParams["figure.figsize"] = (23,12)
import random


# In[3]:


#realized P&L tab from the excel to be exported as CSV file.
mydata = pd.read_csv('oct22.csv')
capital_used = 1000
df = pd.DataFrame(mydata)
header=[]
#Data Cleaning - Remove NaN values and junk data.
for index,row in df.iterrows():
    if row[0] =="Scrip Name":
        header = row
        break
    df.drop(index,axis=0,inplace=True)
df = df.set_axis(header,axis='columns')
df.dropna(axis=1,how="all",inplace=True)


# In[4]:


#data analyzer - calculate profit / loss made on a single trading day.
group_by_date = df.groupby("Sell Date")["Realized P&L"]
profit_by_date=dict()
for date,profits in iter(group_by_date):
    try:
        profit_by_date[date] = sum(list(map(float,profits.tolist())))
    except ValueError:
        pass
final_profit = 0
number_of_days = 0
for key,val in profit_by_date.items():
    final_profit+=val
    number_of_days+=1


# In[5]:


#plot the graph
fig,ax = plt.subplots()
x_values = profit_by_date.keys()
y_values = profit_by_date.values()
left, width = 20, .5
bottom, height = 15, .5

bar_color = ['#007500' if v>0 else '#ff0000' for v in y_values]
y_pos = np.arange(len(x_values))
hbars = ax.barh(y_pos, y_values, align="center", color=bar_color)

ax.set_yticks(y_pos, labels=x_values, fontsize=15)
ax.invert_yaxis()
ax.set_title('P&L Summary for the month of XXXXXX 20XX',fontsize=23, weight='heavy')
ax.text(left,bottom,"Total Profit: %.2f"%(final_profit), fontsize = 20,ha="right")
ax.text(left,bottom+0.75,"Average Profits per traded days: {:.2f}".format(final_profit/number_of_days), fontsize = 20,ha="right")
if capital_used>0:
    ax.text(left,bottom+1.5,"ROI: {:.2f}%".format((final_profit*100)/capital_used), fontsize = 20,ha="right")
ax.bar_label(hbars,fmt="%.1f",label_type='edge',padding=5,fontsize=13, weight='bold')

plt.show()


# In[ ]:




