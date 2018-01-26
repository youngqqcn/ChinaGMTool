#!coding:utf8

'''
Date:2018/1/20/15:53
Author:yqq
Description:  dtc.txt 中  lib=0000

	但是在 dtclib中有它对应的的库   即 索引的 第2个 和 第3个字节

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
			pass
		except:
			pass
	tt.WriteFile("../doc/tmp/2018_01_20_Dtc.txt")




	pass


if __name__ == "__main__":

	main()

	pass