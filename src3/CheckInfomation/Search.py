#!coding:utf8

'''
Date:2018/1/10/14:41
Author:yqq
Description:搜索 满足条件的 ...
'''

from lib.mytool12 import TextTool
from lib.mytool12 import Del0x

gInDir = u"../../txt/中国通用/Type1/Information.txt"




gSearchFormat = 34

def main():

	tt = TextTool(gInDir)
	#tt.ShowAll()
	#def ShowAll(self):
	'''
	:return: 无
	打印
	'''
	indexList = []
	with open(u"../../txt/版本信息的索引.txt") as inFile:
		for line in inFile.readlines():
			indexList.append(line.strip())


	allSectDict = tt.allSectDictOfFile
	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]
		#print ('{0}'.format(sectKey))
		try:
			mode = int(sectDict["INFORMATION"]["InfoMode"][0], 10)
			if mode >= 4:
				try:
					num = int(sectDict["INFORMATION"]["Num"][0], 16)
					#print(num)
					for i in range(1, num + 1):
						itemStr = sectDict["INFORMATION"]["Item%02X" % i][0]
						tmpSplitList = itemStr.split(",")
						format = int(tmpSplitList[len(tmpSplitList) - 1 ], 10) #获取最后一个
						#print(format)
						if format == gSearchFormat:
							if Del0x(sectKey) in indexList:
								print(Del0x(sectKey))
					pass
				except:
					pass

			pass
		except:
			pass


if __name__ == "__main__":

	main()

	pass