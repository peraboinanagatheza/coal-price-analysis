# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:15:47 2024

@author: NAGA
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
dir (pd)
dir(np)
dir(sns)
dir(plt)
merged_economic_data = pd.read_csv(r"C:/Users/NAGA/OneDrive/Desktop/360degiTMG/merged_economic_data.csv")
#First Moment Business Decision
mean  = merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].mean()
print(mean)
mean1 = merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].mean()
print(mean1)
mean2 = merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].mean()
print(mean2)
mean3 = merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].mean()
print(mean3)
mean4 =  merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].mean()
print(mean4)
mean5 = merged_economic_data['Price_WTI'].mean()
print(mean5)
mean6 = merged_economic_data['Price_Brent_Oil'].mean()
print(mean6)
mean7 = merged_economic_data['Price_Dubai_Brent_Oil'].mean()
print(mean7)
mean8 = merged_economic_data['Price_ExxonMobil'].mean()
print(mean8)
mean9 = merged_economic_data['Price_NTPC'].mean()
print(mean9)
mean10 = merged_economic_data['Price_Shenhua'].mean()
print(mean10)
mean11 = merged_economic_data['tempmax_RB'].mean()
print(mean11)
mean12 = merged_economic_data['tempmin_RB'].mean()
print(mean12)
mean13 = merged_economic_data['temp_RB'].mean()
print(mean13)
mean14 = merged_economic_data['dew_RB'].mean()
print(mean14)
mean15 = merged_economic_data['humidity_RB'].mean()
print(mean15)
mean16 = merged_economic_data['precip_RB'].mean()
print(mean16)
mean17 = merged_economic_data['preciptype_RB'].mean()
print(mean17)
mean18 = merged_economic_data['windspeed_RB'].mean()
print(mean18)
mean19 = merged_economic_data['tempmax_Limpopo'].mean()
print(mean19)
mean20 = merged_economic_data['tempmin_Limpopo'].mean()
print(mean20)
mean21 = merged_economic_data['temp_Limpopo'].mean()
print(mean21)
mean22 = merged_economic_data['dew_Limpopo'].mean()
print(mean22)
mean23 = merged_economic_data['humidity_Limpopo'].mean()
print(mean23)
mean24 = merged_economic_data['precip_Limpopo'].mean()
print(mean24)
mean25 = merged_economic_data['preciptype_Limpopo'].mean()
print(mean25)
mean26 = merged_economic_data['windspeed_Limpopo'].mean()
print(mean26)

#median

median = merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].median()
print(median)
median1 = merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].median()
print(median1)
median2 = merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].median()
print(median2)
median3 = merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].median()
print(median3)
median4 =  merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].median()
print(median4)
median5 = merged_economic_data['Price_WTI'].median()
print(median5)
median6 = merged_economic_data['Price_Brent_Oil'].median()
print(median6)
median7 = merged_economic_data['Price_Dubai_Brent_Oil'].median()
print(median7)
median8 = merged_economic_data['Price_ExxonMobil'].median()
print(median8)
median9 = merged_economic_data['Price_NTPC'].median()
print(median9)
median10 = merged_economic_data['Price_Shenhua'].median()
print(median10)
median11 = merged_economic_data['tempmax_RB'].median()
print(median11)
median12 = merged_economic_data['tempmin_RB'].median()
print(median12)
median13 = merged_economic_data['temp_RB'].median()
print(median13)
median14 = merged_economic_data['dew_RB'].median()
print(median14)
median15 = merged_economic_data['humidity_RB'].median()
print(median15)
median16 = merged_economic_data['precip_RB'].median()
print(median16)
median17 = merged_economic_data['preciptype_RB'].median()
print(median17)
median18 = merged_economic_data['windspeed_RB'].median()
print(median18)
median19 = merged_economic_data['tempmax_Limpopo'].median()
print(median19)
median20 = merged_economic_data['tempmin_Limpopo'].median()
print(median20)
median21 = merged_economic_data['temp_Limpopo'].median()
print(median21)
median22 = merged_economic_data['dew_Limpopo'].median()
print(median22)
median23 = merged_economic_data['humidity_Limpopo'].median()
print(median23)
median24 = merged_economic_data['precip_Limpopo'].median()
print(median24)
median25 = merged_economic_data['preciptype_Limpopo'].median()
print(median25)
median26 = merged_economic_data['windspeed_Limpopo'].median()
print(median26)

#mode

