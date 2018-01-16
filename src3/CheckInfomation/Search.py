#!coding:utf8

'''
Date:2018/1/10/14:41
Author:yqq
Description:搜索 满足条件的 ...
'''

from lib.mytool12 import TextTool
from lib.mytool12 import Del0x

gInDir = u"../../txt/中国通用/Type1/Information.txt"



gSearchFormatList = [
	"1A",
	"1B",
	"1C",
	"1D",
	"1E",
	"1F",
	"0E",
	"0D",
	"0C",
	"0F",
	"0A",
	"36",
"37",
"38",
"39"
]


gSearchFormat = 34
gFormatList = []

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
						format = tmpSplitList[len(tmpSplitList) - 1 ] #获取最后一个

						#if False:
						#	format = int(tmpSplitList[len(tmpSplitList) - 1 ], 10) #获取最后一个
						#	print(format)

						if True:   #打印gSearchFormatList 中的
							if format in gSearchFormatList:
								if Del0x(sectKey) in indexList:
									print("{0}===>{1}".format(format, Del0x(sectKey)))

						if False:  #打印所有 算法格式
							if format not in gFormatList:
								gFormatList.append(format)
					pass
				except:
					pass

			pass
		except:
			pass

	for f in gFormatList:
		print(f)


if __name__ == "__main__":

	main()

	pass