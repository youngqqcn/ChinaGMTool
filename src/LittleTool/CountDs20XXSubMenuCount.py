#!coding:utf8

'''
Date:2017/11/29/18:01
Author:yqq
Description:  计算  在  8250 中查找文本的数据流项, 它的文本是否也在8250中找
'''

from lib.mytool12 import TextTool



def main():


	tt = TextTool(u"../../txt/中国通用/Type1/Ds.txt")

	#tt.ShowAll()

	allSectDict = tt.allSectDictOfFile
	for sectKey in allSectDict:

		if(sectKey.split(',')[0] != "0x20"):
			continue


		sectDict = allSectDict[sectKey]
		#print ('{0}'.format(sectKey))

		if "DATASTREAM" in sectDict:
			if "Menu" in sectDict["DATASTREAM"]:
				strValue = sectDict["DATASTREAM"]["Menu"][0]
				subMenuTitleList = strValue.split(',')

				if len(subMenuTitleList) > 1:
					print(sectKey)

		#结论:  所有在 8250中查找的数据流, 都只有一个 数据流子菜单

	pass


if __name__ == "__main__":

	main()

	pass