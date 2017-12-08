#!coding:utf8

'''
Date:2017/12/5/15:13
Author:yqq
Description:  生成 车型表    ECU表
'''

import os
from  lib.mytool12 import RootMenu
from lib.mytool12 import JoinDir

menuDirPath = "../../txt/Rootmenu/"
outPath = "../../doc/tmp/CarTable/"

def main():

	if not os.path.exists(menuDirPath):
		raise ValueError

	if not os.path.exists(outPath):
		os.makedirs(outPath)

	for eachMenu in os.listdir(menuDirPath):
		rm = RootMenu(os.path.join(menuDirPath, eachMenu))
		# rm.ShowAll()
		with open(os.path.join(outPath, eachMenu), "w") as outFile:
			rm.HereditaryTraverse(outFileObj= outFile)

	pass


if __name__ == "__main__":

	main()
	JoinDir(outPath, os.path.join("../../doc/tmp", u"中国通用车型表.txt"))

	pass