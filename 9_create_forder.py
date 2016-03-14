#!/usr/bin/python
from __future__ import print_function
import getopt
import os
import sys
import shutil

class UserOperations(object):
	log_dir = os.getcwd()

	def __init__(this):
		log_dir = os.getcwd()

	def __str__(this):
		return 'log_dir: '+this.log_dir

	def set_log_dir(this, path_arg='.'):
		if not os.path.exists(path_arg):
			return -1
		this.log_dir = os.path.abspath(path_arg)
		return 0

class Report(object):
	report_dir = None

	def __init__(this):
		this.report_dir = os.getcwd()

	def __str__(this):
		return 'report_dir: '+this.report_dir

	def create_report_dir(this, log_dir):
		if not os.path.exists(log_dir):
			return -1
		this.report_dir = log_dir + os.path.sep + "report"
		if os.path.exists(this.report_dir):
			shutil.rmtree(this.report_dir)
		os.makedirs(this.report_dir)
		return 0

def usage(argv):
	print("Usage: %s [-h | --help] [--log-dir dir]"%argv[0])
	return

def main(argc, argv):
	if argc <= 1:
		usage(argv)
		return 0

	try:
		opts, args = getopt.getopt(argv[1:], 'h', ['help', 'log-dir='])
	except getopt.GetoptError:
		print("E: Invalid argument", file=sys.stderr)
		return -1

	user_opt = UserOperations()
	report = Report()

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage(argv)
			return 0
		if opt in '--log-dir':
			if user_opt.set_log_dir(arg) != 0:
				print("E: Invalid log dir", file=sys.stderr)
				return -1
	if report.create_report_dir(user_opt.log_dir) != 0:
		print("E: Create report dir failed", file=sys.stderr)
		return -1
	return 0

if __name__ == "__main__":
	main(len(sys.argv), sys.argv)
