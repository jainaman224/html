def isPrime(a):
	m=0
	for j in range(1,a/2+1):
		if (a%j)==0:
			m+=1
	return m+1
i=1
n=1
div=500
while (i>=1):
	l=isPrime(i)
	ans=i
	if l>div:
		print ans
		break
	n+=1
	i=n*(n+1)/2