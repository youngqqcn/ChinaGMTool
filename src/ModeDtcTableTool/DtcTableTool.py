#!coding:utf8

'''
Date:2017/10/26/13:54
Author:yqq
Description: 将Type1/Dtc.txt转成Excel表格形式
'''

from lib.mytool12 import *

gIndexDict = {}

gDtcLib = TextTool(u"../../txt/中国通用/DtcLib.txt", False)

# 数据结构:
# dict = {sect1:{filed1:{key1:[value1, value2], key2:[value1, value2]}}}

#
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



#gFilterList = ['protocol', 'mode', 'cmd', 'pos', 'status',  'lib' ]
gDealedList = []

gEcuIdList = []

gDtcTextDict = {}

def GetSysPath(sectKey):
	'''
	获取系统路径, 方便测试和验证 
	:param sectKey: 
	:return: 
	'''
	#0x02, 0x94, 0x10, 0x48, 0x00, 0x00, 0x00, 0x00

	preHalfStr = sectKey[ : len(sectKey)/2]   #前半字符串
	#searchStr =  "00000100" + Del0x(preHalfStr) #去掉'0x'
	searchStr =  Del0x(preHalfStr) #去掉'0x'

	searchKey = ''
	# for key, value in gIndexDict.items():
	# 	#print(value)
	# 	if searchStr.strip() in value.strip():
	# 		searchKey = key

	try:
		searchKey =  gIndexDict[searchStr]    #速度快!!
	except:
		pass

	if searchKey == '':
		#print('{0} not found!\n'.format(searchKey))
		return  ' '

	return '0x' + Del0x(searchKey)


def GetSubLibFlag(inLibIndex):
	'''
	判断DtcLib.txt中的inLibIndex段下面, 是否 有   [SUBLIB]
	:param inLibIndex: 
	:return: 
	'''

	d = gDtcLib.allSectDictOfFile
	#print(len(d))
	#print(d.keys())

	tmpIndex = Add0x("0000" + Del0x(inLibIndex).upper())


	if tmpIndex in d:
		#print(tmpIndex)
		if "SUBLIB" in d[tmpIndex]:
			print(tmpIndex)
			return  "1"
	return "  "






def DealOneSectDict(sectDict, ecuId, sectKey, outFile, subTitile):
	'''
	向文件写入一个段
	:param sectDict: 
	:param ecuId: 父EcuID
	:param sectKey: 
	:param outFile: 
	:param subTitile: 子选项名称
	:return: 
	'''
	if ('Protocol' in sectDict) and ('ReadDtc' in sectDict):
		if 'Cmd' not in sectDict['ReadDtc']:
			return


		outFile.write('{0}\t'.format(Del0x(sectKey)))  # 段的索引

		# 获取系统路径
		outFile.write("{0}\t".format(ecuId))  #ecuId


		# if subTitile != "--":
		# 	print (subTitile)

		outFile.write("{0}\t".format(subTitile))  #ecuId

		try:
			outFile.write('{0}\t'.format(sectDict['Protocol']['Protocol'][0]))
		except:
			outFile.write('{0}\t'.format(' '))
		try:
			outFile.write('{0}\t'.format(sectDict['ReadDtc']['Mode'][0]))
		except:
			outFile.write('{0}\t'.format(' '))
		try:
			if 'SpeciDtcCmd' in sectDict['ReadDtc']:
				outFile.write('{0}\t'.format(sectDict['ReadDtc']['SpeciDtcCmd'][0]))
			else:
				outFile.write('{0}\t'.format(sectDict['ReadDtc']['Cmd'][0]))
		except:
			outFile.write('{0}\t'.format(' '))
		try:
			if 'SpeciDtcStartPos' in sectDict['ReadDtc']:
				outFile.write('{0}\t'.format(sectDict['ReadDtc']['SpeciDtcStartPos'][0]))
			else:
				outFile.write('{0}\t'.format(sectDict['ReadDtc']['Pos'][0]))
		except:
			outFile.write('{0}\t'.format(' '))
		try:
			outFile.write('{0}\t'.format(sectDict['ReadDtc']['Status'][0]))
		except:
			outFile.write('{0}\t'.format(' '))
		try:
			outFile.write('{0}\t'.format(sectDict['ReadDtc']['Lib'][0]))
		except:
			outFile.write('{0}\t'.format(' '))
			pass

		try:
			outFile.write('{0}\t'.format(sectDict['ReadDtc']['ReadDtcOffset'][0]))
		except:
			outFile.write('{0}\t'.format(' '))
			pass

		# try:
		# 	outFile.write('{0}\t'.format(sectDict['ReadDtc']['ReadDtcNumPos'][0]))
		# except:
		# 	outFile.write('{0}\t'.format(' '))
		# 	pass




		try:
			outFile.write('{0}\t'.format(sectDict['ReadDtc']['LibFlag'][0]))
		except:
			outFile.write('{0}\t'.format(' '))
			pass

		try:
			outFile.write('{0}\t'.format(GetSubLibFlag(sectDict['ReadDtc']['Lib'][0])))   #是否有SUBLIB
		except:
			outFile.write('{0}\t'.format(' '))
			pass

		outFile.write('\n')
		pass

	pass


