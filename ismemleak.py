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
			if "lost_ration" in line:
				lostvals = re.findall(r"\d+\.\d+", line)
				report.losts.append(float(lostvals[0])*1000)
			line = filp.readline()
	# get a DataFrame with lost datas
	dflen = len(report.losts)
	df = pd.DataFrame({"lost":report.losts, "idx":range(dflen)})
	
	# fit a linear regression
	fit = sm.ols(formula="lost ~ idx", data=df).fit()
	predict = fit.predict(df)
	df['fitted'] = predict

	ydelta = float(df['fitted'][dflen-1] - df['fitted'][0])
	xdelta = int(df['idx'][dflen-1] - df['idx'][0])
	ret = ydelta/xdelta

	# plot
	fig, ax = plt.subplots(figsize=(8,4))
	#ax.scatter(df.idx, df.lost)
	ax.plot(df.idx, df.lost, 'b')
	ax.plot(df.idx, df.fitted, 'r')
	plt.show()
	if ret > 1:
		return 1
	else:
		return 0

def main():
	i = 0
	for i in range(6):
		ret = ismemleak("final_report_mm"+str(i)+".txt")
		if ret == 0:
			print "no memory leak"
		else:
			print "memory leak"
	'''
	ismemleak("final_report_mm"+str(i)+".txt")
	'''

if __name__ == "__main__":
	main()
