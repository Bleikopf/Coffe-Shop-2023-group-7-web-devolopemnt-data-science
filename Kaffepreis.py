import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression

data = pd.read_csv('C:\\PythonTechLabs-Project\\Kaffeepreis.csv', header=None, delimiter=';')

data[['Datum', 'Preis']] = data[0].str.split(',', expand=True)
data.drop(columns=[0], inplace=True)

data['Datum'] = pd.to_datetime(data['Datum'], format='%Y-%m-%d', errors='coerce')
data['Preis'] = data['Preis'].astype(float)
data = data.sort_values(by='Datum')


date_str = input("Please type in the Date like JJJJ-MM-TT: ")
date = datetime.strptime(date_str, '%Y-%m-%d')


X = data[data['Datum'] < date]['Datum'].values.reshape(-1, 1)
y = data[data['Datum'] < date]['Preis'].values


regressor = LinearRegression()
regressor.fit(X, y)

# First we only need the prices (values[0]) and only for the dates in the past (data[data['Datum'] < date].tail(1))

last_price = data[data['Datum'] < date].tail(1)['Preis'].values[0]

# the regression model takes the predict price and compares with the last price. Than it takes the max value of both prices
predicted_price = max(regressor.predict([[date.timestamp() * 1000]])[0], last_price)


print("The estimate coffee price", date_str, "is:", predicted_price, "USD")

coffeprice = predicted_price