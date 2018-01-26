#!coding:utf8

'''
Date:2018/1/17/9:36
Author:yqq
Description:  修改 Type1/Dtc.txt 中 的
	
	只有读码 没有清码的 情况
	
	将 ReadDtc  改为  ReadDtc,ClearDtc

'''

from lib.mytool12 import TextTool
from lib.mytool12 import Add0x
from lib.mytool12 import Del0x




gDtcPath = u"../txt/中国通用/Type1/Dtc.txt"



def main():

	tt = TextTool(gDtcPath)
	#tt.ShowAll()

	allSectDict = tt.allSectDictOfFile
	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]
		#print ('{0}'.format(sectKey))
		try:
			menu = sectDict["Protocol"]["Menu"][0]
			if menu.upper() == "READDTC":
				if "ClearDtc" in sectDict:
					if "Cmd" in sectDict["ClearDtc"]:
						#替换掉
						tt.allSectDictOfFile[sectKey]["Protocol"]["Menu"] = ["ReadDtc,ClearDtc"]
			pass
		except:
			pass
	tt.WriteFile("../doc/tmp/2018_01_17_Dtc.txt")




	pass


if __name__ == "__main__":

	main()

	pass