mode  = merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].mode()
print(mode)
mode1 = merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].mode()
print(mode1)
mode2 = merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].mode()
print(mode2)
mode3 = merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].mode()
print(mode3)
mode4 =  merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].mode()
print(mode4)
mode5 = merged_economic_data['Price_WTI'].mode()
print(mode5)
mode6 = merged_economic_data['Price_Brent_Oil'].mode()
print(mode6)
mode7 = merged_economic_data['Price_Dubai_Brent_Oil'].mode()
print(mode7)
mode8 = merged_economic_data['Price_ExxonMobil'].mode()
print(mode8)
mode9 = merged_economic_data['Price_NTPC'].mode()
print(mode9)
mode10 = merged_economic_data['Price_Shenhua'].mode()
print(mode10)
mode11 = merged_economic_data['tempmax_RB'].mode()
print(mode11)
mode12 = merged_economic_data['tempmin_RB'].mode()
print(mode12)
mode13 = merged_economic_data['temp_RB'].mode()
print(mode13)
mode14 = merged_economic_data['dew_RB'].mode()
print(mode14)
mode15 = merged_economic_data['humidity_RB'].mode()
print(mode15)
mode16 = merged_economic_data['precip_RB'].mode()
print(mode16)
mode17 = merged_economic_data['preciptype_RB'].mode()
print(mode17)
mode18 = merged_economic_data['windspeed_RB'].mode()
print(mode18)
mode19 = merged_economic_data['tempmax_Limpopo'].mode()
print(mode19)
mode20 = merged_economic_data['tempmin_Limpopo'].mode()
print(mode20)
mode21 = merged_economic_data['temp_Limpopo'].mode()
print(mode21)
mode22 = merged_economic_data['dew_Limpopo'].mode()
print(mode22)
mode23 = merged_economic_data['humidity_Limpopo'].mode()
print(mode23)
mode24 = merged_economic_data['precip_Limpopo'].mode()
print(mode24)
mode25 = merged_economic_data['preciptype_Limpopo'].mode()
print(mode25)
mode26 = merged_economic_data['windspeed_Limpopo'].mode()
print(mode26)

#variance

variance = merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].var()
print(variance)
variance1 = merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].var()
print(variance1)
variance2 = merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].var()
print(variance2)
variance3 = merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].var()
print(variance3)
variance4 =  merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].var()
print(variance4)
variance5 = merged_economic_data['Price_WTI'].var()
print(variance5)
variance6 = merged_economic_data['Price_Brent_Oil'].var()
print(variance6)
variance7 = merged_economic_data['Price_Dubai_Brent_Oil'].var()
print(variance7)
variance8 = merged_economic_data['Price_ExxonMobil'].var()
print(variance8)
variance9 = merged_economic_data['Price_NTPC'].var()
print(variance9)
variance10 = merged_economic_data['Price_Shenhua'].var()
print(variance10)
variance11 = merged_economic_data['tempmax_RB'].var()
print(variance11)
variance12 = merged_economic_data['tempmin_RB'].var()
print(variance12)
variance13 = merged_economic_data['temp_RB'].var()
print(variance13)
variance14 = merged_economic_data['dew_RB'].var()
print(mean14)
variance15 = merged_economic_data['humidity_RB'].var()
print(variance15)
variance16 = merged_economic_data['precip_RB'].var()
print(variance16)
variance17 = merged_economic_data['preciptype_RB'].var()
print(variance17)
variance18 = merged_economic_data['windspeed_RB'].var()
print(variance18)
variance19 = merged_economic_data['tempmax_Limpopo'].var()
print(variance19)
variance20 = merged_economic_data['tempmin_Limpopo'].var()
print(variance20)
variance21 = merged_economic_data['temp_Limpopo'].var()
print(variance21)
variance22 = merged_economic_data['dew_Limpopo'].var()
print(variance22)
variance23 = merged_economic_data['humidity_Limpopo'].var()
print(variance23)
variance24 = merged_economic_data['precip_Limpopo'].var()
print(variance24)
variance25 = merged_economic_data['preciptype_Limpopo'].var()
print(variance25)
variance26 = merged_economic_data['windspeed_Limpopo'].var()
print(variance26)

