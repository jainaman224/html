ans1=0
ans2=0
import math
for i in range(0,101):
	ans1=ans1+math.pow(i,2)
for i in range(0,101):
	ans2=ans2+i
ans2=math.pow(ans2,2)

ans=ans2-ans1
print ans