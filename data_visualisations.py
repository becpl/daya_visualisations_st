#Perform advanced level data visualisation using plotly and seaborn to project charts on to streamlit app for dataset provided for assignment
# 4. Make min of 3 different visualisations.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 21:35:24 2021
@author: ayeshauzair
"""

# Apply the pandas methods and functions along with profiling and interpret your findings from given dataset.

import pandas as pd
import pandas_profiling as pp
from matplotlib import pyplot as plt
import seaborn as sns
import plotly_express as px
import streamlit as st


df = pd.read_csv("Mall_Customers.csv")

print("\n\n--------------------------------------------------------------------------")
print("Top 5 rows ")
print("--------------------------------------------------------------------------\n")
print(df.head(5))


print("\n\n--------------------------------------------------------------------------")
print("Bottom 5 rows ")
print("--------------------------------------------------------------------------\n")
print(df.tail(5))


print("\n\n--------------------------------------------------------------------------")
print("DataFrame Info ")
print("--------------------------------------------------------------------------\n")
print(df.info())
print("\n\n")
print("There are 5 columns in this dataframe with 200 non-null values in each. The Genre (Gender) column is categorical, whereas all others have numerical values.")


print("\n\n--------------------------------------------------------------------------")
print("Column Names ")
print("--------------------------------------------------------------------------\n")
print(df.columns)
print("\n\n")
print("Since the Gender column name is mis-spelled, we have renamed it from Genre to Gender.")
print("\n")
df = df.rename(columns = {'Genre':'Gender'})
print("CHECK: Genre is replaced with Gender in the column names")
print(df.columns)


print("\n\n--------------------------------------------------------------------------")
print("DataFrame Description ")
print("--------------------------------------------------------------------------\n")
print(df.describe())
print("\n\n")
print("Statistical evaluation of all numerical columns present in the dataframe.")
print("\n\n")

print("\n\n--------------------------------------------------------------------------")
print("Null Values ")
print("--------------------------------------------------------------------------\n")
print(df.isnull().sum())
print("As suggested by the dataframe info, there are no null columns.")


print("\n\n--------------------------------------------------------------------------")
print("Statistical Analysis: Mean Values of all columns ")
print("--------------------------------------------------------------------------\n")
mean_1 = df['Annual Income (k$)'].mean()
mean_2 = df['Spending Score (1-100)'].mean()
mean_3 = df['Age'].mean()
print("Mean Annual Income (k$) : ", mean_1)
print("Mean Spending Score (1-100) : ", mean_2)
print("Mean Age =", mean_3)
print("\n\n")
print("The mean values match the statistical evaluation given by the .describe() command.")



print("\n\n--------------------------------------------------------------------------")
print("Statistical Analysis: Median Values of all columns ")
print("--------------------------------------------------------------------------\n")
median_1 = df['Annual Income (k$)'].median()
median_2 = df['Spending Score (1-100)'].median()
median_3 = df['Age'].median()
print("Median Annual Income (k$) : ", median_1)
print("Median Spending Score (1-100) : ", median_2)
print("Median Age =", median_3)


print("\n\n--------------------------------------------------------------------------")
print("Statistical Analysis: Mode Values of all columns ")
print("--------------------------------------------------------------------------\n")
mode_1 = df['Annual Income (k$)'].mode().tolist()
mode_2 = df['Spending Score (1-100)'].mode().tolist()
mode_3 = df['Age'].mode().tolist()
print("Mode Annual Income (k$) : ", mode_1)
print("Mode Spending Score (1-100) : ", mode_2)
print ("Mode Age =", mode_3)



print("\n\n--------------------------------------------------------------------------")
print("Statistical Analysis: Group by Categorical Column i.e. Gender ")
print("--------------------------------------------------------------------------\n")
mean_income_gender = df.groupby("Gender")["Annual Income (k$)"].mean()
print("Mean Income by Gender : ", mean_income_gender)
print("\n\n")
mean_spending_gender = df.groupby("Gender")["Spending Score (1-100)"].mean()
print("Mean Spending by Gender : ", mean_spending_gender)
print("\n\n")
print("Male gender generally earns more income than Female gender. However, female gender has a higher spending score, indicating that female gender tends to spend more than male gender.")


print("\n\n--------------------------------------------------------------------------")
print("Creating a New Categorical Column (Age Group) and analysing numerical columns ")
print("--------------------------------------------------------------------------\n")

df.loc[df["Age"]<20,"Age Group"] = "under 20"
df.loc[(df["Age"]<30)&(df["Age"]>19),"Age Group"] = "20 - 29"
df.loc[(df["Age"]<40)&(df["Age"]>29),"Age Group"] = "30 - 39"
df.loc[(df["Age"]<50)&(df["Age"]>39),"Age Group"] = "40 - 49"
df.loc[(df["Age"]<60)&(df["Age"]>49),"Age Group"] = "50 - 59"
df.loc[df["Age"]>59,"Age Group"] = "over 60"

mean_agec = pd.DataFrame(df.groupby("Age Group")["Annual Income (k$)"].mean())
print(mean_agec)
print("\n\n")
mean_spend = pd.DataFrame(df.groupby("Age Group")['Spending Score (1-100)'].mean())
print(mean_spend)
print("\n\n")

print("\n\n--------------------------------------------------------------------------")
print("Creating a New Numerical Column (Score per $ income)")
print("--------------------------------------------------------------------------\n")

df["Score per $ income"] = df["Spending Score (1-100)"] / df["Annual Income (k$)"]
mean_score_income = df["Score per $ income"].mean()
print ("Average spending score per k$ income is ",mean_score_income)


print("\n\n--------------------------------------------------------------------------")
print("A Look at the new dataframe head")
print("--------------------------------------------------------------------------\n")
print(df.head(5))


print("\n\n--------------------------------------------------------------------------")
print("A Look at the new dataframe info")
print("--------------------------------------------------------------------------\n")
print(df.info())
print("There are 7 columns in the dataframe now 200 non-null values in each. Two columns (i.e. Gender and Age Group) are categorical, whereas all other five columns have numerical values.")

# Pandas Profiling

#profile = pp.ProfileReport(df)
#profile.to_file("Summaryreport.html")



print("\n\n--------------------------------------------------------------------------")
print("Final Analysis/Interpretations ")
print("--------------------------------------------------------------------------\n")
print("1. The dataframe originally had 4 numerical columns and 1 categorical column containing the customer's id, age, gender, annual income, and a spending score for a certain mall.")
print("2. There are no null-columns present in the data.")
print("3. The average age of the customers is around 38.85 years.")
print("4. The average annual income of the customers is 60.56 k$. ")
print("5. The average spending score of the customers is 50.2 on a scale of 1-100.")
print("6. There are more females in the data sample collected than males.")
print("7. The Age column appears to be positively skewed (or very close to being normally skewed) with a skewness of 0.485568851. The kurtosis appears to be negative. This means that in the age range of 18-70, the values lie near the median of age 36.0. This is true since the average age of customers is 38.85 years.")



#setup the page with a title and a side bar where the user can choose the graph
st.title("Interactive sales dashboard")
st.write("Click on the arrow on the right hand side for filters")
dpdown = st.sidebar.selectbox("Select filter",["Income per Age Group","Spending Score/Annual Income","Age/Annual Income","Box plots Income by Age Group"])

if dpdown == "Income per Age Group":
    figbar = px.bar(df, x='Age Group', y='Annual Income (k$)')
    st.subheader("Income per Age Group")
    st.plotly_chart(figbar)
elif dpdown == "Spending Score/Annual Income":
    #qtr_figures = [fig_1q, fig_2q, fig_3q]
    #st.plotly_chart(qtr_figures)
    st.write("Scatter plot of Spending Score and Annual Income")
    figure = px.scatter(df, x="Spending Score (1-100)", y="Annual Income (k$)", color="Gender")
    st.plotly_chart(figure)
elif dpdown == "Age/Annual Income":
    #st.plotly_chart(figures_q)
    #pie chart of sales per country
    #country_values = df.groupby(["COUNTRY"])["SALES"].sum().reset_index().sort_values(by="SALES")
    #fig_pie = px.pie(country_values,values="SALES",names="COUNTRY",template="seaborn")
    #st.plotly_chart(fig_pie)
    st.write("Scatter plot of Age and Annual Income (k$)")
    figure2 = px.scatter(df, x="Age", y="Annual Income (k$)", color="Gender")
    st.plotly_chart(figure2)
elif dpdown == "Age/Annual Income":
    #how order status varies YoY (qty ordered) have to convert year from integer to string
    #order_status_values = df.groupby(["STATUS","YEAR_ID"])["QUANTITYORDERED"].sum().reset_index().sort_values(by="QUANTITYORDERED")
    #order_status_values["YEAR_ID"] = order_status_values["YEAR_ID"].astype("str")
    #fig_funnel = px.funnel(order_status_values,x="STATUS",y="QUANTITYORDERED",color="YEAR_ID")
    #st.plotly_chart(fig_funnel)
    st.write("Graph 4 will appear here")
    figure3 = px.scatter(df, x="Age", y="Spending Score (1-100)", color="Gender")
    st.plotly_chart(figure3)
elif dpdown == "Box plots Income by Age Group":
    st.write("Box plots of Annual Income by Age Group")

    #figure4 = px.pie(df,values="Annual Income (k$)" ,names="Gender")
    figure4 = px.box(df, x="Age Group", y="Annual Income (k$)", color="Gender")
    st.plotly_chart(figure4)