class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self,item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def is_empty(self):
		if self.items == []:
			return True
		return False

if __name__ == "__main__":
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(0)

	while not q.is_empty():
		item = q.dequeue()
		print(item)