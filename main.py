#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Read number to string
#main.py

def readnum(numbr):#result = a name-vi a number
	result = "";
	if numbr ==0:	
		result = "Không"
	elif numbr ==1: 
		result = "Một"
 	elif numbr ==2:
		result = "Hai"
	elif numbr ==3: 
		result = "Ba"
 	elif numbr ==4:
		result = "Bốn"
	elif numbr ==5: 
		result = "Năm"
 	elif numbr ==6:
		result = "Sáu"
	elif numbr ==7: 
		result = "Bảy"
 	elif numbr ==8:
		result = "Tám"
	elif numbr ==9:
		result = "Chín"
	else:
		result = "{}".format(numbr)
	return result

def readxy(numbr):#read a number with xy
	x=readnum(numbr/10)
	y=readnum(numbr%10)
	result = "";
	if numbr<20:
		if numbr==10:
			result = "Mười"
		elif numbr%10==5:
			result = "Mười Lăm"
		else:
			result = "Mười {}".format(y)
	else:
		if numbr%10==0:
			result = "{} Mươi".format(x)
		elif numbr%10==1:
			result = "{} Mốt".format(x)
		elif numbr%10==5:
			result = "{} Lăm".format(x)
		else:
			result = "{} {}".format(x, y)
	return result

def readxyz(numbr):#read a number with xyz
	result = "";
	x=readnum(numbr/100)
	yz=readxy(numbr%100)
	z=readnum(numbr%10)

	if numbr<10:
		result = readnum(numbr)
	elif numbr<100:
		result = readxy(numbr)
	elif numbr<1000:
		if numbr%100==0: #x00
			result = "{} Trăm".format(x)
		elif (numbr%100)/10==0: #x0z
			result = "{} Trăm Lẻ {}".format(x,z)
		else:
			result = "{} Trăm {}".format(x, yz)
	else:
		result = "{}".format(numbr)
	return result.lower().capitalize()

#while 1:
#	num=readxyz(int(raw_input("please enter a number 0-9: ")))
#	print num
#chuyen chuoi thanh mang
def converArrtoStr(str):
	arr=str.split(' ')
#vì split trả về arr là mảng chuỗi nên ta phải chuyển sang mảng số.
	for i in range(0,len(arr)):
		arr[i]=int(arr[i])
	return arr

#Doc so tu mang:
def readNumofArray(arr):
	str=""
	#sorted(arr)
	for i in arr:
		if i==arr[len(arr)-1]:
			str+=readxyz(int(i))
		else:
			str+=readxyz(int(i))+" - "
	return str;

strnum=raw_input("Nhập chuỗi số nguyên dương cách nhau bởi khoảng trắng:\n\
	**Enter để bỏ qua**\n")
if strnum!="":
	try:
		arr=sorted(converArrtoStr(strnum))
		print "Chuỗi số tăng dần: ",arr
		print readNumofArray(arr)
	except Exception as e:
		print "Chuỗi nhập vào không đúng định dạng."
		print e

