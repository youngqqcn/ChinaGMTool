#!coding:utf8

'''
Date:2018/1/20/16:42
Author:yqq
Description:  获取两个文件中 的差集
'''

file1Path = "../txt/1_20/1.txt"
file2Path = "../txt/1_20/2.txt"



def main():

	with open(file1Path, "r") as inFile1, open(file2Path, "r") as inFile2:
		lines1 = inFile1.readlines()
		lines2 = inFile2.readlines()


		list1 = []
		list2 = []

		for line in lines1:
			if "=" in line:
				tmp = line[:line.find("=")]
				list1.append(tmp)

		for line in lines2:
			if "=" in line:
				tmp = line[:line.find("=")]
				list2.append(tmp)

		set1 = set(list1)
		set2 = set(list2)

		#print(len(set1))
		#print(len(set2))

		set3 = set1 - set2

		# print(len(set3))

		for item in set3:
			print(item)


	pass


if __name__ == "__main__":

	main()

	pass