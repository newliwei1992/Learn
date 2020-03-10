# def data(**kwargs):
# 	return dict(sorted(kwargs.items(),key=lambda item:item[0]))
# dict1={'维':'111','李':'2222'}
#
# print(data(name=1,pwd=2))

def register():
	'''实现账户的注册功能'''
	username=input("请输入账号：\n")
	password=input("请输入密码：\n")

	temp=username+'|'+password
	with open('login.md','a') as f:
		f.write(temp)

def login():
	'''登陆函数'''
	username=input("输入账号：\n")
	password=input("输入密码：\n")
	with open('login.md','r') as f:
		info=f.read()
	info=info.split('|')
	print(info)
	if username==info[0] and password==info[1]:
		return True
	else:
		return False
print(login())