import pandas as pd 
from itertools import cycle, islice 
import os
import numpy as np
import matplotlib.pyplot as plt

bills = []

bills_file = open('bills.csv') 
for line in bills_file: 
    bills.append(line.strip().split(',')) 
    for col in range(0,len(bills[-1])): 
        bills[-1][col] = bills[-1][col].strip()
 

########## TOTAL CREDITED/DEBITED BY YERA###############################################################
total_year = [] 
for bill in bills:
    if bill[6] == 'credit':
        tcred  = float(bill[5])
        tdeb   = 0
    else:
        tcred  = 0
        tdeb   = float(bill[5])
    
    found = 0
    if len(total_year) > 0:                
        for index in range(len(total_year)):
            if bill[2] == total_year[index]['year']: 
                found = 1
                total_year[index]['credit'] += tcred
                total_year[index]['debit']  += tdeb
                    
    if found == 0:
        total_year.append( {'year': bill[2] , 'credit': tcred , 'debit': tdeb} )        
 
tot_year_cred= {}     
tot_year_deb= {}  
for index in range(len(total_year)):
     tot_year_cred[total_year[index]['year']] =  total_year[index]['credit']
     tot_year_deb[total_year[index]['year']] =  total_year[index]['debit']
     
pd.DataFrame(tot_year_cred, index=['total']).plot(kind='bar' , title ='Total credited by year')   
pd.DataFrame(tot_year_deb, index=['total']).plot(kind='bar' , title ='Total debited by year')   
       
########## MOST POPULAR UTILITY COMPANY ################################################################
most_popular = {} 
for bill in bills:    
    if bill[0] in most_popular:
        most_popular[bill[0]] += 1
    else:
        most_popular[bill[0]] = 1

most_popular = sorted (most_popular.items() , reverse=True)

col1 = []
col2 = []
for company in most_popular:
    col1.append(company[0]) 
    col2.append(company[1])
    
## option 1    
#df = pd.DataFrame(list(zip(col1, col2)), 
#               columns =['Company', 'nr_bills']) 
#df 
#my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(df['nr_bills'])))
#df['nr_bills'].sort_index().plot.barh(color=my_colors, title= 'Most Popular utility company')

## option 2
x = col1
y = col2

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


#######################################################################################################




















