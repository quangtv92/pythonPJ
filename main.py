#!/usr/bin/env python
# -*- coding:utf-8 -*-
#R number in string

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
	result = "";
	if numbr<20:
		if numbr==10:
			result = "Mười"
		else:
			result = "Mười {}".format(readnum(numbr%10))
	else:
		if numbr%10==0:
			result = "{} Mươi".format(readnum(numbr/10))
		elif numbr%10==1:
			result = "{} Mươi Mốt".format(readnum(numbr/10))
		else:
			result = "{} Mươi {}".format(readnum(numbr/10), readnum(numbr%10))
	return result

def readxyz(numbr):#read a number with xyz
	result = "";
	if numbr<10:
		result = readnum(numbr)
	elif numbr<100:
		result = readxy(numbr)
	elif numbr<1000:
		if numbr%100==0: #x00
			result = "{} Trăm".format(readnum(numbr/100))
		elif (numbr%100)/10==0: #x0z
			result = "{} Trăm Lẻ {}".format(readnum(numbr/100),readnum(numbr%10))
		else:
			result = "{} Trăm {}".format(readnum(numbr/100), readxy(numbr%100))
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
#function return sorted array
def sorted_array(arr):
	for i in range(0, len(arr)-1):
		for j in range(i+1, len(arr)):
			if arr[i]>arr[j]:
				temp=arr[i]
				arr[i]=arr[j]
				arr[j]=temp
	return arr

#ham sorted cua he thong
#print sorted(arr)
#Doc so tu mang:
def readNumofArray(arr):
	str=""
	sorted_array(arr)
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
		arr=converArrtoStr(strnum)
		print "Chuỗi số tăng dần: ",sorted_array(arr)
		print readNumofArray(arr)
	except Exception as e:
		print "Chuỗi nhập vào không đúng định dạng."
		print e

