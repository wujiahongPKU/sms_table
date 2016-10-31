#!/bin/python
#!encode=utf-8


import codecs

from time import time

import sys
import os

def loadfile(infile1,infile2):
	fin1=codecs.open(infile1,'r','utf-8')
	fin2=codecs.open(infile2,'r','utf-8')
	fout=open('sms_label.txt','w+')
	for line1 in fin1.readlines():
		line1=line1.strip().split('\t')
		fout.write(str(line1[2].encode('utf-8'))+'\t')
		if str(line1[3])=="严重逾期":
			fout.write(str(1))
		else:
			fout.write(str(0))
	for line2 in fin2.readlines():
		line2=line2.strip().split('\t')
		fout.write(str(line2[2].encode('utf-8'))+'\t')
		if str(line2[3])=="严重逾期":
			fout.write(str(1))
		else:
			fout.write(str(0))

	fin1.close()
	fin2.close()
	fout.close()


if __name__=='__main__':
	loadfile('my_table_1.txt','my_table_2.txt')
	print "end"
