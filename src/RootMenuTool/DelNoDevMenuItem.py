#!coding:utf8

'''
Date:2017/11/9/11:58
Author:yqq
Description:  删除不开发的功能(菜单选项)

只开发下面4大基本功能:
	读故障码
	清除故障码
	读版本信息
	读数据流
	
其他的功能都删掉
'''


import os


#添加需要删掉的"菜单选项"
gDelMenuItemList = [
	"个性化设置",
	"更多故障码信息",
	"检查/维护系统信息",
	"自代码清除测试未通过",
	"自清除后未运行的代码",
	"查询故障码",
	"诊断测试状况",
	"冻结故障状态/故障记录",
	"事件数据",
	"模块零件号信息",

	#"\t编程\n",    #2005  line4847
	#"\t阻断器\n",   #2005
]

MENU_PATH = "../../txt/RootMenu/"           #菜单目录路径
OUTPUT_PATH = "../../doc/tmp/RootMenu_New/" #输出菜单目录路径




def DelNodeAndHisChilds(inOldList, begin):
	'''
	实现一个函数, 跳过 一个节点及其子节点  
	当然,也支持单行的删除, 即它自己就是一个叶子节点
	:param inOldList:  菜单节点list (类似引用传递 )
	:param begin:  开始下标
	:return:  新下标
	'''

	index = begin
	while True:
		index += 1
		if index >= len(inOldList):
			return  index
		if inOldList[index].count('\t') <= inOldList[begin].count('\t'):
			return  index



def Deal(inFilePath ):
	'''
	处理一个菜单文件
	:param inFilePath:  输入文件
	:param outFilePath:  输出文件
	:return: outputLinesList
	'''

	outputLinesList = []
	with open(inFilePath, "r") as inFile:

		linesList = inFile.readlines()
		index = 0
		while index < len(linesList):
			appendFlag = True
			for delStr in gDelMenuItemList:   #检查是需要删除
				if delStr in linesList[index]:
					#跳过此节点及其子节点, 不添加到outputLinesList中
					index = DelNodeAndHisChilds(linesList, index)
					appendFlag = False   #不添加
					break
			if appendFlag: #可以添加
				outputLinesList.append(linesList[index])
				index += 1
			pass

	return  outputLinesList





def Optimize(inLinesList):
	'''
	:param inLinesList:  待优化的菜单
	:return:  优化后的菜单
	'''
	retList = []

	i = 0
	while True:

		if i >= len(inLinesList):
			break

		#优化读取故障码下面只有一个"读取故障码<????>"的情况
		if "读取故障码" == inLinesList[i].strip():
			if ("读取故障码" in  inLinesList[i + 1]) and ('<0x' in inLinesList[i + 1]):
				tabCount = inLinesList[i + 1].count('\t')
				retList.append(inLinesList[i + 1].replace(tabCount * '\t', (tabCount - 1) * '\t')) #减少一个tab键
				i += 2
				continue

		if "阻断器" == inLinesList[i].strip():
			if "编程" in inLinesList[i + 1]:
				i = DelNodeAndHisChilds(inLinesList, i)
				continue

		#...在此添加其他优化....
		#....



		retList.append(inLinesList[i])
		i += 1

	return  retList






def CheckDirs():
	'''
	检查目录
	:return:  无
	'''

	if not os.path.exists(MENU_PATH):   #检查输入文件路径是否存在, 不存在引发异常
		print("输入菜单目录,不存在")
		raise  ValueError

	if os.path.abspath(OUTPUT_PATH) == os.path.abspath(MENU_PATH):  #输出目录不能喝输入目录一样
		print("输出和输入目录相同! 请修改")
		raise ValueError

	if not os.path.exists(OUTPUT_PATH): #如果输出路径不存在,则创建
		#os.mkdir(OUTPUT_PATH)
		os.makedirs(OUTPUT_PATH)

	pass



def main():

	CheckDirs()   #检查目录

	for inFileName in os.listdir(MENU_PATH):  #遍历输入菜单目录
		inFilePath = os.path.join(MENU_PATH , inFileName)       #输入文件路径
		outFilePath = os.path.join(OUTPUT_PATH, inFileName)     #输出文件路径

		retList = Deal(inFilePath )     #删除不开发的菜单项
		retList = Optimize(retList)     #优化


		with open(outFilePath, "w") as outFile:
			outFile.writelines(retList) #输出

	pass


if __name__ == "__main__":

	main()

	pass