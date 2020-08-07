#栈
class Stack(object):
	"""docstring for SStack"""
	def __init__(self,):
		self.values=[]
	def push(self,value):
		self.values.append(value)
	def pop(self):
		return self.values.pop()
	def is_empty(self):
		return self.size()==0
	def size(self):
		return len(self.values)
	def peak(self):
		return self.values[self.size()-1]
		