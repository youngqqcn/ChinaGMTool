#!coding:utf8

'''
Date:2017/10/23/10:05
Author:yqq
Description: 处理菜单文件,去掉 (<0x.*?>)
'''
import os


GLOBAL_PATH = '.'           #菜单文件所在目录, 默认是当前目录
SAVE_OLD_FILE = True        #是否备份原来的文件



def DealText(filePath):

	'''
	处理菜单文件,去掉 (<0x.*?>)
	:param filePath: 菜单文件路径
	:return: 无
	'''

	with open(filePath, "r") as inFile:
		linesList = inFile.readlines() #读取
		for i in range(len(linesList)):
			eachLine = linesList[i]
			if (('<0x' in eachLine) or ('<0X' in eachLine)) and ('>' in eachLine): #查找
				linesList[i] = eachLine.replace(eachLine[eachLine.find('<0x') : eachLine.find('>') + 1 ], '') #替换
				pass

	if SAVE_OLD_FILE: #保留原来的文件
		os.rename(filePath, filePath.replace('.txt', '') + '_bak.txt')  #备份原来的文件

	# 写回
	with open(filePath , "w") as outFile:
		outFile.writelines(linesList)

	pass


def main():

	for rootMenuFile in os.listdir(GLOBAL_PATH) :   #遍历菜单文件目录
		if ("ROOT" in rootMenuFile) | ("root" in rootMenuFile):   #文件名包含root
			DealText(rootMenuFile)

	pass


if __name__ == "__main__":

	main()

	pass