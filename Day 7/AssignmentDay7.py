#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: apple


#Assignment:

Problem Statement A large company named XYZ, employs, at any given point of time, around 4000 employees. However, every year, around 15% of its employees leave the company and need to be replaced with the talent pool available in the job market. The management believes that this level of attrition (employees leaving, either on their own or because they got fired) is bad for the company, because of the following reasons -

The former employeesí projects get delayed, which makes it difficult to meet timelines, resulting in a reputation loss among consumers and partners
A sizeable department has to be maintained, for the purposes of recruiting new talent
More often than not, the new employees have to be trained for the job and/or given time to acclimatise themselves to the company
Hence, the management has contracted an HR analytics firm to understand what factors they should focus on, in order to curb attrition. In other words, they want to know what changes they should make to their workplace, in order to get most of their employees to stay. Also, they want to know which of these variables is most important and needs to be addressed right away.

Since you are one of the star analysts at the firm, this project has been given to you.

Goal of the case study You are required to model the probability of attrition. The results thus obtained will be used by the management to understand what changes they should make to their workplace, in order to get most of their employees to stay.

Columns
EmployeeIDEmployee number/id
EnvironmentSatisfactionWork Environment Satisfaction Level
JobSatisfactionJob Involvement Level Job Involvement Level Job Involvement Level
WorkLifeBalanceWork life balance level



"""

#importing the required library
import pandas as pd

    
#get the dataset from excel file
dataset = pd.read_excel("data_dictionary.xlsx",sheet_name = 0)

print(dataset)

#by clicking the variable explorer we can see the name, type, size.
#name - dataset; type - DataFrame; size - 52* 3 ; 52 - rows; 3 - columns


#Load csv File, no need of sheet name/ num unlike in excel
generalDataSet = pd.read_csv("general_data.csv")
print(generalDataSet)

#Here we have 4410 rows; 24 columns

#Will fetch the result of first value in the dataset, if we need first 3 ,add head(3)
print(generalDataSet.head(1))


#get the last 5 values using tail function
print(generalDataSet.tail())

#Get the info of the dataset
print(generalDataSet.info())


#Using descriptive analysis,We will find the central tendency of the data set
monthlyIncomeMean = generalDataSet["MonthlyIncome"].mean()
print("Mean:-",monthlyIncomeMean)
#Avg mean = 65029.31

monthlyIncomeMedian = generalDataSet['MonthlyIncome'].median()
print("Median:-",monthlyIncomeMedian)


monthlyIncomeMode = generalDataSet['MonthlyIncome'].mode()
print("Mode:-",monthlyIncomeMode)


#combining multiple parameters
meanExperienceYearsAtComp = generalDataSet[["TotalWorkingYears","YearsAtCompany"]].mean()
print(meanExperienceYearsAtComp)

#To find the mode of the years at company
modeExperienceYearsAtComp = generalDataSet[["TotalWorkingYears","YearsAtCompany"]].mode()
print(modeExperienceYearsAtComp)



#Varaince in monthly income:
monthlyIncomeVariance = generalDataSet["MonthlyIncome"].var()
print("Monthly income variance:",monthlyIncomeVariance)


#To find the consistency - std()-Standard Deviation
monthlyIncomeStdDeviation = generalDataSet["MonthlyIncome"].std()
print("Monthly income Std Deviation:",monthlyIncomeStdDeviation)


#describe() - We can count, mean, std,var,min,first, sec,third quarentile,max ranges.
print(generalDataSet[["TotalWorkingYears","YearsAtCompany"]].describe())


#Skewness -symmetry - positive,negative or no skew
#-The result shows the data set is positively skewed. (mean > median)
#Normal distribution.
print("Skewness:-",generalDataSet[["TotalWorkingYears","YearsAtCompany"]].skew())

#Kritosis : - To find the peakness- leptokurtic, mesokurtic, platykurtic
#o/p is - 0.91; 3.923 - THe peakness is positive - leptokurtic
print("Kurtosis:",generalDataSet[["TotalWorkingYears","YearsAtCompany"]].kurt())



#To find outliers 
# 1.Box Plot; 2.Scatter Plot
#Import matplotlib

import matplotlib.pyplot as mPlot

boxPlotValue = mPlot.boxplot(generalDataSet.MonthlyIncome) 

print(boxPlotValue)

scatterPlot = mPlot.scatter(generalDataSet.MonthlyIncome, generalDataSet.YearsAtCompany)
print(scatterPlot)

histoPlot = mPlot.hist(generalDataSet.MonthlyIncome)

print(histoPlot)