#std_dev
std_dev  = merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].std()
print(std_dev)
std_dev1 = merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].std()
print(std_dev1)
std_dev2 = merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].std()
print(std_dev2)
std_dev3 = merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].std()
print(std_dev3)
std_dev4 =  merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].std()
print(std_dev4)
std_dev5 = merged_economic_data['Price_WTI'].std()
print(std_dev5)
std_dev6 = merged_economic_data['Price_Brent_Oil'].std()
print(std_dev6)
std_dev7 = merged_economic_data['Price_Dubai_Brent_Oil'].std()
print(std_dev7)
std_dev8 = merged_economic_data['Price_ExxonMobil'].std()
print(std_dev8)
std_dev9 = merged_economic_data['Price_NTPC'].std()
print(std_dev9)
std_dev10 = merged_economic_data['Price_Shenhua'].std()
print(std_dev10)
std_dev11 = merged_economic_data['tempmax_RB'].std()
print(std_dev11)
std_dev12 = merged_economic_data['tempmin_RB'].std()
print(std_dev12)
std_dev13 = merged_economic_data['temp_RB'].std()
print(std_dev13)
std_dev14 = merged_economic_data['dew_RB'].std()
print(std_dev14)
std_dev15 = merged_economic_data['humidity_RB'].std()
print(std_dev15)
std_dev16 = merged_economic_data['precip_RB'].std()
print(std_dev16)
std_dev17 = merged_economic_data['preciptype_RB'].std()
print(std_dev17)
std_dev18 = merged_economic_data['windspeed_RB'].std()
print(std_dev18)
std_dev19 = merged_economic_data['tempmax_Limpopo'].std()
print(std_dev19)
std_dev20 = merged_economic_data['tempmin_Limpopo'].std()
print(std_dev20)
std_dev21 = merged_economic_data['temp_Limpopo'].std()
print(std_dev21)
std_dev22 = merged_economic_data['dew_Limpopo'].std()
print(std_dev22)
std_dev23 = merged_economic_data['humidity_Limpopo'].std()
print(std_dev23)
std_dev24 = merged_economic_data['precip_Limpopo'].std()
print(std_dev24)
std_dev25 = merged_economic_data['preciptype_Limpopo'].std()
print(std_dev25)
std_dev26 = merged_economic_data['windspeed_Limpopo'].std()
print(std_dev26)

# range

range_1= merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].max()- merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].min()
print(range_1)
range_2= merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].max()- merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].min()
print(range_2)
range_3= merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].max()- merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].min()
print(range_3)
range_4= merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].max()- merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].min()
print(range_4)
range_5= merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].max()- merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].min()
print(range_5)
range_6= merged_economic_data['Price_WTI'].max()- merged_economic_data['Price_WTI'].min()
print(range_6)
range_7= merged_economic_data['Price_Brent_Oil'].max()- merged_economic_data['Price_Brent_Oil'].min()
print(range_7)
range_8= merged_economic_data['Price_Dubai_Brent_Oil'].max()- merged_economic_data['Price_Dubai_Brent_Oil'].min()
print(range_8)
range_9= merged_economic_data['Price_ExxonMobil'].max()- merged_economic_data['Price_ExxonMobil'].min()
print(range_9)
range_10= merged_economic_data['Price_NTPC'].max()- merged_economic_data['Price_NTPC'].min()
print(range_10)
range_11= merged_economic_data['Price_Shenhua'].max()- merged_economic_data['Price_Shenhua'].min()
print(range_11)
range_12= merged_economic_data['tempmax_RB'].max()- merged_economic_data['tempmax_RB'].min()
print(range_12)
range_13= merged_economic_data['tempmin_RB'].max()- merged_economic_data['tempmin_RB'].min()
print(range_13)
range_14= merged_economic_data['temp_RB'].max()- merged_economic_data['temp_RB'].min()
print(range_14)
range_15= merged_economic_data['dew_RB'].max()- merged_economic_data['dew_RB'].min()
print(range_15)
range_16= merged_economic_data['humidity_RB'].max()- merged_economic_data['humidity_RB'].min()
print(range_16)
range_17= merged_economic_data['precip_RB'].max()- merged_economic_data['precip_RB'].min()
print(range_17)
range_19= merged_economic_data['windspeed_RB'].max()- merged_economic_data['windspeed_RB'].min()
print(range_19)
range_20= merged_economic_data['tempmax_Limpopo'].max()- merged_economic_data['tempmax_Limpopo'].min()
print(range_20)
range_21= merged_economic_data['tempmin_Limpopo'].max()- merged_economic_data['tempmin_Limpopo'].min()
print(range_21)
range_22= merged_economic_data['temp_Limpopo'].max()- merged_economic_data['temp_Limpopo'].min()
print(range_22)
range_23= merged_economic_data['dew_Limpopo'].max()- merged_economic_data['dew_Limpopo'].min()
print(range_23)
range_24= merged_economic_data['humidity_Limpopo'].max()- merged_economic_data['humidity_Limpopo'].min()
print(range_24)
range_25= merged_economic_data['precip_Limpopo'].max()- merged_economic_data['precip_Limpopo'].min()
print(range_25)
range_27= merged_economic_data['windspeed_Limpopo'].max()- merged_economic_data['windspeed_Limpopo'].min()
print(range_27)


