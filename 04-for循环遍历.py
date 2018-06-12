
'''
str = 'laowang'
for i in str:
	print(i)
'''

#range()

#random.randint()  有头有尾

for i in range(10,-1,-1):    #有头无尾   
#	print(i)
	pass
'''
for i in range(101):
		print(i)
		break   
'''   

'''
def sum(x,y):
	return x + y
from functools import reduce
print(reduce(sum,range(1,101)))
'''

def sum():
	sum = 0
	for i in range(1,101):
		sum = sum + i 
	return sum
print(sum())
	
	


