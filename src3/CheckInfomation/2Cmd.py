#!coding:utf8

'''
Date:2018/1/12/16:17
Author:yqq
Description:  
	
	有两个 DStreamCmd 的

'''

gInDir = u"../../txt/中国通用/Type1/Information.txt"

def main():

	lines = []
	with open(gInDir, "r") as inFile:
		lines = inFile.readlines()

		for i in range(len(lines)):
			line = lines[i]
			if "DStreamCmd" in line:
				if "DStreamCmd" in lines[i + 1]:
					print(i + 1)




	pass


if __name__ == "__main__":

	main()

	pass