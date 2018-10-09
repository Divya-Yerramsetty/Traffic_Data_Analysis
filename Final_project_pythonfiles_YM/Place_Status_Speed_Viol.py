# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 12:00:20 2017

@author: divya
"""
#This code consists of violations based on zipcodes, status wise and speeding violations
#Imorting pandas, numpy, datetime and matplotlib as required to analyze the csv file.

import pandas as pd
import numpy as np
import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
datetime.datetime.strptime
df = pd.read_csv('denton_traffic_violations.csv')
file1 = pd.read_csv("denton_traffic_violations.csv", parse_dates = [0], infer_datetime_format = True)
file = file1.rename(columns = {'ct_viol_date':'Datetime'})
temp = pd.DatetimeIndex(file['Datetime'])
file['Date'] = temp.date
file['Time'] = temp.time
del file['Datetime']
df['Date'] = file['Date']
df_sorted = df[['cit_citation_no','Date','nam_r_city','nam_r_zip1','viol_status','stc_desc','cod_desc1']]
#Creating new dataframe and saving this as denton.csv to perform required analyses. This new csv consits of specific columns extracted from the main denton_traffic_violations csv.
df_sorted.to_csv('denton.csv')
#The denton.csv consists of only specific columns listed with the above mentioned headers.
df_new = pd.read_csv('denton.csv')
df_new['Date'] = pd.to_datetime(df_new['Date'].astype(str))
#Filering csv based on Dentoncity
df_city_filtered = df_new[(df_new['nam_r_city'].str.contains("DENTON"))]
#Filtering the city filtered dataframe with dates as in mentioned only for the month of december.
df_date_filtered = df_city_filtered[(df_city_filtered['Date'] >= '2016-12-01') & (df_city_filtered['Date'] <= '2016-12-31')]
#Listing and sorting zipcodes in the city of denton and for the month of december
zipcodes = (df_date_filtered.nam_r_zip1.unique())
(zipcodes.sort(axis = -1, kind = 'quicksort', order = None))
print ("THIS IS THE OUTPUT FOR NUMBER OF VIOLATIONS BASED ON PLACE-WISE IN THE CITY OF DENTON. THE PLACE-WISE VIOLATIONS ARE LISTED BASED ON PIN-CODES.")
print ("There are", len(zipcodes), "different places in the city of Denton where the violations are recorded.")
print ("\n")
for item in zipcodes:
    df_zip = df_date_filtered[(df_date_filtered['nam_r_zip1'] == item)]
    Citation_list = df_date_filtered[df_date_filtered['nam_r_zip1'] == item].cit_citation_no.tolist()
    print ("The number of violations based on pincode", item, "are:", len(df_zip))
    print ("The list of Citation numbers based on pincode", item, "are:", Citation_list)
    print ("\n")
#Plotting the number of violations based on zip codes.
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([108,1,1,72,66,34,119,77])
my_xticks = ['76201','76202','76203','76205','76207','76208','76209','76210']
fig = plt.figure()
plt.title('Violations based on zip codes' )
plt.xlabel('Zip codes')
plt.ylabel('Number of violations')
plt.xticks (x, my_xticks)
plt.plot(x, y, 'b*')
plt.plot(x,y)
plt.show()
fig.savefig('Zipcodes_wise_violations.jpg')
print ("*****************************************************************************")

#This is the violation list based upon the status given by police. The number of each type of violation is recorded and the corresponding tickets are also listed for each case.
#Filtering the data by status given by police 
df_viol = df_date_filtered[['Date','nam_r_city','viol_status','stc_desc']]
viol_status = (df_viol.stc_desc.unique())
(viol_status.sort(axis = -1, kind = 'quicksort', order = None))
print ("THIS IS THE OUTPUT FOR THE STATUS GIVEN BY THE POLICE TO THE CORRESPONDING VIOLATION WHICH HAS OCCURED.")
print ("There are", len(viol_status), "statuses given by police in return to the type of violation.")
print ("\n")
for item1 in viol_status:
    df_viol_status = df_viol[df_viol['stc_desc'] == item1]
    Citation_list = df_date_filtered[df_date_filtered['stc_desc'] == item1].cit_citation_no.tolist()
    print ("The number of violations that have ", item1.strip(), "as status are:", len(df_viol_status))
    print ("The list of Citation numbers according to", item1.strip(), "are:", Citation_list)
    print ("\n")
#Plotting the number of violations based on status description given by police for violations.
x1 = np.array([1,2,3,4,5,6,7,8,9,10,11])
y1 = np.array([4,14,7,11,2,25,399,1,1,6,8])
my_xticks = ['AD','CL','DL','AJ','D2','CD','IA','JA','PD','IV','I2']
fig = plt.figure()
plt.title('Actions taken by police' )
plt.xlabel('viol_status')
plt.ylabel('Number of violations')
plt.xticks (x1, my_xticks)
plt.plot(x1, y1, 'b*')
plt.plot(x1,y1)
plt.show()
fig.savefig('Status_wise_violations.jpg')
print (" ")
print ("***************************************************************************")

#This is the violation list regarding differnt types of speeding violations.
df_speed = df_date_filtered[['Date','nam_r_city','cod_desc1']]
#Filtering data based on speeding violations
df_speeding = df_speed[(df_speed['cod_desc1'].str.contains("SPEEDING"))]
speed_status = (df_speeding.cod_desc1.unique())
(speed_status.sort(axis = -1, kind = 'quicksort', order = None))
print ("THIS IS THE OUTPUT FOR THE DIFFERENT TYPES OF VIOLATIONS RELATED TO SPEEDING.")
print ("There are", len(speed_status), "different speeding violations.")
print ("\n")
for item2 in speed_status:
    df_speed_viol = df_speeding[df_speeding['cod_desc1'] == item2]
    Citation_list = df_date_filtered[df_date_filtered['cod_desc1'] == item2].cit_citation_no.tolist()
    print ("The number of speeding violations based on", item2.strip(), "are:", len(df_speed_viol))
    print ("The list of Citation numbers according to", item2.strip(), "are:", Citation_list)
    print ("\n")
#Plotting the number of violations based on speeding issues.
x2 = np.array([1,2,3,4,5,6])
y2 = np.array([1,1,72,82,13,6])
my_xticks = ['ZS30','ZSI35','S','S30M','SIH35','SSZ']
fig = plt.figure()
plt.title('Violations based on Speed' )
plt.xlabel('Speeding violations')
plt.ylabel('Number of violations')
plt.xticks (x2, my_xticks)
plt.plot(x2, y2, 'b*')
plt.plot(x2, y2)
plt.show()
fig.savefig('Speed_wise_violations.jpg')

print ("\n")
print ("RESULTS")
print ("The above analysis indictates that: \n1.The places in Denton with highest number of violations from people living in the areas with the pincodes 76209 with 119 violations. The least number of violations are recorded in the places with the pincodes 76202 and 76203 with only 1 violation. \n\n2.The most repeated status given to violations by the police is INITIAL ARRAIGNMENT. There are 399 cases with the IA Status. \nThe least number of punishments given by the police are JAIL ARRAIGNMENT and PENDING DISMISSAL. \n\n3.The frequently violated speeding violation is the SPEEDING IN 30 MILE HOUR ZONE. There are 82 violations based on this speeding violation condition. The least speeding violation recorded is CONST ZONE SPEEDING 30 MPH ZN.")



