#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 02:17:37 2020

@author: apple
"""


import pandas as pd
import matplotlib.pyplot as plt

print("Hello descriptive stats")
myattritionDataSet = pd.read_excel("3.DescriptiveStatistics.xlsx",sheet_name=0)

attritionHead = myattritionDataSet.head(5)
print(attritionHead)

#1.To find measure of central tendency:
#Mean, Median Mode.

#1.1Mean - Average
meanVal = myattritionDataSet['CurrentSalary'].mean() 
print(meanVal) # -34419/56

#1.2Median - To find the middle value
medianVal = myattritionDataSet['CurrentSalary'].median()
print(medianVal) # -28875.0


#1.3Mode - To find the most repeated value
modeVal = myattritionDataSet['CurrentSalary'].mode()
print(modeVal)# - 30,750

#2.Measure of dispersion
#standard deviation,variance,range,percentile,interquarentile

#2.1Std dev- Represents the consistency
stdDevVal = myattritionDataSet['CurrentSalary'].std()
print(stdDevVal) # - 170.756

#2.2Variance - To see the variation from the mean
varianceVal = myattritionDataSet['CurrentSalary'].var()
#- 291578214.45


#2.3 Describe - Prints overAll datas like mean range,percentiles/quarentiles
describeVal = myattritionDataSet['CurrentSalary'].describe()
print(describeVal)


#3.Measure of shape or distribution
#Unimodal, #bimodal,Bell Shaped


#3.1 - Skewness:- Measure of symmetry
#mean,median,mode = 0 - Normally distributed
#Mean<median - negatively skewed.
#Mean>Median - Positevely Skewed.

skewedVal = myattritionDataSet['CurrentSalary'].skew()
print(skewedVal) #- 2.124 - Positively skewed.

#3.2 - kurtosis - Measure of peakness of data.
#Lepto,meso,platyo

kurtosisVal = myattritionDataSet['CurrentSalary'].kurt()
print(kurtosisVal) #5.3778 -leptokryptic - peakness is high


boxplotVal = plt.boxplot(myattritionDataSet['CurrentSalary'])
print(boxplotVal)


#ScatterPlot - To find the outliers


scatterPlotVal = plt.scatter(myattritionDataSet['CurrentSalary'],myattritionDataSet['After6Months'])
print(scatterPlotVal)












