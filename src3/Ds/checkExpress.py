#!coding:utf8

'''
Date:2018/1/5/18:34
Author:yqq
Description:none
'''




from lib.mytool12 import InList


def main():

	indexList = []
	with open(u"../../txt/1_5.txt", "r") as inFile:
		indexList = inFile.readlines()


	iCount = 0
	with open(u"../../txt/中国通用/Type1/Ds.txt", "r") as inFile:
		lines = inFile.readlines()

		for eachIndex in indexList:

			if InList(eachIndex, lines):
				iCount += 1
				print (eachIndex)


	print(iCount)



	pass


if __name__ == "__main__":

	main()

	pass