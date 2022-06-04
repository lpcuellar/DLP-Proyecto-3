class Parser:
	def __init__(self, tokens):
		self.tokens = tokens
		self.id_token = 0
		self.actual_token = self.tokens[self.id_token]
		self.last_token = ''

	def advance( self ):
		self.id_token += 1
		if self.id_token < len(self.tokens):
			self.actual_token = self.tokens[self.id_token]
			self.last_token = self.tokens[self.id_token - 1]

	def read(self, item, type = False):
		if type:
			if self.actual_token.type == item:
				self.advance()
				return True
			else:
				print ("Error sintactico esperando " + str(item))
				return False
		else:
			if self.actual_token.value == item:
				self.advance()
				return True
			else:
				print ("Error sintactico esperando " + str(item))
				return False
	def Expr(self):

		while self.actual_token.type == 'number' or self.actual_token.type == 'decnumber' or self.actual_token.value == '-' or self.actual_token.value == '(':
			self.Stat()
			self.read(";")
		self.read(".")
    
	def Stat(self):
		value
		print(str(value))

	def Expressionintresult>(self):
		result1,result2
		while self.actual_token.value == " "-"Term<result2>(.result1-=result2.)"or self.actual_token.value == " "-"Term<result2>(.result1-=result2.)":
			if self.actual_token.type == ' "-"Term<result2>(.result1-=result2.)': 
				self.read(' "-"Term<result2>(.result1-=result2.)',True)
				result1+=result2
			if self.actual_token.type == ' "-"Term<result2>(.result1-=result2.)': 
				self.read(' "-"Term<result2>(.result1-=result2.)', True)
				result1-=result2
				
		result=result1
		return result

	def Termintresult>(self):
		result1,result2
		while self.actual_token.value == " "/"Factorresult2>(.result1/=result2.)"or self.actual_token.value == " "/"Factorresult2>(.result1/=result2.)":
			if self.actual_token.type == ' "/"Factorresult2>(.result1/=result2.)': 
				self.read(' "/"Factorresult2>(.result1/=result2.)',True)
				result1*=result2
			if self.actual_token.type == ' "/"Factorresult2>(.result1/=result2.)': 
				self.read(' "/"Factorresult2>(.result1/=result2.)', True)
				result1/=result2
				
		result=result1
		return result

	def Factorintresult>(self):
		signo=1
		signo = -1
		if self.actual_token.type == ' "("Expression<result>")': 
			self.read(' "("Expression<result>")',True)
		result*=signo
		return result

	def Numberintresult>(self):
		self.read('number', True)
		result = int(self.last_token.value)
		return result

