class stack:
	
	def __init__(self, size): 
		self.lst = [None] * size
		self.size = size
		self.top = -1

	def isFull(self):
		return self.top == self.size - 1
	
	def isEmpty(self):
		return self.lst == []

	def push(self, item):
		if self.isFull():
			print("Erro: StackOverFLow!!!")
		else:
			self.top += 1
			self.lst[self.top] = item

	
	def pop(self):
		if self.isEmpty():
			print("StackUnderFlow!!!")
			self.top = -1
			self.lst = [None] * self.size
			
		else:
			topo = self.lst[self.top]
			self.lst = self.lst[:self.top]
			self.top -= 1
			return topo