import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

pd.display_max_columns = None
pd.display_max_rows = None

df = pd.read_csv('data/csv_wranged.csv')
df = df[['year', df.columns[-2], df.columns[-1]]][1:]

# Convert the 'year' column to strings
df['year'] = df['year'].astype(str)


X = df[['year']]
y_inflation_growth = df['inflation_growth']
y_salary_growth = df['salary_depend']

# For inflation growth prediction
inflation_model = LinearRegression()
inflation_poly = PolynomialFeatures(degree=2)  # You can experiment with different degrees
X_inflation_poly = inflation_poly.fit_transform(X)
inflation_model.fit(X_inflation_poly, y_inflation_growth)

# For salary growth prediction
salary_model = LinearRegression()
salary_poly = PolynomialFeatures(degree=2)  # You can experiment with different degrees
X_salary_poly = salary_poly.fit_transform(X)
salary_model.fit(X_salary_poly, y_salary_growth)

# Assuming 'future_years' is a list of years for which you want predictions
future_years = [str(year) for year in range(2024, 2051)]  # Convert future years to strings

# Creating a DataFrame for future years
future_data = pd.DataFrame({'year': future_years})

# Transforming the future data using polynomial features
future_data_inflation_poly = inflation_poly.transform(future_data)
future_data_salary_poly = salary_poly.transform(future_data)

# Predicting inflation growth for future years
future_inflation_predictions = inflation_model.predict(future_data_inflation_poly)

# Predicting salary growth for future years
future_salary_predictions = salary_model.predict(future_data_salary_poly)

# Adding the predictions to the 'future_data' DataFrame
future_data['inflation_growth'] = future_inflation_predictions
future_data['salary_depend'] = future_salary_predictions

result_df = pd.concat([df, future_data], ignore_index=True)
print(result_df)

result_df.to_csv('data/inflation_final.csv')
