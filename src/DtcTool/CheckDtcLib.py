#!coding:utf8

'''
Date:2017/12/11/20:34
Author:yqq
Description:  

	检查 DtcLib.txt  不对的地方

'''


def main():


	inFilePath = u"../../txt/中国通用/DtcLib.txt"
	outFilePath = u"../../doc/tmp/new_DtcLib.txt"

	newLines = []
	with open(inFilePath, "r") as inFile , open(outFilePath, "w") as outFile:
		lines = inFile.readlines()

		for i in range(len(lines)):
			line = lines[i]
			if line[0:2].upper() == "0X":
				nextLine = lines[i + 1]
				if "[LIB]" not in nextLine.upper().strip():
					newLines.append(line)
					newLines.append("[LIB]\t\\n\\\n")
					print (i)
					continue
			newLines.append(line)

		outFile.writelines(newLines)

	pass


if __name__ == "__main__":

	main()

	pass