#!coding:utf8

'''
Date:2017/10/20/11:49
Author:yqq
Description: 统计菜单模式1的,读码模式种类
'''




def main():

	with open(u"../../txt/中国通用/Type1/Dtc.txt", "r") as inFile:
		lineList = inFile.readlines()
		modeList = []
		for  i in range(len(lineList)):
			if '[ReadDtc]' in lineList[i]:
				tmpStr = lineList[i + 1]
				mode = tmpStr[tmpStr.find('=') + 1: tmpStr.find('=') + 5]
				if mode not in modeList:
					modeList.append(mode)

		for mode in sorted(modeList):
			print(mode)

	pass


if __name__ == "__main__":

	main()

	pass