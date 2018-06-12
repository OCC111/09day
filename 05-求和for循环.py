sum1 = 0                #定义一个变量，将 0 赋值给sum1
sum2 = 0
for i in range(0,101):  #循环0~100，，，，for循环有头无尾
	if i % 2 == 0:      #判断是否能被2整除
		sum1 += i       
	else:
		sum2 += i
print('偶数和:%d'% sum1)#输出偶数的和，‘%’表示占位
print('奇数和:%d'% sum2)
print('总和:%d'% (sum1+sum2))

