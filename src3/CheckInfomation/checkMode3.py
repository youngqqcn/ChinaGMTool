#!coding:utf8

'''
Date:2018/1/11/11:32
Author:yqq
Description: 检查版本模式3 

	有 InfoCmd  的 
	
	模式3  是否有组合的版本信息??
'''


from lib.mytool12 import TextTool
from lib.mytool12 import Del0x

gInDir = u"../../txt/中国通用/Type1/Information.txt"


def main1():
	tt = TextTool(gInDir)
	# tt.ShowAll()
	# def ShowAll(self):
	'''
	:return: 无
	打印
	'''
	indexList = []
	with open(u"../../txt/版本信息的索引.txt") as inFile:
		for line in inFile.readlines():
			indexList.append(line.strip())

	allSectDict = tt.allSectDictOfFile
	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]
		# print ('{0}'.format(sectKey))
		try:
			mode = int(sectDict["INFORMATION"]["InfoMode"][0], 10)
			if mode == 3:
				try:
					if("InfoCmd"  in  sectDict["INFORMATION"]):
						if Del0x(sectKey)  in indexList:
							print(Del0x(sectKey))
					pass
				except:
					pass

			pass
		except:
			pass


	pass


def main2():

	tt = TextTool(gInDir)

	allSectDict = tt.allSectDictOfFile
	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]

		try:
			mode = sectDict["INFORMATION"]["InfoMode"][0]
			if mode != "0003":
				continue
			else:
				print ('{0}'.format(sectKey))
				for filedKey in sectDict:
					filedDict = sectDict[filedKey]
					print ('[{0}]'.format(filedKey))
					for keyPairKey in filedDict:
						for listItem in filedDict[keyPairKey]:
							print('{0}={1}'.format(keyPairKey, listItem))
					print ('\n')
		except:
			pass
		pass
	pass



if __name__ == "__main__":

	#main1()
	main2()

	pass