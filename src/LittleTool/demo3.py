#!coding:utf8

'''
Date:2017/11/3/13:47
Author:yqq
Description: 统计cn_OBD_dtc.txt中的7F组中的故障码码号,是否唯一(别的组里面没有)
'''


from  lib.mytool11 import ReadTextPlus


def main():

	# with open(u"../../txt/中国通用/Type1/cn_OBD_dtc.txt", "r") as inFile:
	# 	linesList = inFile.readlines()
	# 	for line in linesList:
	# 		print(line)

	rt = ReadTextPlus(u"../../txt/中国通用/Type1/cn_OBD_dtc.txt")
	#print(len(rt))



	list7F = []
	groutIDList = []
	for key, value in rt.items():
		# print(key.split(","))
		groupID = key.split(",")[3]
		# print(groupID)
		dtcCode = value[0]
		if groupID not in groutIDList:
			groutIDList.append(groupID)
		#dtcText = value[2]


	for eachID in groutIDList:
		print(eachID)


		# if groupID == '0x7F':
		# 	list7F.append(dtcCode)


	# for key, value in rt.items():
	# 	groupID = key.split(",")[3]
	# 	dtcCode = value[0]
	# 	dtcText = value[1]
	# 	#print(dtcCode)
	# 	if (groupID != "0x7F") and (dtcCode in list7F):
	# 		print(groupID + " " + dtcCode + " "  + dtcText)










	pass


if __name__ == "__main__":

	main()

	pass