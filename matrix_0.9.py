def max(a,b):
	if a>b:
		return a
	else:
		return b
		
n=int(input().split()[0])
a=[]
b=[]
for i in range(n+1):
	b.append(0)
a.append(b)	
for i in range(n):
	b=[0]
	for j in input().split():
		b.append(int(j))
	a.append(b)
f=[]
for i in range(n+1):
	b=[]
	for j in range(n+1):
		b.append(0)
	f.append(b)	
for i in range(n):
	for j in range(n):
		f[i+1][j+1]=max(f[i+1][j],f[i][j+1])+a[i+1][j+1]
print(f[n][n])		