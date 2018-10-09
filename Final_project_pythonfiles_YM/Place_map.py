# -*- coding: utf-8 -*-
"""
Created on Wed May  3 18:24:38 2017

@author: AMRUTA MUNGIKAR
"""

import pandas as pd
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
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

denton= Basemap(projection='mill',llcrnrlon = -90,     # lower-left corner longitude
                  llcrnrlat = 25,       # lower-left corner latitude
                  urcrnrlon = -110,      # upper-right corner longitude
                  urcrnrlat = 40,   resolution='l')
denton.drawcoastlines()
denton.drawcountries()
denton.drawstates()
denton.fillcontinents(color='coral',lake_color='#FFFFFF')
denton.drawmapboundary(fill_color='#FFFFFF')

#my_Lat=[33.2167,33.2100,33.2090,33.1838,33.2195,33.2046,33.2245,33.1362]
#my_long=[-97.1413,-97.1300,-97.1534,-97.1306,-97.1898,-97.0606,-97.1036,-97.0821]
#for zipcode 76201-red

long,lat=-97.1413,33.2167
x,y=denton(long,lat)
denton.plot(x,y,'ro')

#for zipcode 76202- green

long,lat=-97.1300,33.2100
x,y=denton(long,lat)
denton.plot(x,y,'go')

#for zipcode 76203-blue
lat, long=33.2090, -97.1534
x,y=denton(long,lat)
denton.plot(x,y,'bo')

#for xipcode 76205-cyan
lat, long=33.1838, -97.1306
x,y=denton(long,lat)
denton.plot(x,y,'co')

#for zipcode 76207-magenta
lat, long=33.2195, -97.1898
x,y=denton(long,lat)
denton.plot(x,y,'mo')

#for zipcode 76208-yellow
lat, long=33.2046, -97.0606
x,y=denton(long,lat)
denton.plot(x,y,'yo')

#for zipcode 76209-white
lat, long=33.2245, -97.1036
x,y=denton(long,lat)
denton.plot(x,y,'wo')

#for zipcode 76210-black
lat, long=33.1362, -97.0821
x,y=denton(long,lat)
denton.plot(x,y,'ko')

plt.title("On Texas Map")
plt.show()

print('--------------------------')
denton_1= Basemap(projection='mill',llcrnrlon = -97,     # lower-left corner longitude
                  llcrnrlat = 33.1,       # lower-left corner latitude
                  urcrnrlon = -97.275,      # upper-right corner longitude
                  urcrnrlat = 33.3,   resolution='l')
denton_1.drawcoastlines()
denton_1.drawcountries()
denton_1.drawstates()
denton_1.fillcontinents(color='coral',lake_color='#FFFFFF')
denton_1.drawmapboundary(fill_color='#FFFFFF')

#for zipcode76201-red
lat, long= 33.2167,-97.1413
x,y=denton_1(long,lat)
denton_1.plot(x,y,'rD')

#for zipcode 76202- green
lat, long=33.2100, -97.1300
x,y=denton_1(long,lat)
denton_1.plot(x,y,'gD')

#for zipcode 76203-#blue
lat, long=33.2090, -97.1534
x,y=denton_1(long,lat)
denton_1.plot(x,y,'bD')

#for xipcode 76205-cyan
lat, long=33.1838, -97.1306
x,y=denton_1(long,lat)
denton_1.plot(x,y,'cD')

#for zipcode 76207-magenta
lat, long=33.2195, -97.1898
x,y=denton_1(long,lat)
denton_1.plot(x,y,'mD')

#for zipcode 76208-yellow
lat, long=33.2046, -97.0606
x,y=denton_1(long,lat)
denton_1.plot(x,y,'yD')

#for zipcode 76209-white
lat, long=33.2245, -97.1036
x,y=denton_1(long,lat)
denton_1.plot(x,y,'wD')

#for zipcode 76210-black
lat, long=33.1362, -97.0821
x,y=denton_1(long,lat)
denton_1.plot(x,y,'kD')
plt.title("zipcodes on Denton map")
plt.show()