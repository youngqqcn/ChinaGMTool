#!coding:utf8

'''
Date:2017/11/21/15:25
Author:yqq
Description:  将Ds.txt 提成Excel表格文件
'''

import os
from collections import OrderedDict
from lib.mytool11 import TextTool
from  lib.mytool11 import ReadText
from lib.mytool11 import Add0x
from lib.mytool11 import Del0x

gMenuEcuSet = set()
gMenuEcuDict = {}
gRootIndexDict = ReadText(u"../../txt/中国通用/RootMenuIndex.txt", tabCount=1)
gDsEcuIndexSet = set()
gDsProtocolDict = {}

def DealEcuId(ecuId):
	if Add0x(ecuId) in gRootIndexDict:
		tmpStr = gRootIndexDict[Add0x(ecuId)]
		index = Add0x( tmpStr[8 : ] + "000000" + tmpStr[6 : 8] )
		return  index
	return "NULL"



def GetMenuEcuIdSet(path):

	for fileName in os.listdir(path):
		with open(os.path.join(path, fileName), "r") as inFile:
			linesList = inFile.readlines()
			for line in linesList:
				if ('<0x' in line) and ('>' in line):
					ecuId = line[line.find('<0x') + 3: line.find('>')]
					#print(ecuId)
					#gMenuEcuSet.add(ecuId)
					if DealEcuId(ecuId) != 'NULL':
						tmpIndex = DealEcuId(ecuId)
						gMenuEcuSet.add(tmpIndex)
						gMenuEcuDict[tmpIndex] = '0x' + ecuId
	pass



def GetDsEcuIdSet(path):

	tt = TextTool(path)
	global gDsEcuIndexSet
	gDsEcuIndexSet = set( tt.allSectDictOfFile.keys() )


	class Tmp:
		def __init__(self):
			self.protocol = ""
			self.cmdMode  = ""

	allSectDict = tt.allSectDictOfFile
	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]
		print ('{0}'.format(sectKey))

		if(sectKey not in gDsProtocolDict):
			gDsProtocolDict[sectKey] = Tmp()

		if("Protocol" in sectDict["Protocol"]):
			#gDsProtocolDict[sectKey].append( sectDict["Protocol"]["Protocol"][0].strip() )
			gDsProtocolDict[sectKey].protocol =  sectDict["Protocol"]["Protocol"][0].strip()

	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]
		if(sectKey not in gDsProtocolDict):
			continue

		gDsProtocolDict[sectKey].cmdMode = '1'
		for fieldKey in sectDict:
			if "ScanCmd" in sectDict[ fieldKey ]:
				#gDsProtocolDict[sectKey] = '2'   #命令模式2
				gDsProtocolDict[sectKey].cmdMode = '2'
				break
	pass







def DictKeyToValue(inDict):

	if(isinstance(inDict, dict)):
		#普通的字典
		newDict = {}
	elif(isinstance(inDict, OrderedDict)):
		#有序字典
		newDict = OrderedDict()
	else:
		print("入参不是字典,请检查")
		raise ValueError

	for key, value in inDict:
		newDict[value] = key
	pass



def main():


	GetMenuEcuIdSet(u"../../txt/中国通用/RootMenu")
	GetDsEcuIdSet(u"../../txt/中国通用/Type1/Ds.txt")


	with open(u"../../doc/tmp/dsCmdMode.txt", "w") as outFile:
		for item in (gDsEcuIndexSet & gMenuEcuSet):   #求交集
			print(item + '\t' + gMenuEcuDict[item])
			outFile.write(item + '\t' + gMenuEcuDict[item]+'\t'+\
			              gDsProtocolDict[item].protocol + '\t' + \
			              gDsProtocolDict[item].cmdMode + ' ' + '\n')

		print(u"个数:" + str(len(gDsEcuIndexSet & gMenuEcuSet)) )


	pass






if __name__ == "__main__":

	main()

	pass