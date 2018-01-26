#!coding:utf8

'''
Date:2018/1/18/11:52
Author:yqq
Description: 替换Type2/Express.txt 中的 
'''

import  re


gInPath = u"../txt/中国通用/Type2/Express.txt"      #读的文件
gOutPath = u"../doc/tmp/Express_2018_1_18.txt"  #处理后的文件


def main():

	pattern = re.compile(r',[0-9A-Fa-f]{8}')   #正则表达式:  匹配 8位 16进制字符


	#打开两个文件,一个是读, 一个是写
	with open(gInPath, "r") as inFile, open(gOutPath, "w") as outFile:

		lines = inFile.readlines() #全部读出来, 放到链表里面, 每一行是一个元素

		for line in lines:  #遍历链表 中的每一行

			#在当前行 用正则表达式匹配, 匹配结果放到 matchList 这个链表里面
			matchList =  re.findall(pattern, line)

			#print(matchList) #打印一下当前行匹配的所有结果

			for match in matchList: #遍历所有匹配结果
				line = line.replace(match, ","+"0x"+match[1:] + "")  #进行替换, 在前面加上 "0x"

			outFile.write(line) #将处理后的当前行 写入文件

	pass


if __name__ == "__main__":

	main()

	pass