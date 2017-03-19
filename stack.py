class Stack:
	def __init__(self, size):
		self.size = size
		self.top = -1
		self.data = []

	def is_full(self):
		return len(self.data) == self.size

	def is_empty(self):
		return self.top == -1

	def increment_top(self):
		self.top += 1

	def decrement_top(self):
		self.top -= 1

	def push(self, x):
		if self.is_full():
			print "Stack is full"
		else:
			self.increment_top()
			self.data.append(x)
			return self.data

	def pop(self):
		if self.is_empty():
			print "Stack is empty"
		else:
			self.decrement_top()
			return self.data.pop()
