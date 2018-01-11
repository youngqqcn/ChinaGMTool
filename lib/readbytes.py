#!coding:utf8


def ReadBytes(fin, num):
	'''
	:param fin:  输入的文件
	:param num: 读取的个数
	:return: 读取到的数据(字符串)
	'''
	tempList = []
	for i in range(0, num):
		tempList.append(fin.read(1).encode('hex'))
	tempList.reverse()
	#print(''.join(tempList))
	return ''.join(tempList).upper()