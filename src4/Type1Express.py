#!coding:utf8

'''
Date:2018/1/18/14:26
Author:yqq
Description: 修改 Express.txt 中的  
			Switch...Case 语句   没有default的
			
	猜想1:   所有switch..case语句  都是用于 "文本" 算法;
'''


gExpPath = u"../txt/中国通用/express.txt"

gOutExpPath = u'../doc/tmp/express_2018_1_18_14_55.txt'


def main():

	tmpList = []
	with open(gExpPath, "r") as inFile, open(gOutExpPath, "w") as outFile:

		lines = inFile.readlines()

		for line in lines:

			if ("switch" in line) and ("case" in line) and ("default" not in line):
				#print(line)
				tmpList.append(line)
				if "string y;" in line: #   y是字符串
					line = line.replace(r'}"', r'default: y=\"0x82,0xFF,0x40,0x00,0x36,0xCE\"; break;}"') #设置为空

				if ("int y;" in line):
					print(line)

			outFile.write(line)

	print(len(tmpList))

	pass


if __name__ == "__main__":

	main()

	pass