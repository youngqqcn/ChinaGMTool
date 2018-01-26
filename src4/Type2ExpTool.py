#!coding:utf8

'''
Date:2018/1/25/15:04
Author:yqq
Description:将 模式2的 express.txt 中的 switch ... case 改成  if...else
'''


tmpExp = r'string y;BYTE x1;switch(((x1)>>2)&0x1){case 0x01:y=\"0x82,0x56,0x00,0x00,0x3E,0xB7\"; break;case 0x00:y=\"0x82,0x56,0x00,0x00,0x02,0xF6\"; break;default:y=\"0x82,0x56,0x01,0x00,0x90,0x46\"; break;}'


def Handle(inExpStr):

	if "string y;" not in inExpStr:
		return inExpStr
	if "switch" not in inExpStr:
		return inExpStr






	pass


def main():




	pass


if __name__ == "__main__":

	main()

	pass