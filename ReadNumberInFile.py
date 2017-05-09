#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Read number in text file
#ReadNumberInFile.py
import main
#tao mang so tu file *.txt
def str_num_text(txtfile):
	str=[]
	f=open(txtfile)
	try:
		for line in f:
			str+=main.converArrtoStr(line)
		return str
	except Exception as e:
		print "Error open file ",e
	finally:	
		f.close()

#test file
try:
	test_str=str_num_text("test.txt")
	print "Chuỗi trong file: ",test_str
	print "Xắp xếp chuỗi trong file: ",main.sorted_array(test_str)
	print "Đọc số: ",main.readNumofArray(test_str)
except Exception as e:
	print e
