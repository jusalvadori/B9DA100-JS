from bill_management import bill_management

import pandas as pd 
from itertools import cycle, islice 
import os
import numpy as np
import matplotlib.pyplot as plt

bill_management = bill_management()
bill_management.read_bills('bills.csv')  # read the initial file
 
########## TOTAL CREDITED/DEBITED BY YEAR ###############################################################

total_year = bill_management.total_by_year()
    
tot_year_cred= {}     
tot_year_deb= {}  
for index in range(len(total_year)):
     tot_year_cred[total_year[index]['year']] =  total_year[index]['credit']
     tot_year_deb[total_year[index]['year']] =  total_year[index]['debit']
     
pd.DataFrame(tot_year_cred, index=['total']).plot(kind='bar' , title ='Total credited by year')   
pd.DataFrame(tot_year_deb, index=['total']).plot(kind='bar' , title ='Total debited by year')   
       
########## MOST POPULAR UTILITY COMPANY ################################################################
most_popular = bill_management.most_popular_company() 

x = []
y = []
for company in most_popular:
    x.append(company[0]) 
    y.append(company[1])
    

fig, ax = plt.subplots()    
width = 0.75 # the width of the bars 
ind = np.arange(len(y))  # the x locations for the groups
my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(y)))
ax.barh(ind, y, width, color= my_colors)
ax.set_yticks(ind+width/2)
ax.set_yticklabels(x, minor=False)
plt.title('Most Popular utility company')
plt.xlabel('Number of bills')
plt.ylabel('Utility company')     
#Plot the data:
plt.savefig(os.path.join('test.png'), dpi=300, format='png', bbox_inches='tight') # use format='svg' or 'pdf' for vectorial pictures


#################### HIGHEST AMOUNT ################################################################

# select credit amounts
sorted_by = bill_management.highest_amount('credit') 
sorted_by_credit = sorted(sorted_by, key=lambda tup: float(tup[5]))
col1 = []
for bill in sorted_by_credit:
    col1.append(float(bill[5])) 

# select debit amounts
sorted_by = bill_management.highest_amount('debit') 
sorted_by_debit = sorted(sorted_by, key=lambda tup: float(tup[5]))
col2 = []
for bill in sorted_by_debit:
    col2.append(float(bill[5])) 

df = pd.DataFrame(list(zip(col1, col2)), 
               columns =['credit', 'debit']) 
    
# get columns to plot
columns = df.columns
# create x data
x_data = range(0, df.shape[0])
# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(x_data, df[column], label=column)
# set title and legend
ax.set_title('Highest amount')
ax.legend()

################# AVERAGE SPENT PER YEAR/MONTH #####################################################

# average spent per period of time
avg_per_period  = bill_management.average_spent_per_period('')

x = []
y = []
for row in avg_per_period.iterrows():
    x.append(row[0][0]+'/'+row[0][1]) 
    y.append(row[1][0])
    

fig, ax = plt.subplots()    
width = 0.75 # the width of the bars 
ind = np.arange(len(y))  # the x locations for the groups
my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(y)))
ax.barh(ind, y, width, color= my_colors)
ax.set_yticks(ind+width/2)
ax.set_yticklabels(x, minor=False)
plt.title('Average spent per year/month (debit)')
plt.xlabel('Amount (EUR)')
plt.ylabel('Year/Month')     
#Plot the data:
plt.savefig(os.path.join('test.png'), dpi=300, format='png', bbox_inches='tight') # use format='svg' or 'pdf' for vectorial pictures

######################### AMOUNT SPENT PER CUSTOMER ################################################

# select John Smyth bills 
result = [group for group in bill_management.bills if group[1] == 'John Smyth']
# order the result above by the amount in the reverse order
sorted_by = sorted(result, key=lambda tup: (tup[2],tup[3],tup[4]))
col1 = []
for bill in sorted_by:
    col1.append(float(bill[5])) 

# select Missy May bills
result = [group for group in bill_management.bills if group[1] == 'Missy May']
# order the result above by the amount in the reverse order
sorted_by = sorted(result, key=lambda tup: (tup[2],tup[3],tup[4]))
col2 = []
for bill in sorted_by:
    col2.append(float(bill[5])) 
    
    
# select Susie Sue bills
result = [group for group in bill_management.bills if group[1] == 'Susie Sue']
# order the result above by the amount in the reverse order
sorted_by = sorted(result, key=lambda tup: (tup[2],tup[3],tup[4]))
col3 = []
for bill in sorted_by:
    col3.append(float(bill[5])) 

df = pd.DataFrame(list(zip(col1, col2, col3)), 
               columns =['John Smyth', 'Missy May', 'Susie Sue']) 
    
# get columns to plot
columns = df.columns
# create x data
x_data = range(0, df.shape[0])
# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(x_data, df[column], label=column)
# set title and legend
ax.set_title('Amount spent per customer')
ax.legend()


###################################################################################################

df.plot.hist(subplots=True, layout=(2,2), figsize=(10, 10), bins=20, title ='Amount spent per customer')
