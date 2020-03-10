# def data(**kwargs):
# 	return dict(sorted(kwargs.items(),key=lambda item:item[0]))
# dict1={'维':'111','李':'2222'}
#1111111
# print(data(name=1,pwd=2))

def register():
	'''实现账户的注册功能'''
	username=input("请输入账号：\n")
	password=input("请输入密码：\n")

	temp=username+'|'+password
	with open('login.md','w') as f:
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

def getNick(func):
	with open('login.md','r') as f:
		info=f.read()
	info=info.split('|')
	if func:
		print('{0}你好，欢迎访问无涯课堂'.format(info[0]))
	else:
		print('请登陆系统')

if __name__=='__main__':
	while True:
		t=int(input('1、注册 2、登陆 3、退出\n'))
		if t==1:
			register()
		elif t==2:
			getNick(login())
		elif t==3:
			import sys
			sys.exit(1)
		else:
			print('输入错误，请继续！')
			continue
