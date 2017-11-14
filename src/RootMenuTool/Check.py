#!coding:utf8

'''
Date:2017/10/11/16:42
Author:yqq
Description: 检查菜单是否有错
'''

import  os



def Check(fileName, inList):
	'''
	:param fileName: 当前正在检查的文件的文件名
	:param inList: 文件内容
	:return: 有错返回False, 否则返回True
	'''

	for i in range(len(inList)):
		eachLine = inList[i]
		if i + 1 == len(inList):
			if "<0x" not in eachLine:
				print("{0} line{1} : {2}\n".format(fileName , i, inList[i].strip()))
				return False
			else:
				continue
		if ("<0x" not in eachLine ): #如果没有"<0x", 那么, 它的下一行的tab数一定大于当前行的tab数
			if inList[i+1].count('\t') <= inList[i].count('\t'):
				print("{0} line{1} : {2}\n".format(fileName , i, inList[i].strip()))
				return False
		else: #如果有"<0x", 那么, 它的下一行的tab一定不大于当前行的tab数
			if inList[i+1].count('\t') > inList[i].count('\t'):
				print("{0} line{1} : {2}\n".format(fileName , i, inList[i].strip()))
				return False
	pass






def main():

	menuDir = "../../doc/tmp/RootMenu_New/"
	for eachFileName in os.listdir(menuDir) :

		with open(os.path.join(menuDir, eachFileName), "r") as inFile:
			linesList = inFile.readlines()
			Check(eachFileName, linesList)


	pass


if __name__ == "__main__":

	main()

	pass