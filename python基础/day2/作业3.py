

username = ['tom', 'jack', 'jom']
password = 123

file = open('user.txt','r')
f = file.readlines()
f = f.__str__()


while True:
	_username =input("请输入用户名：")

	if _username in username:
		if _username in f:
			print("该用户登陆已被锁定，请联系管理员")
			break
		for i in range(3):
			_password = int(input('请输入密码'))
			if _password != password:
				print("密码输入错误,请重新输入")
				if i == 2:
					file = open("user.txt",'a+')
					file.writelines(_username+'\n')
					file.close()
					print("用户已被锁定")
					exit()


			else:
				print("登陆成功，欢迎你！%s "%(_username))
				exit()


