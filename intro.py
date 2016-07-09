import pandas as pd
import Quandl
import math
from sklearn import preprocessing as ppr \
    , cross_validation as cvd, svm
from sklearn.linear_model import LinearRegression as \
    linred


df = Quandl.get("WIKI/GOOGL")

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# defininf features
df['HL_PCT'] = ((df['Adj. High'] - df['Adj. Close']) / df['Adj. Close']) * 100
df['PCT_change'] = ((df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']) * 100

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
# print (df.head())  #printing the features

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

# predicting 1% of the dataframe
forecast_out = int(math.ceil(0.01 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())
