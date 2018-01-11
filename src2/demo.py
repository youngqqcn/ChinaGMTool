#!coding:utf8

'''
Date:2017/12/20/10:29
Author:yqq
Description:none
'''

from lib.mytool12 import TextTool


def main():

	tt = TextTool(u"../txt/中国通用/Type1/Ds.txt")

	# tt.ShowAll()


	allSectDict = tt.allSectDictOfFile
	for sectKey in allSectDict:
		sectDict = allSectDict[sectKey]
		print ('{0}'.format(sectKey))
		for filedKey in sectDict:
			filedDict = sectDict[filedKey]
			print ('[{0}]'.format(filedKey))
			for keyPairKey in filedDict:
				for listItem in filedDict[keyPairKey]:
					print('{0}={1}'.format(keyPairKey, listItem))
			print ('\n')

	pass


if __name__ == "__main__":

	main()

	pass