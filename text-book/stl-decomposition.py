import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import STL

# Example: Using AirPassengers dataset
import statsmodels.api as sm

# https://vincentarelbundock.github.io/Rdatasets/articles/data.html
data = sm.datasets.get_rdataset("AirPassengers", "datasets").data
data['time'] = pd.date_range(start='1949-01', periods=len(data), freq='ME')
# You should pass a pandas Series with a DatetimeIndex as the index,
# and specify the period parameter explicitly if it can't be inferred.
data.set_index('time', inplace=True)

# STL decomposition
stl = STL(data['value'], seasonal=13)
result = stl.fit()

# Plot the decomposition
result.plot()
plt.show()
