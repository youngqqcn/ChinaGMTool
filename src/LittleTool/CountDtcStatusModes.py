#!coding:utf8

'''
Date:2017/10/26/9:56
Author:yqq
Description:none
'''



def main():

	statusDict = {}
	with open(u"../../txt/中国通用/Type1/Dtc.txt", "r") as inFile:
		linesList = inFile.readlines()
		for eachLine in linesList:
			if ("Status=" in eachLine):
				if eachLine.replace('\\n\\', '').strip() not in statusDict:
					#statusList.append(eachLine.replace('\\n\\', '').strip())
					statusDict[eachLine.replace('\\n\\', '').strip()] = 1
				else:
					statusDict[eachLine.replace('\\n\\', '').strip()] += 1

	#key[0],是对键进行排序, key[1]是对值进行排序
	statusList =  sorted(statusDict.iteritems(), key=lambda key:key[1], reverse=True)

	for tp in statusList:
		print("{0}\t{1}".format(tp[0], tp[1]))

	#for key, value in statusDict.items():
	#	print("{0}={1}\n".format(key, value))


	#for status in sorted(statusList):
	#	print(status)

	#print("\n=====\n共计:{0}\n\n".format(len(statusList)))

	pass


if __name__ == "__main__":

	main()

	pass