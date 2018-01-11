#!coding:utf8

'''
Date:2018/1/2/17:47
Author:yqq
Description:  检查菜单
'''

import os

gInDir =  u"../../doc/tmp/RootMenu_1_2/"
gOutDir =  u"../../doc/tmp/RootMenu_1_2_m/"

def Check(fileName, inList, outFile):
	'''
	:param fileName: 当前正在检查的文件的文件名
	:param inList: 文件内容
	:return: 有错返回False, 否则返回True
	'''

	for i in range(len(inList)):

		eachLine = inList[i]


		# 2008  和 2005  2011 特殊情况  特殊处理
		if "2008" in fileName  and   (4846 <= i ) and ( i <= 4857 ):
			outFile.write("{0}".format(eachLine.replace("//", "")))
			continue

		if "2005" in fileName and ( 3684 <= i) and ( i <= 3690):
			outFile.write("{0}".format(eachLine.replace("//", "")))
			continue

		if "2011" in fileName and ( 1003 <= i) and ( i <= 1006):
			outFile.write("{0}".format(eachLine.replace("//", "")))
			continue


		if "//" in eachLine:
			outFile.write("{0}".format(eachLine))
			continue

		if i + 1 == len(inList):  #最后一行
			if "<0x" not in eachLine:
				print("{0} line{1} : {2}\n".format(fileName , i, inList[i].strip()))
				return False
			else:
				outFile.write("{0}".format(eachLine))
				continue

		if ("<0x" not in eachLine ): #如果没有"<0x", 那么, 它的下一行的tab数一定大于当前行的tab数
			delFlag = True
			for j in range(i + 1,  len(inList)):
				line = inList[j]
				if "//" not in line:
					if line.count('\t') <= eachLine.count('\t'):  #
						#outFile.write("//{0}\n".format(eachLine))
						delFlag = True
						break
					elif "<0x" in line:
						delFlag = False
						break
					else:
						pass

			if delFlag:
				print("yes")
				outFile.write("//{0}".format(eachLine))
			else:
				outFile.write("{0}".format(eachLine))

		else: #如果有"<0x", 那么, 它的下一行的tab一定不大于当前行的tab数
			outFile.write("{0}".format(eachLine))
			if inList[i+1].count('\t') > inList[i].count('\t'):
				print("{0} line{1} : {2}\n".format(fileName , i, inList[i].strip()))
				return False
	pass


def main():
	#return


	for fileName in os.listdir(gInDir):
		#print(fileName)
		filePath = os.path.join(gInDir, fileName)
		outFilePath = os.path.join(gOutDir, fileName)

		with open(filePath, "r") as inFile, open(outFilePath, "w") as outFile:
			lines = inFile.readlines()

			newList = []
			for line in lines:
				newList.append(line)


			Check(os.path.split(filePath)[1], newList, outFile=outFile)



	pass






if __name__ == "__main__":

	main()

	pass