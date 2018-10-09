# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:29:10 2017

@author: divya
"""
#This code consists of violations based on date-wise, day wise and time wise.
#Imorting pandas, numpy, datetime and matplotlib as required to analyze the csv file.
import pandas as pd
import numpy as np
import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
datetime.datetime.strptime
df = pd.read_csv('denton_traffic_violations.csv')
file1 = pd.read_csv("denton_traffic_violations.csv", parse_dates = [0,1], infer_datetime_format = True)
file = file1.rename(columns = {'ct_viol_date':'Datetime'})
temp = pd.DatetimeIndex(file['Datetime'])
file['Date'] = temp.date
file['Time'] = temp.time
del file['Datetime']
df['Date'] = file['Date']
df['Time'] = file['Time']
df_sorted = df[['cit_citation_no','Date','Time','nam_r_city','nam_r_zip1']]
df_sorted.to_csv('denton_1.csv')
#The denton_1.csv consists of only specific columns listed with the above mentioned headers.
df_new = pd.read_csv('denton_1.csv')
df_new['Time'] = pd.to_datetime(df_new['Time'].astype(str))
df_city_filtered = df_new[(df_new['nam_r_city'].str.contains("DENTON"))]
df_date_filtered = df_city_filtered[(df_city_filtered['Date'] >= '2016-12-01') & (df_city_filtered['Date'] <= '2016-12-31')]
dates = (df_date_filtered.Date.unique())
(dates.sort(axis = -1, kind = 'quicksort', order = None))
print ("THIS IS THE OUTPUT FOR NUMBER OF VIOLATIONS BASED ON EVERY SINGLE DATE IN THE MONTH OF DECEMBER IN THE CITY OF DENTON.")
print ("\n")
for item in dates:
    df_dates = df_date_filtered[(df_date_filtered['Date'] == item)]
    print ("The number of violations on", item.strip(), "are:", len(df_dates))
#Plotting the number of violations based on dates.
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
y = np.array([34,13,5,4,28,40,14,15,18,7,6,14,42,17,21,18,5,9,18,13,21,28,18,3,1,4,9,20,22])
my_xticks = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29']
fig = plt.figure()
plt.title('Violations based on dates' )
plt.xlabel('Dates')
plt.ylabel('Number of violations')
plt.xticks (x, my_xticks)
plt.plot(x, y, 'b*')
plt.plot(x,y)
plt.show()
fig.savefig('Date_wise_violations.jpg')
print ("*****************************************************************************")


print (" ")
print ("THIS IS THE OUTPUT FOR NUMBER OF VIOLATIONS BASED ON DAY WISE IN THE MONTH OF DECEMBER.")
print ("\n")
df_date_filtered = pd.read_csv("denton_1.csv", parse_dates = [['Date','Time']])
days = df_date_filtered.Date_Time.dt.weekday_name
df_date_filtered['Day_names'] = days
df_date_filtered['Date'] = file['Date']
df_date_filtered['Date'] = pd.to_datetime(df_date_filtered['Date'].astype(str))
df_days = df_date_filtered[(df_date_filtered['nam_r_city'].str.contains("DENTON"))]
df_days_date = df_days[(df_days['Date'] >= '2016-12-01') & (df_days['Date'] <= '2016-12-31')]
Days = df_days_date.Day_names.unique()
(Days.sort(axis = -1, kind = 'quicksort', order = None))
for item1 in Days:
    df_days_filtered = df_days_date[(df_days_date['Day_names'] == item1)]
    print ("The number of violations on", item1, "are:", len(df_days_filtered))
#Plotting the number of violations based on days in the week..
x1 = np.array([1,2,3,4,5,6,7])
y1 = np.array([20,64,105,72,130,67,20])
my_xticks = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
fig = plt.figure()
plt.title('Violations based on days in the week' )
plt.xlabel('Days')
plt.ylabel('Number of violations')
plt.xticks (x1, my_xticks)
plt.plot(x1, y1, 'b*')
plt.plot(x1,y1)
plt.show()
fig.savefig('Day_wise_violations.jpg')
print (" ")
print ("***************************************************************************")

print ("THIS IS THE OUTPUT FOR NUMBER OF VIOLATIONS BASED ON HOURS IN A DAY IN THE ENTIRE MONTH.")
df_days_date['Hours'] = df_days_date.Date_Time.dt.hour
df_mhours = df_days_date[(df_days_date['Hours'] >= 6) & (df_days_date['Hours'] <= 12)]
print ("The total number of violations from 6 to 12 are:", len(df_mhours))
Morning_hours = df_mhours.Hours.unique()
(Morning_hours.sort(axis = -1, kind = 'quicksort', order = None))
for item_1 in Morning_hours:
    df_mh = df_mhours[(df_mhours['Hours'] == item_1)]
    print ("The number of violations in the Morning hours of", item_1, " are:", len(df_mh))
 
print (" ")
df_midhours = df_days_date[(df_days_date['Hours'] >= 13) & (df_days_date['Hours'] <= 19)]
print ("The total number of violations from 13 to 19 are:", len(df_midhours))
Midday_hours = df_midhours.Hours.unique()
(Midday_hours.sort(axis = -1, kind = 'quicksort', order = None))
for item_2 in Midday_hours:
    df_midh = df_midhours[(df_midhours['Hours'] == item_2)]
    print ("The number of violations in the Mid-day hours of", item_2, " are:", len(df_midh))

print (" ")
df_nighthours = df_days_date[(df_days_date['Hours'] >= 20) & (df_days_date['Hours'] <= 23)]
print ("The total number of violations from 20 to 23 are:", len(df_nighthours))
Night_hours = df_nighthours.Hours.unique()
(Night_hours.sort(axis = -1, kind = 'quicksort', order = None))
for item_3 in Night_hours:
    df_nh = df_nighthours[(df_nighthours['Hours'] == item_3)]
    print ("The number of violations in the Night hours of", item_3, " are:", len(df_nh))

print (" ")
df_earlyhours = df_days_date[(df_days_date['Hours'] >= 0) & (df_days_date['Hours'] <= 5)]
print ("The total number of violations from 0 to 5 are:", len(df_earlyhours))
Early_hours = df_earlyhours.Hours.unique()
(Early_hours.sort(axis = -1, kind = 'quicksort', order = None))
for item_4 in Early_hours:
    df_eh = df_earlyhours[(df_earlyhours['Hours'] == item_4)]
    print ("The number of violations in the Early hours within", item_4, " are:", len(df_eh))
#Plotting the number of violations based on time.
x2 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
y2 = np.array([5,2,3,1,1,4,7,21,30,28,23,39,38,56,44,32,24,17,21,18,20,8,23,13])
my_xticks =['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
fig = plt.figure()
plt.title('Violations based on Time' )
plt.xlabel('Hours in a day')
plt.ylabel('Number of violations')
plt.xticks (x2, my_xticks)
plt.plot(x2, y2, 'b*')
plt.plot(x2, y2)
plt.show()
fig.savefig('Time_wise_violations.jpg')

print ("\n")
print ("RESULTS")
print ("The above analysis indictates that: \n1.The dates in the month of december in which there are more number of violations recorded are 13th dec, 6th dec and 1st dec with 43, 40 and 34 violations respectively. Least was recored on 25th dec, only 1 violation. \n\n2.The highest number of violations in the month according to the days in the week is recored on Thursdays with 130 violations. Least violations are recorded on Saturday and Sunday with 20violations on each day. \n\n3.The maximum number of violation occured as usually in the Mid-days hours; 1pm being the highest in the month with 56 violations followed by 2pm with 44 violations and 11am 39 violations. Least number of violations are recorded in the early hours from 2 am to 6am ranging from 1 to 7 violations.")

