# We import the pandas library with the alias pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# (a)
# We store the path to the csv file as string inside the variable file
file = r'http://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv'

# We make our csv file a Pandas dataframe with the .read_csv() method
unrate_df = pd.read_csv(file) 

# We print the first 5 rows with the .head() method
print(unrate_df.head())



# (b)
# DATE column is of type object we will make it type datetime
print(unrate_df.dtypes) # Check the type of values we have in our columns

unrate_df['DATE'] = pd.to_datetime(unrate_df['DATE'], format='%Y-%m-%d')

# Once again we print the type of the values in the column and the DATE
# now is datetime type
print(unrate_df.dtypes)


# We group by year
unrate_series_group = unrate_df.groupby(unrate_df.DATE.dt.year)['VALUE'].mean() 

# We make the the series a pandas dataframe
unrate_df_group = unrate_series_group.to_frame()


# We reset the index which is the DATE
unrate_df_group = unrate_df_group.reset_index()
print(unrate_df_group)


unrate_df_group['VALUE'].hist()
plt.xlabel('AVERAGE VALUE') # Add label to x axis
plt.ylabel('DISTRIBUTION') # Add label to y axis


# (c)

"""
The least-squares regression method is a technique commonly used 
in Regression Analysis. It is a mathematical method used to find 
the best fit line that represents the relationship between 
an independent and dependent variable.


y: dependent variable
m: the slope of the line
x: independent variable
c: y-intercept

"""


X = unrate_df_group.iloc[:, 0] # Take the data from first column
Y = unrate_df_group.iloc[:, 1] # Take the data from the second column
plt.scatter(X,Y) # Create a scatter plot

X_mean = np.mean(X) # Calculate the mean value over DATES column
Y_mean = np.mean(Y) # Calculate the mean value over VALUES column

num = 0
den = 0 

"""
Below we calculate the slope and the y-intercept

At every loop we substract from every element of X the X_mean and
from every element of Y the Y_mean.
Then we add at den variable the substraction of every element of X with X_mean at 
the powe of 2
"""
for i in range(len(X)):
    num += (X[i] - X_mean)*(Y[i] - Y_mean)
    den += (X[i] - X_mean)**2


m = num / den # We calculate the slope of the line 
c = Y_mean - m*X_mean # We calculate the y-intercept

print (m, c)


# Making predictions
Y_pred = m*X + c

plt.scatter(X, Y) # Create a scatter plot with the actual averages
# plt.scatter(X, Y_pred, color='red')
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red') # The red line is the predicted values
plt.show()


























