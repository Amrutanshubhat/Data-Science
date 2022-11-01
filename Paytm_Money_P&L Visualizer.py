#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
#to increase the plot area
plt.rcParams["figure.figsize"] = (15,8)
import random


# In[28]:


#Inport csv / excel file - Rename the file to 'plstatement'
try:
    mydata = pd.read_csv('plstatement.csv')
except FileNotFoundError:
    mydata = pd.read_excel('plstatement.xls',sheet_name=1)
except:
    print("Something went wrong")
capital_used = 200000
df = pd.DataFrame(mydata)
header=[]
#Data Cleaning - Remove NaN values and junk data.
for index,row in df.iterrows():
    if 'Realized P&L' in row.to_list():
        header = row
        break
    df.drop(index,axis=0,inplace=True)
df = df.set_axis(header,axis='columns')
df.dropna(axis=1,how="all",inplace=True)


# In[29]:


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


# In[30]:


#plot the graph
fig,ax = plt.subplots()
x_values = profit_by_date.keys()
y_values = profit_by_date.values()

bar_color = ['#007500' if v>0 else '#ff0000' for v in y_values]
y_pos = np.arange(len(x_values))
hbars = ax.bar(y_pos, y_values, align="center", color=bar_color)

ax.set_xticks(y_pos, labels=x_values, fontsize=8,rotation=90)

ax.set_title('P&L Summary for the month of XXX',fontsize=18, weight='heavy')
ax.bar_label(hbars,fmt="%.1f",label_type='edge',padding=5,fontsize=10, weight='bold')


props = dict(boxstyle='round', facecolor='#7EC8E3', alpha=0.5)
textstr = '\n'.join((
    'Total Profit=%.2f' % (final_profit),
    'Avg. Profit per Day=%.2f' % ((final_profit/number_of_days)),
    "ROI: {:.2f}%".format((final_profit*100)/capital_used)))


# place a text box in upper left in axes coords
ax.text(0.25, 0.15, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)


plt.show()


# In[ ]:





# In[ ]:




