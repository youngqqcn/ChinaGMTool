#!coding:utf8

'''
Date:2017/10/30/16:09
Author:yqq
Description:none
'''

import os
import sys


gIndexDict = {}
gIndexList = []


def ReadMenu():

	for fileName in os.listdir(u"../../txt/中国通用/RootMenu/"):
		# print(fileName)
		with open(u"../../txt/中国通用/RootMenu/{0}".format(fileName), "r") as inFile:
			for line in  inFile.readlines():
				line = line.strip()
				if ('<0x' in line) & ( '>' in line):
					index = line[line.find('<0x') + 1 : line.find('>')]
					if(index not in gIndexList):
						#print(index.strip())
						continue
					#name = line.strip()[line.strip()[ : line.strip().find('<0x')]]
					name = line[ : line.find('<0x') ]

					global gIndexDict
					if index not in gIndexDict:
						gIndexDict[index] = []
					if  name not in gIndexDict[index]:
						gIndexDict[index].append(name)


def ReadIndex():

	with open(u"../../txt/tmpMode.txt", "r") as inFile:
		indexList  = inFile.readlines()
		for index in indexList:
			if len(index.strip()) == 0:
				continue
			else:
				gIndexList.append(index.strip())

	pass


def main():
	ReadIndex()
	#print(len(gIndexList))
	#print(gIndexList[0])
	#print(gIndexList[1])
	ReadMenu()

	#print(len(gIndexDict))

	for index in gIndexDict:
		if len(gIndexDict[index]) > 1 :
			print('{0}  ['.format(index)),
			for item in gIndexDict[index]:
				print(item + ","),
			print(']')
			# print(index)


	pass


if __name__ == "__main__":

	main()

	pass