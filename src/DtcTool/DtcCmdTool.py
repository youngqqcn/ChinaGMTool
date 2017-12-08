#!coding:utf8

'''
Date:2017/12/7/16:36
Author:yqq
Description:

	分析故障码命令 是否都是  A981 开头的 

'''

from lib.mytool12 import  TextTool


def main():

	dtcPath = u"../../txt/中国通用/Type1/Dtc.txt"

	tt = TextTool(dtcPath)

	#tt.ShowAll()
	cmdList = []
	allSectDict = tt.allSectDictOfFile
	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]
		#print ('{0}'.format(sectKey))
		if "ReadDtc" in sectDict:
			try:
				dtcCmd = sectDict["ReadDtc"]["Cmd"][0]
				if dtcCmd not in cmdList:
					cmdList.append(dtcCmd)
				#print(sectDict["ReadDtc"]["Cmd"][0])
			except:
				pass

	cmdList = sorted(cmdList)
	for cmd in cmdList:
		print(cmd)
	pass







	pass


if __name__ == "__main__":

	main()

	pass