#!/usr/bin/env python
#--*-- coding:utf8 --*--
import ReadNumberUseClass
n=ReadNumberUseClass.Readnumber()
try:
	#read number form string input 
	print "Read number form string input :".upper().center(100,'*')
	result=n.readstring('123 41 16 642\n13 50 4 51')
	print result
	#read number form text file input
	print "Read number form text file input :".upper().center(100,'*')
	fromtext=n.readtext('test.txt')
	print "Number as name:\n",fromtext
except Exception as e:
	print e
