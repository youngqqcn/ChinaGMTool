#!coding:utf8

'''
Date:2018/1/3/9:55
Author:yqq
Description:  删除个别不开发的菜单
'''

gDelList = ["检查/保养数据", "获取信息", "配置/复位功能"]


gHighDir = u"../../txt/中国通用/RootMenu/"
gNormalDir = u"../../txt/中国通用/RootMenu_1_2_m"

gOutHighDir = u"../../doc/tmp/1_3/RootMenu/"
gOutNormalDir = u"../../doc/tmp/1_3/Normal_RootMenu/"



import os

from lib.mytool12 import InList


def Deal(inDirPath, outDirPath):

	for fileName in  os.listdir(inDirPath):
		filePath = os.path.join(inDirPath, fileName)
		outFilePath = os.path.join(outDirPath, fileName)
		with open(filePath, "r") as inFile, open(outFilePath, "w") as outFile:
			lines = inFile.readlines()
			for i in range(len(lines)):
				line = lines[i]
				if InList(line, gDelList):
					lines[i] = "//" + line
			outFile.writelines(lines)

	pass



def main():

	if not os.path.exists(gOutHighDir):
		os.makedirs(gOutHighDir)
	if not os.path.exists(gOutNormalDir):
		os.makedirs(gOutNormalDir)

	Deal(gHighDir, gOutHighDir)
	Deal(gNormalDir, gOutNormalDir)

	pass


if __name__ == "__main__":

	main()

	pass