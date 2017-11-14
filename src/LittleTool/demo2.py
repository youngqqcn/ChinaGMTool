
#!coding:utf8

'''
Date:2017/11/1/16:54
Author:yqq
Description: 故障码功能有4个选项, 只保留 "读取故障码"
				读取故障码
				查询故障码
				自清除后未运行的代码
				诊断测试状况
'''

gIndexDict = {}


def GetMenuIndex(inFilePath):

	with open(inFilePath, "r") as inFile:
		linesList = inFile.readlines()
		for line in linesList:
			if '<0x' in line:
				name = line.strip()[ : line.strip().find('<0x')]
				index = line.strip()[line.strip().find('<0x') + 1 : -1]

				if index not in gIndexDict:
					gIndexDict[index] = [name]
				elif name not in gIndexDict[index]:
					gIndexDict[index].append(name)
				else:
					pass
	pass



def main():

	import  os
	menuPath = u"../../txt/RootMenu/"
	for fileName in os.listdir(menuPath):
		filePath = os.path.join(menuPath, fileName)
		GetMenuIndex(filePath)

	outFile = open("../../doc/outIndex.txt", "w")
	with open("../../txt/index.txt", "r") as inFile:
		linesList = inFile.readlines()
		for line in linesList:
			#if len(line.strip()) == 0:
			#	outFile.write("   \n")
			index = line.strip()
			if index in gIndexDict:
				for item in gIndexDict[index]:
					outFile.write("{0}\t".format(item))
			outFile.write(" \n")


	outFile.close()

	pass



if __name__ == "__main__":

	main()

	pass