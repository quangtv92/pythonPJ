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

class ReadString(Readnumber):
	def __init__(self,str):
		arr=map(int,str.split())
		self.arr=sorted(arr)
		print "Number soted:\n",self.arr
		self.result=""

	def readnum(self):
		for temp in self.arr:
			if temp==self.arr[len(self.arr)-1]:
	##			self.result+="{}\n".format(Readnumber.readnum(temp))
			else:
	##			self.result+="{} - ".format(super(self.__class__,self).readnum(temp))
class ReadText(ReadString):
	def __init__(self,txtfile):
		self.str=""
		self.txt=txtfile
		try:
			file=open(self.txt)
			for line in file:
				self.str+=line
		except Exception as e:
			print e
		super(self.__class__,self).__init__(self.str)
##	ReadString.readnum(self.str)


num=ReadString("123 52 222 61 2")
num.readnum()
print num.result
#	print num.readnum()
#	num=ReadText('test.txt')

