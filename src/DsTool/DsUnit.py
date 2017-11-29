#!coding:utf8

'''
Date:2017/11/29/10:28
Author:yqq
Description:  获取Ds.txt用到的所有的   数据流单位
			通过数据流单位  定位  数据流文本
'''

from lib.mytool12 import ReadText
from lib.mytool12 import Add0x
from lib.mytool12 import Del0x
from lib.mytool12 import TextTool
from lib.mytool12 import GetTextFromTextLib
from lib.mytool12 import ReadTextPlus


def main():

	tt = TextTool(u"../../txt/中国通用/Type1/Ds.txt")


	cn_text_Path = u"../../txt/中国通用/cn_text.txt"


	rtp = ReadTextPlus(cn_text_Path, 2)

	unitSet = set()   #单位索引的集合


	allSectDict = tt.allSectDictOfFile
	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]
		#print ('{0}'.format(sectKey))
		for filedKey in sectDict:
			filedDict = sectDict[filedKey]
			#print ('[{0}]'.format(filedKey))
			for keyPairKey in filedDict:
				if("Item" not in keyPairKey):
					continue
				splitedList = filedDict[keyPairKey][0].split(',')
				if (len(splitedList) != 0):
					unitSet.add(splitedList[1].upper())

			#print ('\n')

	with open("../../doc/tmp/unit_text.txt", "w") as outFile:
		for unitIndex in unitSet:
			textStr82FF = ""
			textStr8250 = ""

			retList82FF = GetTextFromTextLib("82FF" + unitIndex, rtp)
			if (len(retList82FF) == 0):
				textStr82FF = "null"
			else:
				textStr82FF = retList82FF[0].strip().replace('"', '')

			retList8250 = GetTextFromTextLib("8250" + unitIndex, rtp)
			if (len(retList8250) == 0):
				textStr8250 = "null"
			else:
				textStr8250 = retList8250[0].strip().replace('"', '')

			print(unitIndex + "\t" + textStr82FF + "\t" + textStr8250)
			outFile.write(unitIndex + "\t" + textStr82FF + "\t" + textStr8250 + "\t" + "  " +"\n")
		pass




if __name__ == "__main__":

	main()

	pass