#!coding:utf8

'''
Date:2017/10/20/13:46
Author:yqq
Description: 统计Dtc.txt中的[Protocol]下的Menu种类
'''

# 其中 0X0000D93 是数据流的menu

def main():

	with open(u"../../txt/中国通用/Type1/Dtc.txt", "r") as inFile:
		lineList = inFile.readlines()
		menuDict = {}
		for  i in range(len(lineList)):
			if 'Menu=' in lineList[i]:
				tmpMenu = lineList[i][lineList[i].find('=') + 1 : lineList[i].rfind('\t') - 1]
				if tmpMenu.strip() not in menuDict:
					menuDict[tmpMenu.strip()] =  1
				else:
					menuDict[tmpMenu.strip()] += 1

		for menu,count in menuDict.items():
			print(menu + "=" + str(count))


	pass


if __name__ == "__main__":

	main()

	pass