def GetText(index):

	if index in gDtcTextDict:
		return gDtcTextDict[index].strip()

	pass


def WriteFile(sectDict, outFilePath):

	outFile = open(outFilePath, "w")

	allSectDict = sectDict

	for sectKey in allSectDict:
		tmpSectDict = allSectDict[sectKey]

		if sectKey in gDealedList:
			continue   #如果已经处理过了, 则跳过

		ecuId = GetSysPath(sectKey)

		if ecuId[2:] not in gEcuIdList:
			continue

		#2017-12-13
		if "SYSTEM" in tmpSectDict:
			num = int(tmpSectDict["SYSTEM"]["Num"][0][2:], 16)
			for i in range(1, num):

				tmpPreffix = (Del0x(sectKey)[:2] == "20") and ("8250") or ("82FF")
				subName = GetText(   Add0x( tmpPreffix + tmpSectDict["SYSTEM"]["Item" +  "%02X" % i][0] ) )
				# break

				tmpSectKey = Add0x(Del0x(sectKey)[ : 8] + ("%02X" % i) + Del0x(sectKey)[10:])

				if tmpSectKey in  gDealedList:
					continue   #如果已经处理过了, 则跳过

				#print(subName)

				try:
					DealOneSectDict(sectDict[tmpSectKey], ecuId, tmpSectKey, outFile, subName)
				except:
					#0x00, 0xA0, 0x1E, 0xE2, 0x01, 0x00, 0x00, 0x01
					#0x00, 0xA0, 0x26, 0x0D, 0x01, 0x00, 0x00, 0x01
					print(tmpSectKey)    #有两个找不到, 可能是道通的库有问题; 已经改了
				gDealedList.append(tmpSectKey)
			continue
		else:
			DealOneSectDict(tmpSectDict, ecuId, sectKey, outFile, "  ")
			gDealedList.append(sectKey)


	outFile.close()
	pass

#
# def MyReadText(filePath):
#
# 	with open(filePath, "r") as inFile:
# 		linesList  = inFile.readlines()
# 		for line in linesList:
# 			key = line.split('\t')[0].strip()
# 			value = line.split('\t')[1].strip()
# 			gIndexDict[key] = value
# 	pass





def MyReadText(filePath):

	with open(filePath, "r") as inFile:
		linesList  = inFile.readlines()
		for line in linesList:
			key = line.split('\t')[0].strip()
			value = line.split('\t')[1].strip()[1 : -1]
			value = value[len(value)/2 : ]
			#print(value)
			gIndexDict[value] = key            #速度更快!!
	pass

def GetEcuIdList(filePath):
	with open(filePath, "r") as inFile:
		linesList  = inFile.readlines()
		for line in linesList:
			gEcuIdList.append(line.strip())


def GetDtcTextDict(filePath):

	global gDtcTextDict
	gDtcTextDict = ReadText(filePath, 2)

	pass


def main():

	GetDtcTextDict(u"../../txt/中国通用/cn_text.txt")
	# for k, v in gDtcTextDict.items():
	# 	print("{0}={1}".format(k, v))
	# return

	GetEcuIdList(u"../../txt/中国通用_所有ECUID.txt")

	MyReadText(u"../../txt/中国通用/RootMenuIndex.txt")

	tt =  TextTool(u"../../txt/中国通用/Type1/Dtc.txt")
	#tt.ShowAll()

	#WriteFile(tt.allSectDictOfFile, "../../doc/tmp/DtcTable_12_15.txt")
	WriteFile(tt.allSectDictOfFile, "../../doc/tmp/DtcTable_2018_01_19.txt")




	pass


if __name__ == "__main__":

	main()

	pass