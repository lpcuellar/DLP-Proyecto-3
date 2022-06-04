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
		value = 0
		value = self.Expression(value)
		print(value)

	def Expression(self,result1):
		result1, result2 = 0, 0
		result1 = self.Term(result1)
		while self.actual_token.value == " "-"Term<result2>(.result1-=result2.)"or self.actual_token.value == " "-"Term<result2>(.result1-=result2.)":
			if self.actual_token.type == ' "-"Term<result2>(.result1-=result2.)': 
				self.read(' "-"Term<result2>(.result1-=result2.)',True)
				result2 = self.Term(result2)
				result1+=result2
			if self.actual_token.type == ' "-"Term<result2>(.result1-=result2.)': 
				self.read(' "-"Term<result2>(.result1-=result2.)', True)
				result2 = self.Term(result2)
				result1-=result2
				
		return result1

	def Term(self,result):
		result1, result2 =  0,0
		result1 = self.Factor(result1)
		while self.actual_token.value == " "/"Factor<result2>(.result1/=result2.)"or self.actual_token.value == " "/"Factor<result2>(.result1/=result2.)":
			if self.actual_token.type == ' "/"Factor<result2>(.result1/=result2.)': 
				self.read(' "/"Factor<result2>(.result1/=result2.)',True)
				result2 = self.Factor(result2)
				result1*=result2
			if self.actual_token.type == ' "/"Factor<result2>(.result1/=result2.)': 
				self.read(' "/"Factor<result2>(.result1/=result2.)', True)
				result2 = self.Factor(result2)
				result1/=result2
				
		result=result1
		return result

	def Factor(self,result):
		signo=1
		signo = -1
	if self.actual_token.type == 'number': 
		self.read('number', True)
		result = self.Number(result)
	if self.actual_token.type == 'decnumber': 
		self.read('decnumber', True)
		result = self.Number(result)
	if self.actual_token.type ==  ' "(" Expression<result> ")': 
		self.read(' "(" Expression<result> ")', True)
		result = self.Expression(result)
		self.read(')')
	result*=signo
	return result

	def Number(self,result):
		if self.actual_token.type == 'number': 
			self.read('number',True)
		if self.actual_token.type == 'decnumber': 
			self.read('decnumber', True)
			
		result = int(self.last_token.value)
		return result

#file to test

import collections
EPSILON = 'ε'
class Automata:
	def __init__(self, exp):
		self.id = exp 
		self.states = []

class Token:
	def __init__(self, type, value):
		self.type = type 
		self.value = value

class State: 
	def __init__(self,num):
		self.id = num
		self.transitions = []
		self.accept = False 

class Transition: 
	def __init__(self,sym,to):
		self.symbol = sym
		self.to = to

def is_in_language(automata, expresion):
  if expresion == ' ' or expresion == '':
      expresion = EPSILON
  actual = [0]
  actual = cerradura(automata, actual)
  i = 0
  while True:
      temp = []
      for num in actual:
          for transition in automata.states[num].transitions:
              if transition.symbol == expresion[i] and transition.to not in temp:
                  temp.append(transition.to)
      i += 1
      temp = cerradura(automata, temp)
      if not temp and expresion == EPSILON:
          break
      actual = temp.copy()
      if i > len(expresion)-1:
          break
  for id in actual:
      if automata.states[id].accept:
          return True
  return False

def cerradura(automata, actual):
  for num in actual:
      for transition in automata.states[num].transitions:
          if transition.symbol == EPSILON and transition.to not in actual:
              actual.append(transition.to)
  return actual

def read_word(file, actual):
  temp_word = ''
  while actual < len(file):
      if(file[actual] == ' ' or file[actual] == '\n') and (len(temp_word)>0):
          break
      elif file[actual] == ' ' or file[actual] == '\n':
          actual += 1
      else:
          temp_word += file[actual]
          actual += 1
  return temp_word, actual

def word_break(file, automata0, actual = 0):
  temp = ''
  validos = []
  while actual < len(file):
      temp += file[actual]
      if is_in_language(automata0, temp):
          validos.append(temp)
      elif len(temp) == 1  and is_in_language(automata0, str(ord(temp))):
          validos.append(temp)
      actual += 1
  if validos:
      return max(validos, key = len)
  return False
