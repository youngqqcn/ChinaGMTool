#!coding:utf8

'''
Date:2018/1/4/10:01
Author:yqq
Description:

	检查 版本信息库中   的   Menu    
	是否有二级菜单

'''

from lib.mytool12 import TextTool
from lib.mytool12 import Del0x


def main():

	indexList = []
	with open(u"../../txt/版本信息的索引.txt") as inFile:
		for line in inFile.readlines():
			indexList.append(line.strip())


	tt = TextTool(u"../../txt/中国通用/Type1/Information.txt")

	#tt.ShowAll()
	# def ShowAll(self):
	# 	'''
	# 	:return: 无
	# 	打印
	# 	'''

	allSectDict = tt.allSectDictOfFile
	iCount = 0
	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]

		if "INFORMATION" in sectDict:
			try:
				menuStr = sectDict["INFORMATION"]["Menu"][0]
				if("0X") in menuStr.upper():
					#print(Del0x(sectKey))
					if Del0x(sectKey) in indexList:
						print(sectKey)
						iCount += 1
					else:
						print(">>>{0}".format(sectKey))
			except:
				pass

	print(iCount)
	pass


if __name__ == "__main__":

	main()

	pass