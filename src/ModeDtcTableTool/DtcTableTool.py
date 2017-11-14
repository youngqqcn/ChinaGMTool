#!coding:utf8

'''
Date:2017/10/26/13:54
Author:yqq
Description: 将Type1/Dtc.txt转成Excel表格形式
'''

from lib.mytool11 import *

gIndexDict = {}

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






def WriteFile(sectDict, outFilePath):

	outFile = open(outFilePath, "w")

	allSectDict = sectDict

	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]

		if ('Protocol' in sectDict) and ('ReadDtc' in sectDict):
			if 'Cmd' not in sectDict['ReadDtc']:
				continue

			outFile.write('{0}\t'.format(sectKey)) #段的索引
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


			#获取系统路径

			outFile.write("{0}\t".format( GetSysPath(sectKey)) )


			outFile.write('\n')
			pass
		else:
			continue



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
			print(value)
			gIndexDict[value] = key            #速度更快!!
	pass


def main():

	MyReadText(u"../../txt/中国通用/RootMenuIndex.txt")

	tt =  TextTool(u"../../txt/中国通用/Type1/Dtc.txt")
	#tt.ShowAll()

	WriteFile(tt.allSectDictOfFile, "../../doc/tmp/Mode1_Dtc.txt")




	pass


if __name__ == "__main__":

	main()

	pass