## third moment decesion
# skewness

skew_1=merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].skew()
print(skew_1)
skew_2=merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].skew()
print(skew_2)
skew_3=merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].skew()
print(skew_3)
skew_4=merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].skew()
print(skew_4)
skew_5=merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].skew()
print(skew_5)
skew_6=merged_economic_data['Price_WTI'].skew()
print(skew_6)
skew_7=merged_economic_data['Price_Brent_Oil'].skew()
print(skew_7)
skew_8=merged_economic_data['Price_Dubai_Brent_Oil'].skew()
print(skew_8)
skew_9=merged_economic_data['Price_ExxonMobil'].skew()
print(skew_9)
skew_10=merged_economic_data['Price_NTPC'].skew()
print(skew_10)
skew_11=merged_economic_data['Price_Shenhua'].skew()
print(skew_11)
skew_12=merged_economic_data['tempmax_RB'].skew()
print(skew_12)
skew_13=merged_economic_data['tempmin_RB'].skew()
print(skew_13)
skew_14=merged_economic_data['temp_RB'].skew()
print(skew_14)
skew_15=merged_economic_data['dew_RB'].skew()
print(skew_15)
skew_16=merged_economic_data['humidity_RB'].skew()
print(skew_16)
skew_17=merged_economic_data['precip_RB'].skew()
print(skew_17)
skew_19=merged_economic_data['windspeed_RB'].skew()
print(skew_19)
skew_20=merged_economic_data['tempmax_Limpopo'].skew()
print(skew_20)
skew_21=merged_economic_data['tempmin_Limpopo'].skew()
print(skew_21)
skew_22=merged_economic_data['temp_Limpopo'].skew()
print(skew_22)
skew_23=merged_economic_data['dew_Limpopo'].skew()
print(skew_23)
skew_24=merged_economic_data['humidity_Limpopo'].skew()
print(skew_24)
skew_25=merged_economic_data['precip_Limpopo'].skew()
print(skew_25)
skew_27=merged_economic_data['windspeed_Limpopo'].skew()
print(skew_27)

# fourth moment decesion
# kurtosis
kurt_1=merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].kurtosis()
print(kurt_1)
kurt_2=merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].kurtosis()
print(kurt_2)
kurt_3=merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].kurtosis()
print(kurt_3)
kurt_4=merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].kurtosis()
print(kurt_4)
kurt_5=merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].kurtosis()
print(kurt_5)
kurt_6=merged_economic_data['Price_WTI'].kurtosis()
print(kurt_6)
kurt_7=merged_economic_data['Price_Brent_Oil'].kurtosis()
print(kurt_7)
kurt_8=merged_economic_data['Price_Dubai_Brent_Oil'].kurtosis()
print(kurt_8)
kurt_9=merged_economic_data['Price_ExxonMobil'].kurtosis()
print(kurt_9)
kurt_10=merged_economic_data['Price_NTPC'].kurtosis()
print(kurt_10)
kurt_11=merged_economic_data['Price_Shenhua'].kurtosis()
print(kurt_11)
kurt_12=merged_economic_data['tempmax_RB'].kurtosis()
print(kurt_12)
kurt_13=merged_economic_data['tempmin_RB'].kurtosis()
print(kurt_13)
kurt_14=merged_economic_data['temp_RB'].kurtosis()
print(kurt_14)
kurt_15=merged_economic_data['dew_RB'].kurtosis()
print(kurt_15)
kurt_16=merged_economic_data['humidity_RB'].kurtosis()
print(kurt_16)
kurt_17=merged_economic_data['precip_RB'].kurtosis()
print(kurt_17)
kurt_19=merged_economic_data['windspeed_RB'].kurtosis()
print(kurt_19)
kurt_20=merged_economic_data['tempmax_Limpopo'].kurtosis()
print(kurt_20)
kurt_21=merged_economic_data['tempmin_Limpopo'].kurtosis()
print(kurt_21)
kurt_22=merged_economic_data['temp_Limpopo'].kurtosis()
print(kurt_22)
kurt_23=merged_economic_data['dew_Limpopo'].kurtosis()
print(kurt_23)
kurt_24=merged_economic_data['humidity_Limpopo'].kurtosis()
print(kurt_24)
kurt_25=merged_economic_data['precip_Limpopo'].kurtosis()
print(kurt_25)
kurt_27=merged_economic_data['windspeed_Limpopo'].kurtosis()
print(kurt_27)

