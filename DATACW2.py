#Import necessary libraries
import pandas as pd
import janitor
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import statsmodel.api as sm

# load data 
df = pd.read_excel (r"C:\Users\Serah\Downloads\Data_CW2.xlsx")
print(df.head())

#Cleaning data 
def decimal_year_date(decimal_year):
    year = int(decimal_year)
    start = datetime(year, 1, 1)
    end = datetime(year+1,1 , 1)
    days_in_year =(end - start).days
    frac = decimal_year - year
    return start + timedelta( days= int(frac*days_in_year))


df["sale date"]= df["sale date"]. apply(decimal_year_date)

df
# Missing variables
df.isnull().sum()

#descriptive statistics
df.describe()

X = df[['sale_date', 'model_age', 'proximity_log', 'number_of_dealerships_nearby']]
y = df['vechicle_sale_price']
    



