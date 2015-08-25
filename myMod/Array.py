'''
	module for array like the one in c,java
'''
class Array:
	def array(self,n):
		a=[]
		for i in range(n):
			a.append(0)
		return a
		
	def array2(self,m,n):
		a=[]
		for i in range(m):
			b=self.array(n)
			a.append(b)
		return a
	