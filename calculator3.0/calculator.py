import sys

#----------------???????????----------------
class Employee(object):
	def __init__(self,usr_filename):
		with open(usr_filename, 'r') as usr_file:
			usr_list = usr_file.readlines()	
		for str in usr_list:
			u_listtwo = str.split(',')
			usr_dictkey = u_listtwo[0].strip()
			usr_dictvalue = u_listtwo[1].strip().strip('\n')
			usr_dict[usr_dictkey] = usr_dictvalue

#----------------???????????----------------
	def calculator(self,gongzi_filename):
		for ID,salary in usr_dict.items():
			salary = int(salary)
			self.salary = salary

			if salary > config.JiShuH:
				JiShu = config.JiShuH
			elif salary < config.JiShuL:
				JiShu = config.JiShuL
			else:
				JiShu = salary

			self.id = str(ID)
			shebao = JiShu * (config.YangLao + config.YiLiao + config.ShiYe + config.GongShang + config.ShengYu + config.GongJiJin)
			self.shebao = format(shebao,'.2f')
			tax = salary - shebao - 3500			

			if tax <= 0:
				tax = 0
				rate = 0
				decute = 0
			elif tax <= 1500:
				rate = 0.03
				decute = 0
			elif 1500 < tax <= 4500:
				rate = 0.1
				decute = 105
			elif 4500 < tax <= 9000:
				rate = 0.2
				decute = 555
			elif 9000 < tax <= 35000:
				rate = 0.25
				decute = 1005
			elif 35000 < tax <= 50000:
				rate = 0.3
				decute = 2755
			elif 50000 < tax <= 80000:
				rate = 0.35
				decute = 5505
			elif 80000 < tax : 
				rate = 0.45
				decute = 13505

			taxrate = tax * rate - decute 
			self.taxrate = format(taxrate,'.2f')
			pay = salary - taxrate - shebao
			self.pay = format(pay,'.2f')			
			with open(gongzi_filename,'a') as gongzi_file:
				gongzi_file.write('{},{},{},{},{}\n'.format(self.id,self.salary,self.shebao,self.taxrate,self.pay))

#----------------??????----------------
class Config(object):
	def __init__(self,cfg_filename):		
		with open(cfg_filename, 'r') as cfg_file:
			cfg_list = cfg_file.readlines()
		for str in cfg_list:			
			c_listtwo = str.split('=')	
			cfg_dictkey = c_listtwo[0].strip() #strip()???????????(?????)????????
			cfg_dictvalue = c_listtwo[1].strip().strip('\n')
			cfg_dict[cfg_dictkey] = cfg_dictvalue #??????????

		self.JiShuL = float(cfg_dict['JiShuL'])
		self.JiShuH = float(cfg_dict['JiShuH'])
		self.YangLao = float(cfg_dict['YangLao'])
		self.YiLiao = float(cfg_dict['YiLiao'])
		self.ShiYe = float(cfg_dict['ShiYe'])
		self.GongShang = float(cfg_dict['GongShang'])
		self.ShengYu = float(cfg_dict['ShengYu'])
		self.GongJiJin = float(cfg_dict['GongJiJin']) #?????????

#----------------???----------------	
try:
	if __name__ == '__main__':
		cfg_dict = {}
		usr_dict = {}

#----------------???????????----------------
		cfg_index = sys.argv.index('-c')
		cfg_filename = './' + sys.argv[cfg_index + 1]
		config = Config(cfg_filename) 

#----------------??????????ID????----------------

		usr_index = sys.argv.index('-d')
		usr_filename = './' + sys.argv[usr_index + 1]
		usr = Employee(usr_filename)
		
#----------------?????????----------------
		gongzi_index = sys.argv.index('-o')
		gongzi_filename = './' + sys.argv[gongzi_index + 1]
		usr.calculator(gongzi_filename)

#----------------????----------------	
except:
	print('ParameterError')