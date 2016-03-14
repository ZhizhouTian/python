#!/usr/bin/python
from __future__ import print_function

import sys
import xdrlib
import os.path
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

def main():
	report_xls = "./report.xls"
	report_txt = "./report.txt"
	if os.path.exists(report_xls):
		os.remove(report_xls)
	
	book = xlwt.Workbook(encoding='utf-8', style_compression=0)
	sheet = book.add_sheet('test_sheet', cell_overwrite_ok=True)

	row = 0
	col = 0

	sheet.write(row, col, 'id')
	row += 1

	for i in range(100):
		sheet.write(row, col, i)
		row += 1

	book.save(report_xls)

if __name__ == "__main__":
	main()
