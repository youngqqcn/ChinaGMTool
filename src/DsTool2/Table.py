#!coding:utf8

'''
Date:2017/12/5/19:05
Author:yqq
Description:
	
	根据ECUID  获取协议类型
	
	1.通过EcuId, 在RootMenuIndex.txt中获取 nextID
	2.解析nextID, type分类  和  功能分类
	3.从功能文件获取协议类型
'''

from lib.mytool12 import ReadText
from  lib.mytool12 import TextTool
from lib.mytool12 import Add0x
from lib.mytool12 import Del0x

from threading import  Thread    #使用多线程,加快处理速度

import os
import  datetime


beginTime = datetime.datetime.now()



gIndexPath = u"../../txt/中国通用/RootMenuIndex.txt"



gType1List = [
		"00000100" , "00000200", "00000300" ,"00000400"\
		,"00000500" , "00000600" , "00000700" , "00000102"\
		, "000012FE"
]

gT1DtcTT = TextTool(u"../../txt/中国通用/Type1/Dtc.txt")
gT1DsTT = TextTool(u"../../txt/中国通用/Type1/Ds.txt")
gT1InfoTT = TextTool(u"../../txt/中国通用/Type1/Information.txt")


gThreadCount = 256
gLinesList = []
gThreadOutputPath = u"../../doc/tmp/threadOutput"

gOutputDict = {}

gOutputFilePath = u"../../doc/tmp/中国通用车型表_1208.txt"

def Type1_DTC(index):

	d = gT1DtcTT.allSectDictOfFile
	prot = ''
	if index in d:
		if "SYSTEM" in d[index]:
			index  = Add0x(Del0x(index)[0:8] + ("%02X" % 1) + Del0x(index)[10 :])
		try:
			prot = d[index]["Protocol"]["Protocol"][0].strip()
			pass
		except:
			prot = ""
			pass

	return prot


def Type1_DS(index):
	prot = ''

	d = gT1DsTT.allSectDictOfFile

	if index in d:

		if "Protocol" in d[index]:
			try:
				prot = d[index]["Protocol"]["Protocol"][0].strip()
				#print(u"数据流{0}".format(prot))
				pass
			except:
				prot = ""
				pass
		else:
			print("no protocol")
	return prot


def Type1_VerInfo(index):

	prot = ''

	d = gT1InfoTT.allSectDictOfFile

	if index in d:

		if "Protocol" in d[index]:
			try:
				prot = d[index]["Protocol"]["Protocol"][0].strip()
				# print(u"数据流{0}".format(prot))
				pass
			except:
				prot = ""
				pass
		else:
			print("no protocol")
	return prot



def Type1(nextId):

	funcType = nextId[ : 6] + "00"

	index = nextId[8:].strip() + "000000" + nextId[6:8]
	if funcType in ["00000100", "00001100"]:
		#读码清码
		#print(index)
		return Type1_DTC(Add0x(index))
		pass
	elif funcType in ["00001200", "00000400"]:
		return Type1_DS(Add0x(index))
		#读数据流
		pass
	elif funcType in ["00000700", "00001000"]:
		return  Type1_VerInfo(Add0x(index))
		#版本信息
		pass
	else:
		pass

	pass





def Type2(nextId):
	pass


def Type3(nextId):

	pass






def GetProtocolTypeByEcuID(ecuId):
	'''
	根据ecuId获取协议类型	
	:param ecuId: 
	:return: 协议类型
	'''

	_0xIndex = Add0x(ecuId[2:])
	indexRT = ReadText(gIndexPath, 1)

	retProtocol = ""
	if _0xIndex in indexRT:
		nextId = indexRT[_0xIndex]
		type = nextId[ 0 : 8]
		#print(type)

		if type in gType1List:
			#type1
			retProtocol = Type1(nextId)
			pass
		elif type == "0000FFFF":
			retProtocol = Type2(nextId)
			pass
		elif type == "00000000":
			retProtocol = Type3(nextId)
			pass
		else:
			retProtocol = Type1(nextId)
			#type1
			pass

		index = nextId[8:].strip() + "000000" + nextId[6:8]

	else:
		index = "  "

	return retProtocol, index







def main():

	inFilePath = u"../../doc/tmp/中国通用车型表.txt"
	outFilePath = u"../../doc/tmp/中国通用车型表(带协议类型).txt"

	with open(inFilePath, "r") as inFile, open(outFilePath, "w") as outFile:
		lines = inFile.readlines()
		for line in lines:
			ecuId = line.split('\t')[0]
			protocolType, index =  GetProtocolTypeByEcuID(ecuId)
			#print(protocolType)

			if isinstance(protocolType, str) :
				if len(protocolType) == 0:
					protocolType = "  "
				outFile.write("{0}".format(index + "\t"+ protocolType +"\t"+ line))
			else:
				outFile.write("{0}".format(index + "\t" + "   " + "\t" + line))

	pass


def Process(linesList, threadNo):

	lines = linesList

	#with open("{0}/{1}.txt".format(gThreadOutputPath, str(threadNo)), "w") as outFile:
	if (True):
		for line in lines:
			ecuId = line.split('\t')[0]
			protocolType,index = GetProtocolTypeByEcuID(ecuId)
			# print(protocolType)

			if isinstance(protocolType, str):
				if len(protocolType) == 0:
					protocolType = "  "
				#outFile.write("{0}".format(protocolType + "\t" + line))
				gOutputDict[threadNo].append("{0}".format(index + "\t"+ protocolType + "\t" + line))
			else:
				#outFile.write("{0}".format("   " + "\t" + line))
				gOutputDict[threadNo].append("{0}".format(index + "\t" + "  "+ "\t" + line))

	pass



def JobDistribute(beginIndex = 0, jobCount = 0 ):
	'''
	:param jobCount: 任务数
	:return: 
	'''
	averageJobCount = jobCount / gThreadCount
	print(averageJobCount)

	threadPool = []
	for i in range(gThreadCount):
		if i+1 == gThreadCount:  #最后一个线程收尾
			tmpList = gLinesList[ i * averageJobCount :  ]
			tmpThread = Thread(target=Process,  args=(tmpList, i))
		else:
			tmpList = gLinesList[ i * averageJobCount :   i*averageJobCount  + averageJobCount]
			tmpThread = Thread(target=Process, args=(tmpList, i))
			#print("线程{0}的任务数:{1}->{2}".format(i, beginIndex + i*averageJobCount , jobCount - i * averageJobCount))
		threadPool.append(tmpThread)

	for thread in threadPool:  #启动所有子线程
		thread.start()

	for thread in threadPool:   #等待所有子线程结束
		thread.join()

	print("DONE!")

	pass


def main2():

	for i in range(gThreadCount):
		global  gOutputDict
		gOutputDict[i] = []   #构造一个列表, 用于输出


	inFilePath = u"../../doc/tmp/中国通用车型表.txt"
	#outFilePath = u"../../doc/tmp/中国通用车型表(带协议类型).txt"

	with open(inFilePath, "r") as inFile:
		global  gLinesList
		gLinesList = inFile.readlines()
		print(len(gLinesList))

	JobDistribute(0, len(gLinesList))  #分配任务



	#统一写入文件
	with open(gOutputFilePath, "w") as outFile:
		for k, vList in gOutputDict.items():
			outFile.writelines(vList)

	endTime = datetime.datetime.now()

	print("总用时:{0}".format(  endTime - beginTime) )
	pass


if __name__ == "__main__":

	if not os.path.exists(gThreadOutputPath):
		os.makedirs(gThreadOutputPath)

	#main()
	main2() #使用多线程

	pass