## graphical representation


plt.figure(figsize=(10, 6))

# Univariate Analysis
# Histogram for Coal_RB_4800_FOB_London_Close_USD
plt.hist(merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'], bins=20)
plt.title('Histogram of Coal_RB_4800_FOB_London_Close_USD')
plt.xlabel('Coal_RB_4800_FOB_London_Close_USD')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# defing the functioning to plot the histogram for all the columns by using the for loop .

merged_economic_data.describe
merged_economic_data.columns
#list of columns 

columns = [
    'Coal_RB_5500_FOB_London_Close_USD',
    'Coal_RB_5700_FOB_London_Close_USD',
    'Coal_RB_6000_FOB_CurrentWeek_Avg_USD',
    'Coal_India_5500_CFR_London_Close_USD',
    'Price_WTI',
    'Price_Brent_Oil',
    'Price_Dubai_Brent_Oil',
    'Price_ExxonMobil',
    'Price_NTPC',
    'Price_Shenhua',
    'tempmax_RB',
    'tempmin_RB',
    'temp_RB',
    'dew_RB',
    'humidity_RB',
    'precip_RB',
    'windspeed_RB',
    'tempmax_Limpopo',
    'tempmin_Limpopo',
    'temp_Limpopo',
    'dew_Limpopo',
    'humidity_Limpopo',
    'precip_Limpopo',
    'windspeed_Limpopo'
]


# function to plot the histogram for each given column

def plot_histogram(column):
 plt.hist(data[columns].dropna(), bins=20)
    plt.title(f'Histogram of {columns}')
    plt.xlabel(columns)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    
# plots for each given column by using for loop
for column in columns:
    plot_histogram(column)
    
    plt.hist(merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'], bins=20)
    plt.title('Histogram of Coal_RB_4800_FOB_London_Close_USD')
    plt.xlabel('Coal_RB_5500_FOB_London_Close_USD')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    
    #graphical histogram
    plt.hist(merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'], bins=20)
    plt.hist(merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'], bins=20)
    plt.hist(merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'], bins=20)
    plt.hist(merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'], bins=20)
    plt.hist(merged_economic_data['Coal_India_5500_CFR_London_Close_USD'], bins=20)
    plt.hist(merged_economic_data['Price_WTI'], bins=20)
    plt.hist(merged_economic_data['Price_Brent_Oil'], bins=20)
    plt.hist(merged_economic_data['Price_Dubai_Brent_Oil'], bins=20)
    plt.hist(merged_economic_data['Price_ExxonMobil'], bins=20)
    plt.hist(merged_economic_data['Price_NTPC'], bins=20)
    plt.hist(merged_economic_data['Price_Shenhua'], bins=20)
    plt.hist(merged_economic_data['tempmax_RB'], bins=20)
    plt.hist(merged_economic_data['tempmin_RB'], bins=20)
    plt.hist(merged_economic_data['temp_RB'], bins=20)
    plt.hist(merged_economic_data['dew_RB'], bins=20)
    plt.hist(merged_economic_data['humidity_RB'], bins=20)
    plt.hist(merged_economic_data['precip_RB'], bins=20)
    plt.hist(merged_economic_data['preciptype_RB'], bins=20)
    plt.hist(merged_economic_data['windspeed_RB'], bins=20)
    plt.hist(merged_economic_data['tempmax_Limpopo'], bins=20)
    plt.hist(merged_economic_data['tempmin_Limpopo'], bins=20)
    plt.hist(merged_economic_data['temp_Limpopo'], bins=20)
    plt.hist(merged_economic_data['dew_Limpopo'], bins=20)
    plt.hist(merged_economic_data['humidity_Limpopo'], bins=20)
    plt.hist(merged_economic_data['precip_Limpopo'], bins=20)
    plt.hist(merged_economic_data['preciptype_Limpopo'], bins=20)
    plt.hist(merged_economic_data['windspeed_Limpopo'], bins=20)
    
    #boxplot
    sns.boxplot(merged_economic_data.Coal_RB_4800_FOB_London_Close_USD)
    sns.boxplot(merged_economic_data.Coal_RB_5500_FOB_London_Close_USD)
    sns.boxplot(merged_economic_data.Coal_RB_5700_FOB_London_Close_USD)
    sns.boxplot(merged_economic_data.Coal_RB_6000_FOB_CurrentWeek_Avg_USD)
    sns.boxplot(merged_economic_data.Coal_India_5500_CFR_London_Close_USD)
    sns.boxplot(merged_economic_data.Price_WTI)
    sns.boxplot(merged_economic_data.Price_Brent_Oil)
    sns.boxplot(merged_economic_data.Price_Dubai_Brent_Oil)
    sns.boxplot(merged_economic_data.Price_ExxonMobil)
    sns.boxplot(merged_economic_data.Price_NTPC)
    sns.boxplot(merged_economic_data.Price_Shenhua)
    sns.boxplot(merged_economic_data.tempmax_RB)
    sns.boxplot(merged_economic_data.tempmin_RB)
    sns.boxplot(merged_economic_data.temp_RB)
    sns.boxplot(merged_economic_data.dew_RB)
    sns.boxplot(merged_economic_data.humidity_RB)
    sns.boxplot(merged_economic_data.precip_RB)
    sns.boxplot(merged_economic_data.preciptype_RB)
    sns.boxplot(merged_economic_data.windspeed_RB)
    sns.boxplot(merged_economic_data.tempmax_Limpopo)
    sns.boxplot(merged_economic_data.tempmin_Limpopo)
    sns.boxplot(merged_economic_data.temp_Limpopo)
    sns.boxplot(merged_economic_data.dew_Limpopo)
    sns.boxplot(merged_economic_data.humidity_Limpopo)
    sns.boxplot(merged_economic_data.precip_Limpopo)
    sns.boxplot(merged_economic_data.preciptype_Limpopo)
    sns.boxplot(merged_economic_data.windspeed_Limpopo)
    
#replacing with missing values
merged_economic_data['preciptype_RB'] = merged_economic_data['preciptype_RB'].fillna('no rain')
print(merged_economic_data)
merged_economic_data['preciptype_Limpopo'] = merged_economic_data['preciptype_Limpopo'].fillna('no rain')
print(merged_economic_data)
    # Detection of Outliers
IQR = merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].quantile(0.75) - merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].quantile(0.25) # IQR - Inter quartile range IQR = Q3-Q1
lower_limit = merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].quantile(0.25) - (IQR * 1.5) # Q1 - 1.5 * IQR
upper_limit =merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].quantile(0.75) + (IQR * 1.5) # Q3 + 1.5 * IQR
IQR1 = merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].quantile(0.75) - merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].quantile(0.25)
IQR2 = merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].quantile(0.75) - merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].quantile(0.25) # IQR - Inter quartile range IQR = Q3-Q1
IQR3 = merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].quantile(0.75) - merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].quantile(0.25) # IQR - Inter quartile range IQR = Q3-Q1
IQR4 = merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].quantile(0.75) - merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].quantile(0.25) # IQR - Inter quartile range IQR = Q3-Q1
IQR5 = merged_economic_data['Price_WTI'].quantile(0.75) - merged_economic_data['Price_WTI'].quantile(0.25) # IQR - Inter quartile range IQR = Q3-Q1
IQR6= merged_economic_data['Price_Brent_Oil'].quantile(0.75) - merged_economic_data['Price_Brent_Oil'].quantile(0.25) # IQR - Inter quartile range IQR = Q3-Q1
IQR7= merged_economic_data['Price_Dubai_Brent_Oil'].quantile(0.75) - merged_economic_data['Price_Dubai_Brent_Oil'].quantile(0.25) # IQR - Inter quartile range IQR = Q3-Q1
IQR8= merged_economic_data['Price_ExxonMobil'].quantile(0.75) - merged_economic_data['Price_ExxonMobil'].quantile(0.25) # IQR - Inter quartile range IQR = Q3-Q1
IQR9= merged_economic_data['Price_NTPC'].quantile(0.75) - merged_economic_data['Price_NTPC'].quantile(0.25) # IQR - Inter quartile range IQR = Q3-Q1
IQR10= merged_economic_data['Price_Shenhua'].quantile(0.75) - merged_economic_data['Price_Shenhua'].quantile(0.25) # IQR - Inter quartile range IQR = Q3-Q1
IQR11 = merged_economic_data['tempmax_RB'].quantile(0.75) - merged_economic_data['tempmax_RB'].quantile(0.25)
IQR12 = merged_economic_data['tempmin_RB'].quantile(0.75) - merged_economic_data['tempmin_RB'].quantile(0.25)
IQR13 = merged_economic_data['temp_RB'].quantile(0.75) - merged_economic_data['temp_RB'].quantile(0.25)
IQR14 = merged_economic_data['dew_RB'].quantile(0.75) - merged_economic_data['dew_RB'].quantile(0.25)
IQR15 = merged_economic_data['humidity_RB'].quantile(0.75) - merged_economic_data['humidity_RB'].quantile(0.25)
IQR16 = merged_economic_data['precip_RB'].quantile(0.75) - merged_economic_data['precip_RB'].quantile(0.25)
IQR17 = merged_economic_data['preciptype_RB'].quantile(0.75) - merged_economic_data['preciptype_RB'].quantile(0.25)
IQR18= merged_economic_data['windspeed_RB'].quantile(0.75) - merged_economic_data['windspeed_RB'].quantile(0.25)
#missing values
merged_economic_data.isnull().sum().sum()
merged_economic_data.columns
merged_economic_data.isna().sum().sum()
print(merged_economic_data)

