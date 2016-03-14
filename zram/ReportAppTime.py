#!/usr/bin/python
from __future__ import print_function
import os.path
import sys
import xdrlib
import os.path
import re
try:
	import xlrd
except:
	print("E: need to install xlrd", file=sys.stderr)
	os.system("pip install xlrd")
	import xlrd
try:
	import xlwt
except:
	print("E: need to install xlwt", file=sys.stderr)
	os.system("pip install xlwt")
	import xlwt

	'''com.tencent.news/com.tencent.news.activity.SplashActivity'''
applist = {
	'com.tencent.news',
	'com.tmall.wireless',
	'com.autonavi.minimap',
	'com.jingdong.app.mall',
	'com.moji.mjweather',
	'com.tencent.mobileqq',
	'com.mymoney',
	'com.taobao.taobao',
	'com.tencent.mm',
	'com.wochacha'
	}

def main(logfile, reportfile):
	if not os.path.exists(logfile):
		raise Exception("log file %s not found"%logfile)

	if os.path.exists(reportfile):
		os.remove(reportfile)
	
	book = xlwt.Workbook(encoding='utf-8', style_compression=0)
	sheet = book.add_sheet('appmem_sheet', cell_overwrite_ok=True)

	filp = open(logfile, 'r')
	line = filp.readline()

	for appname in applist:
		print(appname),
		while line:
			if "am_activity_launch_time" in line:
				if appname in line:
					#if "SplashActivity" not in line:
					print(line)
			line = filp.readline()
	book.save(reportfile)

if __name__ == "__main__":
	main("./0-events-01-01-08-24-22.log", "./report_apptime.xlsx")
