print('')
print('')
print('-'*30)
print('-'*30)
print('欢迎来到王者荣耀!')
print('-'*30)
print('-'*30)



account = 'laowang'
pwd = 123456


name = input('请输入账号:')
print('-'*30)
print('-'*30)
userpwd = int(input('请输入密码:'))
print('-'*30)
print('-'*30)

if name == account and userpwd == pwd:
	print('-'*30)
	print('登录成功!')
	print('-'*30)
	number = int(input('请输入:0-ADC,1-肉,2-法师'))
	print('-'*30)
