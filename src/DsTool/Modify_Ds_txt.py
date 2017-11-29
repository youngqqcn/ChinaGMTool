#!coding:utf8

'''
Date:2017/11/29/14:19
Author:yqq
Description:  修改Type1/Ds.txt   在文本索引加上 82FF 或者 8250 
	
'''

from lib.mytool12 import ReadText
from lib.mytool12 import TextTool



def main():

	dsUnitIndexFilePath = u"../../txt/DsUnitIndex.txt"
	tt = TextTool(u"../../txt/中国通用/Type1/Ds.txt")

	unitDict = {}    #单位索引  和 标志 组成的字典
	rt = ReadText(dsUnitIndexFilePath, 1)
	for k, vList in rt.items():
		# print(k + "\t" + vList[0])
		unitDict[k] = vList[0]

	allSectDict = tt.allSectDictOfFile
	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]
		# print ('{0}'.format(sectKey))
		for filedKey in sectDict:
			filedDict = sectDict[filedKey]
			# print ('[{0}]'.format(filedKey))
			for keyPairKey in filedDict:
				if ("Item" not in keyPairKey) or (keyPairKey == "ItemNum"):
					continue
				splitedList = filedDict[keyPairKey][0].split(',')
				if (len(splitedList) > 0):
					try:
						tmpDsUnitIndex = splitedList[1].upper()
						flag = unitDict[tmpDsUnitIndex]  #直接获取, 如果没有,引发异常
					except:
						#print(splitedList)
						print(sectKey + "\t" + filedKey + "\t" + keyPairKey)
						print ("error!!!!")
						continue

					if flag.strip() == '0':
						addStr = "82FF"
					elif flag.strip() == '1':
						addStr = "8250"
					elif tmpDsUnitIndex == "NULL":
						continue
					else:
						print(tmpDsUnitIndex)
						print("$$$$$$$$$$$")
						continue

					#加82FF  或者 8250
					newSplitedList = splitedList
					newSplitedList[0] = addStr + splitedList[0]  #数据流文本 加 82FF  或者 8250
					newSplitedList[1] = addStr + splitedList[1]  #数据流单位 加 82FF  或者 8250

					newJoinedStr = ','.join(newSplitedList)  #以逗号分隔

					filedDict[keyPairKey][0] = newJoinedStr   #放回去

		pass  #for

	tt.WriteFile("../../doc/tmp/new_Type1_Ds.txt")  #输出已经修改了的

	pass #def



if __name__ == "__main__":

	main()

	pass