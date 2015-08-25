def array(n):
	a=[]
	for i in range(n):
		a.append(0)
	return a
	
def array2(m,n):
	a=[]
	for i in range(m):
		b=array(n)
		a.append(b)
	return a
	
def max(a,b):
	if a>b:
		return a
	else:
		return b
		
n=int(input().split()[0])
a=array2(n+1,n+1);
f=array2(n+1,n+1);

for i in range(n):
	j=0
	for k in input().split():
		a[i+1][j+1]=int(k)
		j+=1
		
for i in range(n):
	for j in range(n):
		f[i+1][j+1]=max(f[i+1][j],f[i][j+1])+a[i+1][j+1]
print(f[n][n])		