def main():
  automatas = []
  automata0 = Automata("completo")
  temp_node= State(0)
  temp_transition = Transition('0', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('2', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('3', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('4', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('5', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('6', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('7', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('8', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('9', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('\n', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('\r', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('\t', 2)
  temp_node.transitions.append(temp_transition)
  automata0.states.append(temp_node)
  temp_node= State(1)
  temp_node.accept = True
  temp_transition = Transition('0', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('2', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('3', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('4', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('5', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('6', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('7', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('8', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('9', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('.', 3)
  temp_node.transitions.append(temp_transition)
  automata0.states.append(temp_node)
  temp_node= State(2)
  temp_node.accept = True
  temp_transition = Transition('\n', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('\r', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('\t', 2)
  temp_node.transitions.append(temp_transition)
  automata0.states.append(temp_node)
  temp_node= State(3)
  temp_transition = Transition('0', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('2', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('3', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('4', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('5', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('6', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('7', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('8', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('9', 4)
  temp_node.transitions.append(temp_transition)
  automata0.states.append(temp_node)
  temp_node= State(4)
  temp_node.accept = True
  temp_transition = Transition('0', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('2', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('3', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('4', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('5', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('6', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('7', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('8', 4)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('9', 4)
  temp_node.transitions.append(temp_transition)
  automata0.states.append(temp_node)
  automatas.append(automata0)

  automata1 = Automata("number")
  temp_node= State(0)
  temp_transition = Transition('0', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('2', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('3', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('4', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('5', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('6', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('7', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('8', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('9', 1)
  temp_node.transitions.append(temp_transition)
  automata1.states.append(temp_node)
  temp_node= State(1)
  temp_node.accept = True
  temp_transition = Transition('0', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('2', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('3', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('4', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('5', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('6', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('7', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('8', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('9', 1)
  temp_node.transitions.append(temp_transition)
  automata1.states.append(temp_node)
  automatas.append(automata1)

  automata2 = Automata("decnumber")
  temp_node= State(0)
  temp_transition = Transition('0', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('2', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('3', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('4', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('5', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('6', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('7', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('8', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('9', 1)
  temp_node.transitions.append(temp_transition)
  automata2.states.append(temp_node)
  temp_node= State(1)
  temp_transition = Transition('0', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('2', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('3', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('4', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('5', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('6', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('7', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('8', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('9', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('.', 2)
  temp_node.transitions.append(temp_transition)
  automata2.states.append(temp_node)
  temp_node= State(2)
  temp_transition = Transition('0', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('2', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('3', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('4', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('5', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('6', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('7', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('8', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('9', 3)
  temp_node.transitions.append(temp_transition)
  automata2.states.append(temp_node)
  temp_node= State(3)
  temp_node.accept = True
  temp_transition = Transition('0', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('2', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('3', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('4', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('5', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('6', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('7', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('8', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('9', 3)
  temp_node.transitions.append(temp_transition)
  automata2.states.append(temp_node)
  automatas.append(automata2)

  automata3 = Automata("white")
  temp_node= State(0)
  temp_transition = Transition('\n', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('\r', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('\t', 1)
  temp_node.transitions.append(temp_transition)
  automata3.states.append(temp_node)
  temp_node= State(1)
  temp_node.accept = True
  temp_transition = Transition('\n', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('\r', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('\t', 1)
  temp_node.transitions.append(temp_transition)
  automata3.states.append(temp_node)
  automatas.append(automata3)

  print('archivo a revisar?')
  archivo = input()
  prueba = open('../test/'+archivo)
  data = prueba.read()
  prueba.close()
  i = 0
  tokens = []
  last = 0
  while i < len(data):
      valid = word_break(data, automata0, i)
      if valid:
          if last != 0 and (i - last > 0):
              while last < i:
                  print(data[last], end='')
                  last += 1
              print(': False')
          last += len(valid)
          aut = 1
          new_token = Token('ANY', valid)
          while aut<len(automatas):
              if (is_in_language(automatas[aut], valid)):
                  new_token = Token(automatas[aut].id, valid)
                  break
              aut += 1
          tokens.append(new_token)
          i += len(valid)
      else:
          i+=1
  parser = Parser(tokens)
  parser.Expr()
if __name__ == "__main__":
   main()