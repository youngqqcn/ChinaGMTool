#!coding:utf8

'''
Date:2018/1/3/17:01
Author:yqq
Description:none
'''




def main():

	with open(u"../../txt/中国通用/CN_ROOT.txt", "r") as inFile:
		lines = inFile.readlines()
		tmpLines = lines[1:]
		tmpLines.reverse()
		tmpLines.insert(0, lines[0])

		newLines = tmpLines

		with open(u"../../doc/tmp/New_CN_ROOT.txt", "w") as outFile:
			outFile.writelines(newLines)

	pass


if __name__ == "__main__":

	main()

	pass