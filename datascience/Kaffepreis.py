import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

data = pd.read_csv('Kaffeepreis.csv', parse_dates=['Datum'])
data = data.set_index('Datum')

data = data.resample('M').mean()
data = data['1973':]

train_size = int(len(data) * 0.8)
train, test = data[:train_size], data[train_size:]

model = ARIMA(train, order=(1, 1, 1))
model_fit = model.fit()
forecast = model_fit.forecast(steps=60)

plt.plot(train, label='Trainingsdaten')
plt.plot(test, label='Testdaten')
plt.plot(forecast, label='Vorhersage')
plt.legend()
plt.show()

avg_1yr_price = forecast[:12].mean()
avg_5yr_price = forecast[:60:12].mean()

forecast_df = pd.DataFrame({'1Jahr': [avg_1yr_price], '5Jahr': [avg_5yr_price]})
forecast_df.to_csv('Coffeeprice_forecast.csv', index=False)
