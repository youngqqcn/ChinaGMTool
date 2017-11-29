#!coding:utf8

'''
Date:2017/11/17/16:48
Author:yqq
Description:  处理Dtc.txt中 Menu错误     
'''

from lib.mytool11 import TextTool


def main():


	tt = TextTool(u"../../txt/中国通用/Type1/Dtc.txt")
	#tt = TextTool(u"../../doc/tmp/new_2017_11_17.txt")


	allSectDict = tt.allSectDictOfFile
	count = 0
	modeList = []
	for sectKey in allSectDict:
		try:
			sectDict = allSectDict[sectKey]
			if ("ReadDtc" in sectDict) and ("ClearDtc" in sectDict):
				if("Cmd" not in sectDict["ReadDtc"]) and (sectDict["Protocol"]["Menu"][0].strip() == "ReadDtc"):
					#print(sectDict["ReadDtc"]["Mode"]),
					#print(sectKey)

					#把[Protocol]中的Menu替换成成 ClearDtc
					sectDict["Protocol"]["Menu"][0] = "ClearDtc"
				count += 1
		except:
			pass

	print("总数: %d" % count)
	print("-----------")
	for mode in modeList:
		print(mode)


	tt.WriteFile("../../doc/tmp/new_2017_11_17.txt")  #写回文件
	pass


if __name__ == "__main__":

	main()

	pass