#forword fill method
merged_economic_data['Coal_RB_4800_FOB_London_Close_USD']=merged_economic_data['Coal_RB_4800_FOB_London_Close_USD'].fillna(method='ffill')
merged_economic_data['Coal_RB_5500_FOB_London_Close_USD']=merged_economic_data['Coal_RB_5500_FOB_London_Close_USD'].fillna(method='ffill')
merged_economic_data['Coal_RB_5700_FOB_London_Close_USD']=merged_economic_data['Coal_RB_5700_FOB_London_Close_USD'].fillna(method='ffill')
merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD']=merged_economic_data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].fillna(method='ffill')
merged_economic_data['Coal_India_5500_CFR_London_Close_USD']=merged_economic_data['Coal_India_5500_CFR_London_Close_USD'].fillna(method='ffill')
merged_economic_data['Price_WTI']=merged_economic_data['Price_WTI'].fillna(method='ffill')
merged_economic_data['Price_Brent_Oil']=merged_economic_data['Price_Brent_Oil'].fillna(method='ffill')    
merged_economic_data['Price_Dubai_Brent_Oil']=merged_economic_data['Price_Dubai_Brent_Oil'].fillna(method='ffill')    
merged_economic_data['Price_ExxonMobil']=merged_economic_data['Price_ExxonMobil'].fillna(method='ffill')    
merged_economic_data['Price_NTPC']=merged_economic_data['Price_NTPC'].fillna(method='ffill')    
merged_economic_data['Price_Shenhua']=merged_economic_data['Price_Shenhua'].fillna(method='ffill')   

#backword fill method
merged_economic_data['Price_NTPC']=merged_economic_data['Price_NTPC'].fillna(method='bfill')    

    #detecting outliers and replacing nan
   
        Q1 =  merged_economic_data[columns].quantile(0.25)
        Q3 =  merged_economic_data[columns].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        merged_economic_data[columns] = pd.DataFrame(np.where( merged_economic_data[columns] > upper_bound, np.nan, np.where( merged_economic_data[columns] < lower_bound, np.nan,  merged_economic_data[columns])))
    
#performing linear interpolation on data
merged_economic_data[columns] =merged_economic_data[columns].interpolate(method='linear').ffill().bfill()
    

#eda preprocessing by using autoeda
import pandas as pd 

df = pd.read_csv(r"C:/Users/NAGA/OneDrive/Desktop/360degiTMG/merged_economic_data.csv")
#pip install sweetviz
import sweetviz as sv

s = sv.analyze(df)
s.show_html()



# D-Tale
########

 pip install dtale   
import dtale
import pandas as pd

df = pd.read_csv(r"C:/Users/NAGA/OneDrive/Desktop/360degiTMG/merged_economic_data.csv")

d = dtale.show(df)
d.open_browser()






    
    
    
    
    
    
    
    
   
 
    