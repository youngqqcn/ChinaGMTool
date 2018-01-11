#!coding:utf8

'''
Date:2018/1/6/14:46
Author:yqq
Description: 
		将 express.txt中的   三目运算符  转为  if...else... 的形式
'''



def main():


	with open(u"../../txt/中国通用/express.txt", "r") as inFile, \
			open(u"../../doc/tmp/newExpress_1_6.txt", "w") as outFile:
		lines = inFile.readlines()


		iCount = 0
		for line in lines:
			newLine = line
			if ("?" in line)  and (":" in line):
				iCount += 1
				#处理三目运算符
				splitList = line.split(";")

				for exp in splitList[2:]:
					if ("?" in exp)  and (":" in exp):
						#print(">>>" + exp)
						y = exp[ : exp.find("=")]  #获取 y
						cond = exp[exp.find("=")+1 : exp.find("?")]  #获取条件
						frist  = exp[ exp.find("?") + 1  : exp.find(":") ]  #获取第 1 个值
						second = exp[ exp.find(":") + 1  :  ]  #获取第 2 个值

						newExp = "if({0}) {1}={2}; else {1}={3}".format(cond, y, frist, second)
						newLine = newLine.replace(exp, newExp)

				print(newLine)
			outFile.write(newLine)
			pass
		print(">>>>>>>>>>>>>> {0}".format(iCount) )




	pass


if __name__ == "__main__":

	main()

	pass