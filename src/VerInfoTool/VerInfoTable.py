#!coding:utf8

'''
Date:2017/12/11/10:30
Author:yqq
Description:none
'''

from lib.mytool12 import TextTool
from lib.mytool12 import Add0x
from lib.mytool12 import Del0x


gEcuIdList = []

def GetEcuIdList(filePath):
	with open(filePath, "r") as inFile:
		linesList  = inFile.readlines()
		for line in linesList:
			gEcuIdList.append(line.strip())


def main():

	GetEcuIdList(u"../../txt/中国通用_所有索引.txt")

	infoFilePath =  u"../../txt/中国通用/Type1/Information.txt"
	tt = TextTool(infoFilePath)
	#tt.ShowAll()

	with open(u"../../doc/tmp/中国通用_版本信息表_12_13.txt", "w") as outFile:
		allSectDict = tt.allSectDictOfFile
		for sectKey in allSectDict:
			if Del0x(sectKey) not in gEcuIdList:
				continue
			sectDict = allSectDict[sectKey]
			#print ('{0}\t'.format(Del0x(sectKey))),  #索引

			if "INFORMATION" in sectDict:
				if "InfoMode" in sectDict["INFORMATION"]:
					outFile.write('{0}\t'.format(Del0x(sectKey)))
					outFile.write('{0}\t'.format(sectDict["INFORMATION"]["InfoMode"][0]))
				elif "Menu" in sectDict["INFORMATION"]:
					tmpStr = sectDict["INFORMATION"]["Menu"][0]
					for tmpAddr in tmpStr.split(","):
						outFile.write('{0}\t'.format(Del0x(sectKey)))
						if tmpAddr in sectDict:
							if "InfoMode" in sectDict[tmpAddr]:
								outFile.write('{0}\t'.format(sectDict[tmpAddr]["InfoMode"][0]))

							if "Protocol" in sectDict:
								if "Protocol" in sectDict["Protocol"]:
									outFile.write('{0}\t'.format(sectDict["Protocol"]["Protocol"][0]))
								if "ToolID" in sectDict["Protocol"]:
									outFile.write('{0}\t'.format(sectDict["Protocol"]["ToolID"][0]))
								if "EcuID" in sectDict["Protocol"]:
									outFile.write('{0}\t'.format(sectDict["Protocol"]["EcuID"][0]))
							if "DStreamCmd" in sectDict[tmpAddr]:
								outFile.write('{0}\t'.format(sectDict[tmpAddr]["DStreamCmd"][0]))
							outFile.write("\n")
					continue  #继续后面的


			if "Protocol" in sectDict:
				if "Protocol" in sectDict["Protocol"]:
					outFile.write('{0}\t'.format(sectDict["Protocol"]["Protocol"][0]))
				if "ToolID" in sectDict["Protocol"]:
					outFile.write('{0}\t'.format(sectDict["Protocol"]["ToolID"][0]))
				if "EcuID" in sectDict["Protocol"]:
					outFile.write('{0}\t'.format(sectDict["Protocol"]["EcuID"][0]))
			if "INFORMATION" in sectDict:
				if "DStreamCmd" in sectDict["INFORMATION"]:
					outFile.write('{0}\t'.format(sectDict["INFORMATION"]["DStreamCmd"][0]))
			outFile.write("\n")
	pass


if __name__ == "__main__":

	main()

	pass