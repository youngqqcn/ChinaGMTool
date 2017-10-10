#!coding:utf8

'''
Date:2017/10/10/13:44
Author:yqq
Description: 删除没用的菜单项,减少菜单深度
'''

import os


gDirName = "../../txt/RootMenu"
gFilterList = []


# def DelCommantedLine():
# 	'''
# 	删除已经屏蔽掉的行, 即 以"//"开头的行
# 	:return:
# 	'''
#
# 	for eachFileName in os.listdir(gDirName) :
# 		eachFilePath =  os.path.join(gDirName, eachFileName)
#
# 		inFile = open(eachFilePath, "r")
# 		lineList = inFile.readlines()
# 		inFile.close()
#
# 		with open(eachFilePath, "w") as outFile:
# 			for eachLine in lineList:
# 				if r"//" in eachLine:
# 					continue #不写回
# 				else:
# 					outFile.write(eachLine) #写回去
# 	pass


def DelOneTab(inList, begin):
	'''
	:param i:  从inList[i]开始, 后面tab
	:return: 
	'''
	if len(inList) == 0:
		return
	tabCount = inList[begin].count('\t')

	for i in range(begin , len(inList) ):
		if (inList[i].count('\t') <= tabCount) and (i != begin):
			break
		else:
			inList[i] = inList[i].replace('\t'*inList[i].count('\t'), '\t' * (inList[i].count('\t')- 1) )   #减少一个tab键
	pass



def Judge(line):
	'''
	:param line: 
	:return: 
	'''

	for delMenuName in  gFilterList :
		#if delMenuName in line:
		#	return True
		if delMenuName.strip() == line.strip():
			return True

	return False



def Filter():
	'''
	 处理菜单文件, 删除无用菜单项
	:return: 
	'''

	for eachFileName in os.listdir(gDirName):
		eachFilePath = os.path.join(gDirName, eachFileName)

		outFile = open("../../doc/tmp/RootMenu/" + eachFileName, "w")

		with open(eachFilePath, "r") as inFile:
			lineList  = inFile.readlines()
			for i in range(len(lineList)):
				if Judge(lineList[i]):
					DelOneTab(lineList, i)   #将从下表i开始, 到tab键小于或等于这一行的tab键的某行结束
					continue
				outFile.write(lineList[i])

		outFile.close()

	pass



def main():

	#DelCommantedLine()    #只用一次


	with open("../../txt/DelMenuName.txt", "r") as inFile:
		while True:
			line  = inFile.readline()
			if len(line.strip()) == 0:
				break
			gFilterList.append(line.strip())

	Filter()


	pass


if __name__ == "__main__":

	main()

	pass