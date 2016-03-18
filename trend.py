# get some data
import pandas.io.data as web
import datetime
start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2016, 2, 29)
df=web.DataReader("F", 'yahoo', start, end)

# a bit of munging - better column name - Day as integer 
df = df.rename(columns={'Adj Close':'AdjClose'})
df['Day'] = range(len(df))

# fit a linear regression
import statsmodels.formula.api as sm
fit = sm.ols(formula="AdjClose ~ Day", data=df).fit()
print(fit.summary())
predict = fit.predict(df)
df['fitted'] = predict

# plot
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8,4))
ax.scatter(df.index, df.AdjClose)
ax.plot(df.index, df.fitted, 'r')
ax.set_ylabel('$')
fig.suptitle('Yahoo')

plt.show()
