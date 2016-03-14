#!/usr/bin/python
from __future__ import print_function
import os
import sys
import xml.etree.ElementTree as et

CONFIGS = None

class Configs(object):
	''' Abstrace interface '''
	def set_cfg(this, c):
		raise Exception("Should have implemented this")
	@staticmethod
	def get(cft_typ):
		if cfg_typ not in CONFIGS:
			raise Exception("E: Unknow config type")
		return CONFIGS[cft_typ]

class MemConfig(Configs):
	forders = []
	def set_cfg(this, c):
		items = c.findall("item")
		for i in items:
			this.forders.append(i.text)

class FtpConfig(Configs):
	def set_cfg(this, c):
		pass

class CmdConfig(Configs):
	def set_cfg(this, c):
		pass

CONFIGS = {"memory":MemConfig(), "ftp":FtpConfig(), "cmdline":CmdConfig()}

CONFIG_FILE="./config.xml"

if not os.path.exists(CONFIG_FILE):
	raise Exception("E: Can not find %s"%CONFIG_FILE)
else:
	root = et.parse(CONFIG_FILE).getroot();

config_nodes = root.find("configs").findall("config")

for c in config_nodes:
	cfg_typ = c.get("type")
	if cfg_typ not in CONFIGS:
		raise Exception("E: Unknow type in config.xml")
	CONFIGS[cfg_typ].set_cfg(c)

	
def main():
	memcfg = Configs.get("memory")
	print(memcfg.forders)

if __name__ == "__main__":
	main()
