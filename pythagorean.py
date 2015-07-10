import math
l=1000
for i in range(l/4,(3*l/4)):
	for k in range(1,l/2):
		j=l-i-k
		if (math.pow(j,2)+math.pow(k,2))==math.pow(i,2):
			ans=i*j*k
			break

print ans