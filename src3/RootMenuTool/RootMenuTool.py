#!coding:utf8

'''
Date:2018/1/2/10:51
Author:yqq
Description:  分高低配 

算法设计:

	      如果当前节点的子节点中有(版本信息,故障码,数据流)这样的 "叶子"
	          那么, 他的父节点 , 必定是  系统名
	          如果  系统名 在保留列表中:
	              则保留
	          否则:
	              将当前节点 及其 子节点屏蔽掉

'''

from  lib.mytool12 import RootMenu
from lib.mytool12 import Add0x
from  lib.mytool12 import Del0x

import  os

gKeepList = ["发动机", "马达","电动机","充气", "刹车", "变速箱", "变速器", "气囊", "防抱死", "ABS"]

gInDir = u"../../txt/中国通用/RootMenu/"
gOutDir =  u"../../doc/tmp/RootMenu_1_2/"


gLeafList = ["版本信息", "数据流", "故障码", "设定选装件"]


def InList(inStr, inList):

	for item in  inList:
		if item in inStr:
			return True
	return False


def HasLeafNode(inDict):

	for k, v in inDict.items():
		# if isinstance(v, list):
		# 	return  True
		if InList(k, gLeafList) :
			return  True
	return False



def GetSysName(inDict):
	sysName = inDict.keys()[0]
	return  sysName




def WriteCurAndChild(outFile, inDict, tabCount = 0, isDel=False):

	if isinstance(inDict, list):
		return

	elif isinstance(inDict, dict):
		for key, value in inDict.items():
			if isinstance(value, list):
				if isDel:
					#print("//{0}{1}<{2}>".format('\t' * tabCount, key, value[0]))  # 叶子节点,ECU
					outFile.write("//{0}{1}<{2}>\n".format('\t' * tabCount, key, value[0]))  # 叶子节点,ECU
				else:
					#print("{0}{1}<{2}>".format('\t' * tabCount, key, value[0]))  # 叶子节点,ECU
					outFile.write("{0}{1}<{2}>\n".format('\t' * tabCount, key, value[0]))  # 叶子节点,ECU
			else:
				if isDel:
					#print("//{0}{1}".format('\t' * tabCount, key))  # 系统
					outFile.write("//{0}{1}\n".format('\t' * tabCount, key))  # 系统
				else:
					#print("{0}{1}".format('\t' * tabCount, key))  # 系统
					outFile.write("{0}{1}\n".format('\t' * tabCount, key))  # 系统

			WriteCurAndChild(outFile, value, tabCount + 1, isDel)  # 继续递归

	else:  # 参数类型错误
		print(type(inDict))
		raise ValueError
	pass



def IsEcuID(inDict):

	if len(inDict) != 1:
		return False

	for k, v in inDict.items():
		if isinstance(v, list):
			return True
	return False



def Deal2(outFile, inDict, tabCount = 0):

	'''
	如果当前节点的  "子节点" 中有(版本信息,故障码,数据流)这样的 "叶子"
	          那么, "当前根节点" , 必定是  系统名
	          如果  系统名 在保留列表中:
	              则保留
	          否则:
	              将当前节点 及其 "后代节点" 屏蔽掉
	'''

	if isinstance(inDict, list):
		print('************************')
		return

	for key, value in inDict.items():
		sysName = key

		if isinstance(value, list):
			# print('***********list***********')
			print("{0}{1}{2}".format(tabCount * '\t', sysName, value[0]))
			outFile.write("{0}{1}<{2}>\n".format(tabCount * '\t', sysName, value[0]))
			continue

		if HasLeafNode(value):

			if  InList(sysName, gKeepList):
				#写入文件
				#print("{0}{1}".format(tabCount * '\t',    sysName))
				outFile.write("{0}{1}\n".format(tabCount * '\t',    sysName))
				WriteCurAndChild(outFile, value, tabCount + 1, isDel=False)
				pass
			else:
				#屏蔽掉
				outFile.write("//{0}{1}\n".format(tabCount * '\t',    sysName))
				#print("//{0}{1}".format(tabCount * '\t',    sysName))
				WriteCurAndChild(outFile, value, tabCount + 1, isDel=True)
				pass
		else:
			#写入文件
			#print("{0}{1}".format(tabCount * '\t',    sysName))

			if IsEcuID(value):
				outFile.write("//{0}{1}\n".format(tabCount * '\t',    sysName))
				WriteCurAndChild(outFile, value, tabCount + 1, isDel=True)
				pass
			else:
				outFile.write("{0}{1}\n".format(tabCount * '\t',    sysName))
				Deal2(outFile, value, tabCount + 1)
				pass
	pass



def main():

	for fileName in os.listdir(gInDir):
		#print(fileName)
		filePath = os.path.join(gInDir, fileName)

		inFilePath = filePath
		fileName = os.path.split(inFilePath)[1]
		outFilePath = os.path.join(gOutDir, fileName)
		with open(outFilePath, "w") as outFile:
			rm = RootMenu(inFilePath)
			#if "2016" in outFilePath:
			#	rm.ShowAll()
			inDict = rm.menuDict
			Deal2(outFile, inDict, 0)

	pass


if __name__ == "__main__":

	main()

	pass