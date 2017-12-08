#!coding:utf8

'''
Date:2017/12/1/17:54
Author:yqq
Description:none
'''



def main():

	#filePath = u"../../txt/2008科帕奇菜单.txt"
	filePath = u"../../txt/2012凯越菜单.txt"


	ecuIDSet = set()
	with open(filePath, "r") as inFile, \
			open(u"../../doc/tmp/2012凯越菜单EcuID.txt", "w") as outFile:
			#open(u"../../doc/tmp/2008科帕奇数据流ecuID.txt", "w") as outFile:\
		linesList = inFile.readlines()

		for line in linesList:
			if "数据流<0x" in line:
				if( line not in ecuIDSet ):
					print(line)
				tmpEcuID = line[line.find("0x") : line.find(">") ] + "\n"
				ecuIDSet.add(tmpEcuID)

		outFile.writelines(list(ecuIDSet))




	pass


if __name__ == "__main__":

	main()

	pass