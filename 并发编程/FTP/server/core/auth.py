import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Auth:
	def laned(self,msg):
		pass


	def registered(self,msg):
		with open('%s/conf/userinfo'%BASE_DIR,'a') as f:
			try:
				user_dir = '%s/home/%s'%(BASE_DIR,msg['username'])
				os.mkdir(user_dir)
				l = [msg['username'],msg['password']]
				f.write('|'.join(l))
			except FileExistsError:#不能创建同名字的文件夹
				print('该用户已存在')