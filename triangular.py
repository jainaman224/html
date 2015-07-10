import math
 
 
def isprime(n):
	for num in range(2,int(math.floor(math.sqrt(n))+1)):
		if n%num==0:
			return(False)
	return(True)
 
def findfactors(n):
	primes=[]
	b=0
	for num in range(2,int(math.floor(n/2)+1)):
		if isprime(n):
			primes.append(n)
			break
		c=n
		if(n%num==0 and isprime(num)):
			
			c=n/num
			primes.append(num)
			while(c%num==0):
				primes.append(num)
				b=c
				c=b/num
		n=c
	return(primes)
 
print findfactors(100)
