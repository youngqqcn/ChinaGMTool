
#!coding:utf8

'''
Date:2017/11/23/11:28
Author:yqq
Description:none
'''

from lib.mytool12 import TextTool
from lib.mytool12 import ReadText
from lib.mytool12 import Add0x
from lib.mytool12 import Del0x
from lib.mytool12 import DictKVInvert


def CheckDsMode(inDict1, inDict2, inDict3):
	'''
	验证 RootMenuIndex.txt 中的 索引 和数据流模式之间的关系
	猜想1: 所有0000040开头的都是模式1
	猜想2: 所有000012FE开头的都是模式2
	:return: 
	'''
	class Ds:
		def __init__(self):
			self.index = ""
			self.mode = ""

	outFile = open("../../doc/tmp/dsModeCheckResult.txt", "w")

	for key, value in inDict1.items():
		#print(key + "\t" + value)
		tmpDs = Ds()
		tmpDs.index = Add0x( key[2 : ] )
		tmpDs.mode = value.strip()

		if tmpDs.index in inDict2:
			nextID = inDict2[tmpDs.index].strip()
			if (nextID[ : 8] == "0000040") and (tmpDs.mode != '1'):
				print("0x" + Del0x(tmpDs.index) +"\t"+inDict3["0x" + Del0x(tmpDs.index)] + "   is not mode 1")
				outFile.write("0x" + Del0x(tmpDs.index) +"\t"+inDict3["0x" + Del0x(tmpDs.index)] + "   is not mode 1\n")
			elif (nextID[ : 8] == "000012FE") and (tmpDs.mode != '2'):
				outFile.write("0x" + Del0x(tmpDs.index) +"\t"+inDict3["0x" + Del0x(tmpDs.index)] + "   is not mode 2\n")
			else:
				pass

	outFile.close()

	pass



def CheckDsText(path, inDict1, inDict2):
	'''
	检查菜单
	:param path: 
	:param inDict1: 
	:param inDict2:  cn_text.txt字典
	:return: 
	'''
	tt = TextTool(path)

	# def ShowAll(self):
	# 	'''
	# 	:return: 无
	# 	打印
	# 	'''
	#
	# 	allSectDict = self.allSectDictOfFile
	# 	for sectKey in allSectDict:
	# 		sectDict = allSectDict[sectKey]
	# 		print ('{0}'.format(sectKey))
	# 		for filedKey in sectDict:
	# 			filedDict = sectDict[filedKey]
	# 			print ('[{0}]'.format(filedKey))
	# 			for keyPairKey in filedDict:
	# 				for listItem in filedDict[keyPairKey]:
	# 					print('{0}={1}'.format(keyPairKey, listItem))
	# 			print ('\n')
	# 	pass


	_8250List = set()
	_82FFList = set()

	allSectDict = tt.allSectDictOfFile
	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]
		mode = -1
		for filedKey in sectDict:
			filedDict = sectDict[filedKey]
			if("DStreamCmd" in filedDict):
				mode = 1
				break
			if ("ScanCmd" in filedDict):
				mode = 2
				break

		for filedKey in sectDict:
			filedDict = sectDict[filedKey]

			num = 0
			if ("Num" in filedDict):
				num = int(filedDict["Num"][0][2:], 16)  # 获取item个数, 转成十进制
			for keyPairKey in filedDict:
				if "Item" in keyPairKey:
					#print(filedDict[keyPairKey][0])
					tmpStr = filedDict[keyPairKey][0]
					dsText = tmpStr.split(',')[0]   #获取数据流文本索引
					if mode == 1:
						if Add0x( "82FF" + dsText.upper() ) not in inDict2:
							#print (sectKey + "不在82FF")
							#print(dsText)
							_82FFList.add(sectKey)
							break
					if mode == 2:
						if Add0x( "8250" + dsText.upper() ) not in inDict2:
							# if(dsText[0] != '4'):
							# 	try:
							# 		if(int(dsText, 16) < 0x5003):
							# 			print(dsText + "不在8250")
							# 	except:
							# 		pass
							#print(sectKey + "不在8250")
							_8250List.add(sectKey)
							break


	for _8250 in _8250List:
		#print(_8250 + " 不在8250")
		pass
	# print(len(_8250List))

	for _82FF in _82FFList:
		#print(_82FF + " 不在82FF")
		pass

	# for _82

	return _8250List

	pass



def Foo(set1, set2, inDict):
	'''
	求set1 和 set2 的差集
	:param set1: 模式2, 用到的索引
	:param set2: 模式2, 不在8250里面的
	:param inDict: 
	差集就是:  用到的, 在50里面的
	:return: 
	'''

	with open(u"../../doc/tmp/用到的_且在8250里面的.txt", "w") as outFile:
		for item in (set1 - set2):
			print(item + "\t" + inDict[item])
			outFile.write(item + "\t" + inDict[item] + "\n")
	with open(u"../../doc/tmp/用到的_且不在8250里面的.txt", "w") as outFile:
		for item in (set1 & set2):
			print(item + "\t" + inDict[item])
			outFile.write(item + "\t" + inDict[item] + "\n")

	pass




def main():

	rt1 =  ReadText(u"../../txt/dsModeCheck.txt", 1)

	rt2 = ReadText(u"../../txt/中国通用/RootMenuIndex.txt", 1)

	rt3 = ReadText(u"../../txt/dsModeCheck2.txt", 1)
	rt3 = DictKVInvert(rt3)  #键值互换

	rt4 = ReadText(u"../../txt/中国通用/cn_text.txt", 2)

	#for k, v in rt4.items():
		#print(k  + "\t" + v)

	#CheckDsMode(rt1, rt2, rt3)
	rt5 = CheckDsText(u"../../txt/中国通用/Type1/Ds.txt", DictKVInvert(rt3), rt4)
	#for item in rt5:
	#	print(item)

	rt3 = DictKVInvert(rt3)
	Foo(set(rt3.keys()), set(rt5), rt3)





	pass


if __name__ == "__main__":

	main()

	pass