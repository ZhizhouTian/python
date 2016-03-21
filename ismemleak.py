import os
import re
import datetime
try:
	import pandas.io.data as pd
except:
	if platform.system() == "Linux":
		os.system("sudo pip install pandas")
	else:
		os.system("pip install pandas")
	import pandas.io.data as pd

try:
	import statsmodels.formula.api as sm
except:
	if platform.system() == "Linux":
		os.system("sudo pip install statsmodels")
	else:
		os.system("pip install statsmodels")
	import statsmodels.formula.api as sm

try:
	import matplotlib.pyplot as plt
except:
	if platform.system() == "Linux":
		os.system("sudo pip install matplotlib")
	else:
		os.system("pip install matplotlib")
	import matplotlib.pyplot as plt

class Report(object):
	losts = []

'''
Parameters:
	filename: file path and name include memory lost data
Return:
	0: there is not any memory leak 
	1: there are memory leaks
'''
def ismemleak(filename):
	report = Report()
	if not os.path.exists(filename):
		raise Exception("%s does not exists")
	with open(filename) as filp:
		line = filp.readline()
		while line:
			if "lost:" in line:
				lostvals = re.findall(r"\d+", line)
				report.losts.append(float(lostvals[0])/1000.0)
			line = filp.readline()
	# get a DataFrame with lost datas
	df = pd.DataFrame({"lost":report.losts, "idx":range(1, len(report.losts)+1)})
	
	# fit a linear regression
	fit = sm.ols(formula="idx ~ lost", data=df).fit()
	predict = fit.predict(df)
	df['fitted'] = predict
	print df

	# plot
	fig, ax = plt.subplots(figsize=(8,4))
	ax.scatter(df.idx, df.lost)
	ax.plot(df.idx, df.fitted, 'r')
	plt.show()
	print df

def main():
	ismemleak("final_report_mm.txt")

if __name__ == "__main__":
	main()
