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

report_items = {
		"time":"Sun",
		"memfree":"MemFree",
		"cache":"Cached",
		"zramuse":"zram",
		"swapfree":"SwapFree"
		}

def main(logfile, reportfile):
	if not os.path.exists(logfile):
		raise Exception("log file %s not found"%logfile)

	if os.path.exists(reportfile):
		os.remove(reportfile)
	
	book = xlwt.Workbook(encoding='utf-8', style_compression=0)
	sheet = book.add_sheet('appmem_sheet', cell_overwrite_ok=True)

	row = 0
	col = 0

	sheet.write(row, col, "time")
	col += 1

	sheet.write(row, col, "memfree")
	col += 1

	sheet.write(row, col, "cache")
	col += 1

	sheet.write(row, col, "zramuse")
	col += 1

	sheet.write(row, col, "swapfree")
	col += 1

	row += 1

	filp = open(logfile, 'r')
	line = filp.readline()

	while line:
		newline_flag = False
		if report_items["time"] in line:
			sheet.write(row, 0, line[10:-10])
		elif report_items["memfree"] in line:
			sheet.write(row, 1, re.search(r'\d+', line).group())
		elif report_items["cache"] in line:
			sheet.write(row, 2, re.search(r'\d+', line).group())
		elif report_items["zramuse"] in line:
			line = filp.readline()
			sheet.write(row, 4, line[:-2])
		elif report_items["swapfree"] in line:
			sheet.write(row, 3, re.search(r'\d+', line).group())
			newline_flag = True

		line = filp.readline()
		if newline_flag:
			row += 1
		
	book.save(reportfile)

if __name__ == "__main__":
	main("./appmem.log", "./report_appmem.xlsx")
