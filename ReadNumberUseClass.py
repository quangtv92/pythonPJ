#!/usr/bin/env python
#--*-- coding:utf8 --*--
class Readnumber(object):
	def __init__(self):
		self.num=['Một','Hai','Ba','Bốn', 'Năm','Sáu','Bảy','Tám','Chín']

	def readX(self,x):
		for k,v in enumerate(self.num):
			if x==k+1:
				return v

	def readXY(self,xy):
		value=""
		x, y=xy/10, xy%10
		if x==1:
			if y==0:
				value='Mười'
			elif y==5:
				value='Mười lăm'
			else:
				value='Mười '+self.readX(y)
		else:
			if y==0:
				value=self.readX(x)+" mươi"
			elif y==1:
				value=self.readX(x)+" mươi mốt"
			elif y==5:
				value=self.readX(x)+" mươi lăm"
			else:
				value=self.readX(x)+" mươi "+self.readX(y)
		return value.lower().capitalize()

	def readXYZ(self,xyz):
		value=""
		x, y, z,yz=xyz/100, xyz%100/10, xyz%100, xyz%100
		if x==1:
			if y==0:
				if z==0:
					value='Một trăm'
				else:
					value='Một trăm lẻ {}'.format(self.readX(z))
			else:
				value='Một trăm {}'.format(self.readXY(yz))		
		else:
			if y==0:
				if z==0:
					value='{} trăm'.format(self.readX(x))
				else:
					value='{} trăm lẻ {}'.format(self.readX(x),self.readX(z))
			else:
				value='{} trăm {}'.format(self.readX(x),self.readXY(yz))
		return value.lower().capitalize()

	def readnum(self,anum):
		if anum<10:
			return self.readX(anum)
		elif anum<100:
			return self.readXY(anum)
		else:
			return self.readXYZ(anum)

	def readstring(self,str):
		arr=map(int,str.split())
		arr=sorted(arr)
		print "Number soted:\n",arr
		result=""
		for temp in arr:
			if temp==arr[len(arr)-1]:
				result+="{}\n".format(self.readnum(temp))
			else:
				result+="{} - ".format(self.readnum(temp))
		return result

	def readtext(self,txt):
		str=""
		try:
			file=open(txt)
			for line in file:
				str+=line
			return self.readstring(str)
		except Exception as e:
			print e
		

