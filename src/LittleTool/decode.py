#!coding:utf8

'''
Date:2017/10/23/20:26
Author:yqq
Description:none
'''
import  os
import sys


def MyWaldDir(path):
	pathList =[]
	for dirpath,dirnames,filenames in os.walk(path):
		for file in filenames:
			fullpath=os.path.join(dirpath,file)
			pathList .append(fullpath)
	return pathList


def Convert(filePath):
	'''
	:param filePath: 文件路径
	:return: 
	'''

	if('.pdf' in filePath) | ('.doc' in filePath) | ('.jpg' in filePath):
		return

	with open(filePath, "r") as inFile:
		linesList = inFile.readlines()
		newFileName = ''
		if '.cpp' in filePath:
			newFileName = filePath.replace('.cpp', '_cpp')
		elif '.h' in filePath:
			newFileName = filePath.replace('.h', '_h')
		elif '.txt' in filePath:
			newFileName = filePath.replace('.txt', '_txt')
		else:
			return
		with open(newFileName, "w") as outFile:
			outFile.writelines(linesList)
	pass



def DeConvert(filePath):
	'''
	:param filePath: 文件路径
	:return: 
	'''

	if('.pdf' in filePath) | ('.doc' in filePath) | ('.jpg' in filePath):
		return

	newFileName = ''
	if '_cpp' in filePath:
		newFileName = filePath.replace('_cpp', '.cpp')
	elif '_h' in filePath:
		newFileName = filePath.replace('_h', '.h')
	elif '_txt' in filePath:
		newFileName = filePath.replace('_txt', '.txt')
	else:
		return
	os.rename(filePath, newFileName)  #重命名
	pass

def Clean(filePath):

	if ('_cpp' in filePath) | ('_h' in filePath) | ('_txt' in filePath):
		os.remove(filePath)

	pass

def main():

	funcObj = ''
	if "--clean" ==  sys.argv[1].lower().strip():
		funcObj = Clean
	elif "--convert" == sys.argv[1].lower().strip():
		funcObj = Convert
	elif '--deconvert' == sys.argv[1].lower().strip():  #将 '_后缀名', 改回 '.后缀'
		funcObj = DeConvert
	else:
		print("usage: \n decode --clean  #clean \n decode --convert   #convert\n ")


	for fileName in  MyWaldDir("SRC"):
		funcObj(fileName)
	for fileName in  MyWaldDir("LIBTEXT"):
		funcObj(fileName)
	pass


if __name__ == "__main__":

	main()

	pass