#!coding:utf8

'''
Date:2017/10/10/13:44
Author:yqq
Description: 删除没用的菜单项,减少菜单深度
'''

import os


gDirName = "../../txt/RootMenu"
gFilterList = []



gSpecifyList = [
	"变速器类型",
	"牵引力控制",
	"空调系统",
	"水平调节系统",
	"分动箱",
	"方向盘选件",
	"安全气囊选件",
	"前大灯选项",
	"排气类型",
	"变速器",
]


# def DelCommantedLine():
# 	'''
# 	删除已经屏蔽掉的行, 即 以"//"开头的行
# 	:return:
# 	'''
#
# 	for eachFileName in os.listdir(gDirName) :
# 		eachFilePath =  os.path.join(gDirName, eachFileName)
#
# 		inFile = open(eachFilePath, "r")
# 		lineList = inFile.readlines()
# 		inFile.close()
#
# 		with open(eachFilePath, "w") as outFile:
# 			for eachLine in lineList:
# 				if r"//" in eachLine:
# 					continue #不写回
# 				else:
# 					outFile.write(eachLine) #写回去
# 	pass


def DelOneTab(inList, begin):
	'''
	:param i:  从inList[i]开始, 后面tab
	:return: 
	'''
	if len(inList) == 0:
		return
	tabCount = inList[begin].count('\t')

	for i in range(begin , len(inList) ):
		if (inList[i].count('\t') <= tabCount) and (i != begin):
			break
		else:
			inList[i] = inList[i].replace('\t'*inList[i].count('\t'), '\t' * (inList[i].count('\t')- 1) )   #减少一个tab键
	pass



def Judge(line):
	'''
	:param line: 
	:return: 
	'''

	for delMenuName in  gFilterList :
		#if delMenuName in line:
		#	return True
		if delMenuName.strip() == line.strip():
			return True

	return False


def IsSpecify(inLine):
	'''
	判断是否需要特殊处理
	:param inLine: 
	:return: 
	'''

	for item in gSpecifyList:
		if item.strip() == inLine.strip():
			return True
	return False



def GetIndex(inList, tabCount):
	'''
	查找tab数与tabCount相同的 
	:param inList: 
	:return: 
	'''

	for i in range(len(inList)):
		if inList[i].count('\t') == tabCount:
			return (True, i)
		if inList[i].count('\t') < tabCount:
			return (False, -1)
	return (False, -1)




def SpecifyDeal(inList, begin):
	'''
	特殊处理
	:param inList: 
	:param begin: 
	:return: 
	'''

	'''
	"变速器类型",
	"牵引力控制",
	"空调系统",
	"水平调节系统",
	"分动箱",
	"方向盘选件",
	"安全气囊选件",
	"前大灯选项",
	"排气类型",
	'''


	if inList[begin].strip() == "变速器类型":
		isSuffix = True
		suffixStr = "(变速器)"
		pass
	elif inList[begin].strip() == "牵引力控制":
		isSuffix = True
		suffixStr = "(牵引力控制)"
		pass
	elif inList[begin].strip() == "空调系统":
		isSuffix = True
		suffixStr = "(空调)"
		pass
	elif inList[begin].strip() == "水平调节系统":
		isSuffix = True
		suffixStr = "(水平调节)"
		pass
	elif inList[begin].strip() == "分动箱":
		isSuffix = True
		suffixStr = "(分动箱)"
		pass
	elif inList[begin].strip() == "方向盘选件":
		isSuffix = True
		suffixStr = "(方向盘选件)"
		pass
	elif inList[begin].strip() == "安全气囊选件":
		isSuffix = True
		suffixStr = "(安全气囊选件)"
		pass
	elif inList[begin].strip() == "前大灯选项":
		isSuffix = True
		suffixStr = "(前大灯选项)"
		pass
	elif inList[begin].strip() == "排气类型":
		isSuffix = True
		suffixStr = "(排气类型)"
		pass
	elif inList[begin].strip() == "变速器":   #2016,变速器类型下又分了变速器(AT变速器, EMT变速器)
		return
	else:
		raise ValueError

	tmpStr = inList[begin + 1]
	if isSuffix: #加后面
		inList[begin + 1] = tmpStr.replace(tmpStr.strip(), tmpStr.strip() + suffixStr)
	else: #加前面
		inList[begin + 1] = tmpStr.replace(tmpStr.strip(), suffixStr + tmpStr.strip() )

	tmpIndex = GetIndex(inList[begin + 2:], inList[begin + 1].count('\t'))
	if tmpIndex[0]:
		tmpStr = inList[begin + 2 + tmpIndex[1]]
		if isSuffix: #加后面
			inList[begin + 2 + tmpIndex[1]] = tmpStr.replace(tmpStr.strip(), tmpStr.strip() +suffixStr )
		else: #加前面
			inList[begin + 2 + tmpIndex[1]] = tmpStr.replace(tmpStr.strip(), suffixStr + tmpStr.strip() )
	pass

	pass



def Filter():
	'''
	 处理菜单文件, 删除无用菜单项
	:return: 
	'''

	for eachFileName in os.listdir(gDirName):
		eachFilePath = os.path.join(gDirName, eachFileName)

		outFile = open("../../doc/tmp/RootMenu/" + eachFileName, "w")

		with open(eachFilePath, "r") as inFile:
			lineList  = inFile.readlines()
			for i in range(len(lineList)):
				if Judge(lineList[i]):
					DelOneTab(lineList, i)   #将从下标i开始, 到tab键小于或等于这一行的tab键的某行结束
					continue
				if IsSpecify(lineList[i]):
					if (lineList[i].strip() == "变速器" ) and ("<0x" in lineList[i + 1]):
						pass
					elif (lineList[i].strip() == "分动箱" ) and ("<0x" in lineList[i + 1]):
						pass
					elif (lineList[i].strip() == "空调系统" ) and ("<0x" in lineList[i + 1]):
						pass
					elif (lineList[i].strip() == "燃油" ) and ("<0x" in lineList[i + 1]):
						pass
					elif (lineList[i].strip() == "制动器系统" ) and ("<0x" in lineList[i + 1]):
						pass
					elif (lineList[i].strip() == "挂车制动" ) and ("<0x" in lineList[i + 1]):
						pass
					else:
						SpecifyDeal(lineList, i)
						DelOneTab(lineList, i)   #将从下标i开始, 到tab键小于或等于这一行的tab键的某行结束
						continue
				outFile.write(lineList[i])

		outFile.close()

	pass



def main():

	with open("../../txt/DelMenuName.txt", "r") as inFile:
		while True:
			line  = inFile.readline()
			if len(line) == 0:
				break
			if len(line.strip()) == 0:
				continue
			gFilterList.append(line.strip())

	Filter()


	pass


if __name__ == "__main__":

	main()

	pass