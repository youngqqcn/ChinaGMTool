#!coding:utf8

'''
Date:2017/12/5/10:50
Author:yqq
Description:

	车型 ECU表

	  通过  "年份"   "车型"   "系列"   "协议"   
	

'''

import os
import sys
from lib.mytool12 import RootMenu



keys = []


def PrintKeys(keys):
	'''
	:param keys: 
	:return: 
	'''

	for item in keys:
		print ("{0}\t".format(item)),

# def ShowAll(self, inDict='self.menuDict', tabCount=0):
# 	'''
# 	:param inDict:  root菜单树(字典)
# 	:param tabCount: 缩进的tab数量
# 	:return: 无
# 	'''
# 	if inDict == 'self.menuDict':
# 		inDict = eval(inDict)
#
# 	if isinstance(inDict, list):
# 		return
# 	# print("{0}{1}".format('\t'*tabCount, inDict[0]))
# 	elif isinstance(inDict, dict):
# 		for key, value in inDict.items():
# 			if isinstance(value, list):
# 				print("{0}{1}<{2}>".format('\t' * tabCount, key, value[0]))  # 叶子节点,ECU
# 			else:
# 				print("{0}{1}".format('\t' * tabCount, key))  # 系统
#
# 			self.ShowAll(value, tabCount + 1)  # 继续递归
# 	else:  # 参数类型错误
# 		print(type(inDict))
# 		raise ValueError
# 	pass


from copy import  deepcopy   #深拷贝
from copy import  copy  #浅拷贝



def HereditaryTraverse(inDict, preStr):
	'''
	每次都从根开始遍历,  即保存"祖先"的信息 , 我称之为 "遗传遍历" 
	:param inDict: 
	:param preStr: 
	:return: 
	'''

	if isinstance(inDict, list):
		for item in inDict:
			print("{0}{1}".format(preStr, item))
		return
	elif isinstance(inDict, dict):
		for k, v in inDict.items():
			tmpPreStr = preStr + k
			HereditaryTraverse(v, tmpPreStr)
	else:
		pass

	pass

def HereditaryTraverse2(inDict, preStr, leafNodeType = list):
	'''
	每次都从根开始遍历,  即保存"祖先"的信息 , 我称之为 "遗传遍历" 
	:param inDict: 
	:param preStr: 
	:param leafNodeType: 保存叶子节点的"容器" 一般为 list
	:return: 
	'''

	if isinstance(inDict, leafNodeType):
		for item in inDict:
			print("{0}{1}".format(preStr, item))
		return
	elif isinstance(inDict, dict):
		for k, v in inDict.items():
			tmpPreStr = preStr + k
			HereditaryTraverse(v, tmpPreStr)
	else:
		pass

	pass


def HereditaryTraverse3(inDict, preStr = '', separator = '\t', leafNodeType = list):
	'''
	每次都从根开始遍历,  即保存"祖先"的信息 , 我称之为 "遗传遍历" 
	:param inDict: 
	:param preStr: 
	:param leafNodeType: 保存叶子节点的"容器" 一般为 list
	:return: 
	'''

	if isinstance(inDict, leafNodeType):
		for item in inDict:
			print("{0}{1}{2}".format(preStr, separator, item))
	elif isinstance(inDict, dict):
		for k, v in inDict.items():
			tmpPreStr = preStr +  k + separator
			HereditaryTraverse3(v, tmpPreStr)
	else:
		pass
	pass


def main():

	menuDirPath = "../../txt/Rootmenu/"
	for eachMenu in os.listdir(menuDirPath):
		rm = RootMenu(os.path.join(menuDirPath, eachMenu))
		#rm.ShowAll()
		HereditaryTraverse3(rm.menuDict)
		break


	# d = {'A' : {'B':['C', 'D'], 'E':['F', 'G']}}
	# HereditaryTraverse3(d, '\t')

	pass


if __name__ == "__main__":

	main()

	pass