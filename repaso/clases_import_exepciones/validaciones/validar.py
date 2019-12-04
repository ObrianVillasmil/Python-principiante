class validar(object):

	def __init__(self,op,val):
		self.op =op
		self.val=val
		
	def validaString(self):
		while True:
			try:
				
				break
			except Exception as e:
				raise e
			finally:
				pass
			
	def validaInt(self,val):
		while True:
			try:
				valor = int(val);
				success = {
					'success': True,
					'valor' : valor 
				};
				break
			except Exception as e:
				success = {
					'success': False,
					'valor' : '' 
				};
			finally:
				return success

	
	def validaFloat(self,val):
		while True:
			try:
				valor = float(val);
				success = {
					'success': True,
					'valor' : valor 
				};
				break
			except Exception as e:
				success = {
					'success': False,
					'valor' : '' 
				};
			finally:
				return success

	def validaMail(self):
		pass


	def comprueba(self):
		if(self.op==1):
			return self.validaString(self.val)
		elif(self.op==2):
			return self.validaInt(self.val)
		elif(self.op==3):
			return self.validaFloat(self.val)
		elif(self.op==4):
			return self.validaMail(self.val)
		else:
			return 0
		