#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import re                                                        #����������ʽģ�飺reģ��

def translate(inputFile, outputFile):
	fin = open(inputFile, 'r')                                   #�Զ��ķ�ʽ�������ļ�
	fout = open(outputFile, 'w')                                 #��д�ķ�ʽ������ļ�

	for eachLine in fin:                                         #���ж����ļ�����
		line = eachLine.strip().decode('utf-8', 'ignore')        #����ǰ������صĴ�������ת����Unicode��
		
		p2 = re.compile(ur'[^\u4e00-\u9fa5]')                    #���ĵı��뷶Χ�ǣ�\u4e00��\u9fa5
		
		zh = " ".join(p2.split(line)).strip()                    
		zh = ",".join(zh.split())

		outStr = zh                                              #������ش����õ����ĵ��ı�

		fout.write(outStr.strip().encode('utf-8') + '\n')
		
	fin.close()
	fout.close()

if __name__ == '__main__':
	translate(sys.argv[1], sys.argv[2])                          ##ͨ����������в��������������ļ�����ִ�У�����

