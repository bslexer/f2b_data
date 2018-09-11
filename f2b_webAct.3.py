# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:42:08 2018

@author: Brian Schleckser
@Requested by: Melissa Pearce

Regarding: Free 2B Foods, Web Sales.
           Observing sales , shipping, and related connections.
           
Working version, with hopes to add user functionality, create hands-off usage.

"""

import pandas as pd
import collections as co
import os

#path info
path = r'C:\Users\Brian Schleckser\Documents\f2b\MP_webAct'
os.listdir(path)

readOut = 'LONG'
start = pd.to_datetime('2018-2-23')
#loop uses less than, so pick next day to capture up until midnight on that last wanted day
end = pd.to_datetime('2018-9-4')

#file used should be grouped by SO.NUM, product column only included to identify FRT
print " What file?"
salesDF = pd.read_csv(path + '\_fishBowl_export sale items.csv', usecols=['num', 'synthName', 'keyDate', 'product','qty', 'Ordered'])[['num', 'synthName', 'keyDate', 'product','qty', 'Ordered']]

salesDF['keyDate'] =  pd.to_datetime(salesDF['keyDate'])
salesDF = salesDF.dropna()
for index, row in salesDF.iterrows():
    #print salesDF['keyDate'][index]
    if salesDF['keyDate'][index] < start or salesDF['keyDate'][index] > end:
        salesDF = salesDF.drop(index)
    

#for loop to clean / normalize data...drawn from the f2b fishbowl so, and soitems tables.
for index, row in salesDF.iterrows(): 
    #print row
    #for each num, if its not a digit, get rid of it, aftward, convert to int.
    salesDF['num'] = salesDF['num'].replace('\D', '', regex=True).astype(int)
    #just messing with the date format.
    #salesDF['keyDate'] = salesDF['keyDate'].str.replace('/', '_')
    #cutting out un-needed product info.
    salesDF['product'] = salesDF['product'].str.slice(0, 6, 1)
    salesDF['product'] = salesDF['product'].astype('|S') 
    #converting quantity to a simple int.
    salesDF['Ordered'] = salesDF['Ordered'].astype(float)

#print salesDF
print (salesDF.dtypes)


#########################
#converting dataframe to tupel groups for easier iterating.
orderTuples = list(salesDF.itertuples(index=False))
custShip = quantCustShip = totalSales = quantSales = 0
saleOver49 = 0
saleOver29Below49 = 0
smallSale = 0
orderList = []



#month counting
#total sales by month counting
monthDict = {}
monthSaleDict = {}
monthItemDict = {}
monthBracketDict = {}

for order in orderTuples:
    if order[3][0:3] != "FRT": 

        # orders by month
        if order[2].month not in monthDict:
            monthDict[order[2].month] = 1
        elif order[2].month in monthDict:
            monthDict[order[2].month] += 1
            
        # sales by month
        if order[2].month not in monthSaleDict:
            monthSaleDict[order[2].month] = order[5]
        elif order[2].month in monthSaleDict:
            monthSaleDict[order[2].month] = monthSaleDict[order[2].month] + order[5]
            
        # items by month
        if order[2].month not in monthItemDict:
            monthItemDict[order[2].month] = order[4]
        elif order[2].month in monthSaleDict:
            monthItemDict[order[2].month] = monthItemDict[order[2].month] + order[4]        
###Tested /\
            
        
        
        
        
        
        
        # sale bracket by month
#Need to rollup by order for this

        if order[5] > 49:
            saleOver49 += 1
        elif order[5] > 29 and order[5] < 49:
            saleOver29Below49 += 1
        else:
            smallSale += 1

        '''
        if order[2].month not in monthBracketDict:
            monthBracketDict[order[2].month] = order[4]
        elif order[2].month in monthSaleDict:
            monthItemDict[order[2].month] = monthItemDict[order[2].month] + order[4]
        '''

Total = df['MyColumn'].sum()



































#month counting
for order in orderTuples:
    print order[2].month
    saleMonth = order[2].month
    
    if order[0] not in 
    
    
    if order[3][0:3] != 'FRT':
        totalSales = totalSales + order[5]
        if int(order[0]) not in orderList:
            orderList.append(int(order[0]))
            quantSales += 1
        print quantSales, order[0]
        #print 'yep'
    else:
        custShip = custShip + order[5]
        quantCustShip += 1
        
    if order[5] > 29 and order[3][0:3] != 'FRT':
        saleOver29 += 1
    if order[5] > 49 and order[3][0:3] != 'FRT':
        saleOver49 += 1
    if order[5] < 29 and order[3][0:3] != 'FRT':
        #print order[2]
        smallSale += 1
 

    
print "customer shipping", custShip
print "total sales", totalSales
print "quantity sales", quantSales
print "over 49:", saleOver49, "over 29:", saleOver29, "low sale:", smallSale

avgOrder = perOver49 = perOver29 = perCustPayShip = 0.0

avgOrder = totalSales / quantSales
perOver49 = (saleOver49 / float(quantSales) * 100)
perOver29 = (saleOver29 / float(quantSales) * 100)
perCustPayShip = (quantCustShip / float(quantSales) * 100)

print "avg:", avgOrder
print "Percent orders Over 49", perOver49
print "Percent orders over 29", perOver29
print "Percent orders where customer paid for shipping", perCustPayShip
    '''
itemDict = {}
for p in salesDF['product']:
    if p[:-3] != 'FRT':
        if p not in itemDict:
            itemDict[p] = 1 
        elif p in itemDict:
            itemDict[p] += 1
           

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
    
    
#FM01D01, dark1, 1 mc = 6 Z01D01 items
    FM01D01 = itemDict['Z01D01'] / 6
#FM01D02, 1 cup mint, 1 mc = 6 Z01D02
    FM01D02 = itemDict['Z01D02'] / 6
     
    
    
    
    
    
    
    
manuDict = {}
#final product key = mastercase, division factor
#dark1
manuDict['Z01D01'] = ('FM01D01', 6)         
#rice1
manuDict['Z01R01'] = ('FM01R01', 6) 
#dark2
manuDict['Z02D01'] = ('FM02D01', 6) 
#mint2
manuDict['Z02D02'] = ('FM02D02', 6)
#rice2
manuDict['Z02R01'] = ('FM02R01', 6) 
#cran3
manuDict['Z04D12'] = ('FM04D02', 3) 
#cran6
manuDict['Z04D02'] = ('FM04D02', 1) 
#blue3
manuDict['Z04R11'] = ('FM04R01', 3) 
#blue6
manuDict['Z04R01'] = ('FM04R01', 1) 
manuDict[FM01D01] = ('Z01D01', 6) 
manuDict[FM01D01] = ('Z01D01', 6) 
manuDict[FM01D01] = ('Z01D01', 6) 
            
 '''           
            
  



          
'''            
#cherry singles
manuDict['Z03D01'] = ('FM03D03', 10)
#cherry 5pack 
manuDict['Z03D13'] = ('FM03D03', 10)
#rice singles 
manuDict['Z03R01'] = ('FM03R01', 10)           
'''            
            
            
            
            
#bring in angela's shipping report    
    
    
    '''
###########################
#converting the dictionary into a dataframe to prepare for export. Combo and frequency are column names.
#sorting frequency values by descending.\\
resultDF = pd.DataFrame.from_dict(comboDict, orient= 'index').reset_index()
resultDF = pd.DataFrame(resultDF.values, columns = ['combo','frequency','description','price'])

resultDF = resultDF.sort_values(by='frequency', ascending=False)



# Create a Pandas Excel writer using XlsxWriter as the engine. https://xlsxwriter.readthedocs.io/working_with_pandas.html
writer = pd.ExcelWriter('F2B_webSale_act_6_16_7_9.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
if readOut == 'LONG':
    resultDF.to_excel(writer,index=False, sheet_name=' Detailed Results')
else:
    resultDF.to_excel(writer,index=False, sheet_name=' Simple Results')
    
salesDF.to_excel(writer,index=False, sheet_name='Beginning Data')

# Close the Pandas Excel writer and output the Excel file.
writer.save()