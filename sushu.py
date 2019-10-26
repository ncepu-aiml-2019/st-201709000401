import math
print("素数：")
print(2)
print(3)
for i in range(5,100):
	a=0
	m=int(i/2)
	for x in range(2,m):
		if i%x==0:
			a=1
			break
	if a==0:
		print(i)