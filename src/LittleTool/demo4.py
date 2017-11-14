#!coding:utf8

'''
Date:2017/11/13/17:20
Author:yqq
Description: 获取 cn_OBD_dtc.txt  部分子集
'''



PATH = u"../../txt/中国通用/Type1/cn_OBD_dtc.txt"

class CDtc:
	'''
	故障码类, 相当于 一个结构体
	'''
	def __init__(self):
		self.index = ''
		self.text = ''
		self.code = ''



def ReadText(Path):
	'''
	读cn_OBD_dtc.txt   放到DtcList    对象List里面
	:param Path: 
	:return:  DtcList   
	'''


	DtcList = []

	with open(Path, "r") as inFile:
		linesList = inFile.readlines()

		for line in linesList:
			splitedList = line.split('\t\t')

			tmpDtc = CDtc()   #临时对象

			tmpDtc.index = splitedList[0].strip()   #索引
			tmpDtc.code = splitedList[1].strip()    #故障码码号(PCBU码)
			tmpDtc.text = splitedList[2].strip()    #故障码文本

			DtcList.append(tmpDtc)

	return DtcList



def WriteFile(number1 , inList):

	# if  number1 == '$$':
	# 	with open(u"../../doc/tmp/11_13_没16的.txt".format(number1 ), "w") as outFile:
	# 		for code in  inList:
	# 			print(code)
	# 			outFile.write(code + "\n")

	with open(u"../../doc/tmp/11_13_有{0}没有{1}的.txt".format(number1, 16 ), "w") as outFile:
	#with open(u"../../doc/tmp/11_13_有{0}且有{1}的.txt".format(10, 11 ), "w") as outFile:
		for code in  inList:
			# print(code)
			outFile.write(code + "\n")
	pass



def main():


	numList = [ ('%02X' % i).upper() for i in range(1, 0x1B + 1)]   #生成 1 - 0x1B 的16进制字符串
	Sixteen = []

	Elven = []
	Ten = []


	DtcList = ReadText(PATH)

	for dtc in DtcList:
		if "0x01,0x00,0x02,0x16" in dtc.index:
			Sixteen.append(dtc.code)
		#if "0x01,0x00,0x02,0x11" in dtc.index:
		#	Elven.append(dtc.code)
		#if "0x01,0x00,0x02,0x10" in dtc.index:
		#	Ten.append(dtc.code)


	# (求10 和 11  的并集)  与  16 的差集
	# tmpList = []
	# for dtcCode in Elven:
	# 	if dtcCode in Sixteen:
	# 		continue
	# 	if dtcCode in Ten:
	# 		tmpList.append(dtcCode)
	#
	#
	# WriteFile(0, tmpList)




	#求集合
	for number in numList:
		tmpDtcList = []
		for dtc in DtcList:

			if "0x01,0x00,0x02,0x16" not in dtc.index:
				if "0x01,0x00,0x02,0x7F" not in dtc.index:
					#if dtc.code not in Sixteen:    #没0x16的
					if dtc.code in Sixteen:      #有0x16的

						if "0x01,0x00,0x02,0x{0}".format(number) in dtc.index:
							tmpDtcList.append(dtc.code)

		WriteFile(number, tmpDtcList) #输出到文件

	pass


if __name__ == "__main__":

	main()

	pass