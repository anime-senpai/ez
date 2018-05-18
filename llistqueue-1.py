#   Data Structures and Algorithms Using Python
#
#   Rance D. Necaise
#   Wiley, 2011
#
#   8.2   Implementing the Queue
#   8.2.3 Using a Linked List
#
#   vk, 2014
#   ab, 2018 

# Implementation of the Queue ADT using a linked list.
# Contiene método excahnge Tarea 3 Colas Horario 0583 (2018-1)

class Queue:
	# Creates an empty queue.
	def __init__(self):
		self._qhead = None
		self._qtail = None
		self._count = 0

	# Returns True if the queue is empty or False otherwise.
	def isEmpty(self):
		return self._qhead is None

	# Returns the number of items in the queue.
	def __len__(self):
		return self._count

	# Adds the given item to the queue.
	def enqueue(self, pid, burst, arrival=0,turnaround=0, priority=0):
		node = _QueueNode(pid, burst, arrival, turnaround, priority)
		if self.isEmpty():
			self._qhead = node
		else:
			self._qtail.next = node

		self._qtail = node
		self._count += 1

	# Removes and returns the first item in the queue.
	def dequeue(self):
		assert not self.isEmpty(), "Cannot dequeue from an empty queue."
		node = self._qhead
		if self._qhead is self._qtail:
			self._qtail = None
		self._qhead = self._qhead.next
		self._count -= 1
		return node.pid


	def sortShortest(self):
		q = Queue()
		
		#print("entro 1")
		while True:
			#print("entro 2")
			ptr = self._qhead
			ptrAnt = None
			minAnt = None
			minNode = self._qhead
			while True:
				if ptr is None:
					break
				else:
					if(ptr.burst < minNode.burst):
						minNode = ptr
						minAnt = ptrAnt
					ptrAnt = ptr
					ptr = ptr.next
			#print("salio 2")
			if(minAnt is None):
				self._qhead = minNode.next
			else:
				minAnt.next = minNode.next
			minNode.next = None
			self._count -= 1
			q.enqueue(minNode.pid, minNode.burst, minNode.arrival, minNode.turnaround)	
			if(self.isEmpty()):
				break
		#print("salio 1")
		#print("entro 3")
		while True:
			if(q.isEmpty()):
				break
			else:
				ptr = q._qhead
				self.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
				q.dequeue()
		#print("salio 3")

	def schedulingSJFNO(self):
		print("scheduling Shortest Job First no Preemptive")
		print("")
		q1 = Queue()
		ptr = self._qhead
		while(ptr is not None):
			q1.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
			ptr = ptr.next
		q = Queue()
		t = 0
		q1.sortShortest()
		ptr = q1._qhead
		while ptr is not None:
			ptr1 = ptr
			while(t<ptr.arrival):
				q1.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
				q1.dequeue()
				ptr = q1._qhead
				if (ptr1.pid == ptr.pid):
					t+=1
			ptr = q1._qhead
			t += ptr.burst
			ptr.turnaround = t - ptr.arrival
			q.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
			q1.dequeue()
			if(not q1.isEmpty()):
				q1.sortShortest()
			ptr = q1._qhead
		q.printStatistics()
		print("")


	def schedulingSJF(self):
		print("scheduling Shortest Job First Preemptive")
		print("")
		q1 = Queue()
		ptr = self._qhead
		while(ptr is not None):
			q1.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
			ptr = ptr.next
		q = Queue()
		t = 0
		q1.sortShortest()
		ptr = q1._qhead
		while ptr is not None:
			ptr1 = ptr
			while(t<ptr.arrival):
				q1.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
				q1.dequeue()
				ptr = q1._qhead
				if (ptr1.pid == ptr.pid):
					t+=1
			ptr = q1._qhead
			t += 1
			ptr.burst -=1
			if (ptr.burst == 0):
				ptr.turnaround = t - ptr.arrival
				q.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
				q1.dequeue()
			if(not q1.isEmpty()):
				q1.sortShortest()
			ptr = q1._qhead
		q.printStatistics()
		print("")

	def sortPriority(self):
		q = Queue()
		
		#print("entro 1")
		while True:
			#print("entro 2")
			ptr = self._qhead
			ptrAnt = None
			minAnt = None
			minNode = self._qhead
			while True:
				if ptr is None:
					break
				else:
					if(ptr.priority > minNode.priority):
						minNode = ptr
						minAnt = ptrAnt
					ptrAnt = ptr
					ptr = ptr.next
			#print("salio 2")
			if(minAnt is None):
				self._qhead = minNode.next
			else:
				minAnt.next = minNode.next
			minNode.next = None
			self._count -= 1
			q.enqueue(minNode.pid, minNode.burst, minNode.arrival, minNode.turnaround, minNode.priority)	
			if(self.isEmpty()):
				break
		#print("salio 1")
		#print("entro 3")
		while True:
			if(q.isEmpty()):
				break
			else:
				ptr = q._qhead
				self.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround, ptr.priority)
				q.dequeue()
		#print("salio 3")

	def schedulingPriority(self):
		print("scheduling Priority")
		print("")
		q1 = Queue()
		ptr = self._qhead
		while(ptr is not None):
			q1.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround, ptr.priority)
			ptr = ptr.next
		q = Queue()
		t = 0
		q1.sortPriority()
		ptr = q1._qhead
		while ptr is not None:
			ptr1 = ptr
			while(t<ptr.arrival):
				q1.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround, ptr.priority)
				q1.dequeue()
				ptr = q1._qhead
				if (ptr1.pid == ptr.pid):
					t+=1	
			ptr = q1._qhead
			t += 1
			ptr.burst -= 1
			if (ptr.burst == 0):
				ptr.turnaround = t - ptr.arrival
				q.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround, ptr.priority)
				q1.dequeue()

			if(not q1.isEmpty()):
				q1.sortPriority()

			ptr = q1._qhead
		q.printStatistics()
		print("")

			
	def printQueue(self):        
		t = self._qhead
		while t is not None:
			print(t.pid,end=",")
			print(t.priority,end=" ")
			t = t.next
		print("")
	
	def printStatistics(self):
		t = self._qhead
		tp = 0
		while t is not None:
			tp += t.turnaround
			print("Pid del proceso:",t.pid,"Tiempo de retorno:",t.turnaround)
			t = t.next        
		print("Tiempo promedio de retorno:",tp/self._count)
	   
	
	def sortArrival(self):
		q = Queue()

		while True:
			ptr = self._qhead
			ptrAnt = None
			minAnt = None
			minNode = self._qhead
			while True:
				if ptr is None:
					break
				else:
					if(ptr.arrival < minNode.arrival):
						minNode = ptr
						minAnt = ptrAnt
					ptrAnt = ptr
					ptr = ptr.next
			if(minAnt is None):
				self._qhead = minNode.next
			else:
				minAnt.next = minNode.next
			minNode.next = None
			self._count -= 1
			q.enqueue(minNode.pid, minNode.burst, minNode.arrival, minNode.turnaround)	
			if(self.isEmpty()):
				break
		while True:
			if(q.isEmpty()):
				break
			else:
				ptr = q._qhead
				self.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
				q.dequeue()


	def schedulingRR(self, quantum):
		print("scheduling Round Robin")
		print("")
		q1 = Queue()
		ptr = self._qhead
		while(ptr is not None):
			q1.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
			ptr = ptr.next
		q = Queue()
		t = 0
		q1.sortArrival()
		ptr = q1._qhead
		while True:
			if ptr is None:
				break
			if(t>=ptr.arrival):            
				if ptr.burst <= quantum:
					t += ptr.burst
					ptr.turnaround = t - ptr.arrival
					ptr.burst = 0
					q.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
					q1.dequeue()
				else:
					t += quantum
					ptr.burst -= quantum                    
					q1.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
					q1.dequeue()
				ptr = ptr.next
			else:
				ptr1 = ptr
				while True:
					
					if(t<ptr.arrival):
						q1.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
						ptr = ptr.next
						q1.dequeue()
						if(ptr1.pid == ptr.pid):
							t+=1
							break
					else:
						break
				ptr = q1._qhead    
		q.printStatistics()   
		print("") 

	def schedulingFCFS(self):
		print("scheduling First Come First Serve")
		print("")
		q1 = Queue()
		ptr = self._qhead
		while(ptr is not None):
			q1.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
			ptr = ptr.next
		q = Queue()
		t = 0
		q1.sortArrival()
		ptr = q1._qhead

		while ptr is not None:
			if(t>= ptr.arrival):
				t += ptr.burst
				ptr.turnaround = t-ptr.arrival 
				ptr.burst = 0
				q.enqueue(ptr.pid, ptr.burst, ptr.arrival, ptr.turnaround)
				q1.dequeue()
				ptr = ptr.next
			else:
				t+=1
			
		q.printStatistics()
		print("")

	def __iter__(self):
		return QueueIterator(self._qhead) 


class QueueIterator:
	def __init__(self, head):
		self.curNode = head

	def __iter__(self):
		return self
	
	def __next__(self):
		if self.curNode is None:
			raise StopIteration
		else:
			item = self.curNode.item
			self.curNode = self.curNode.next
			return item
		
# The private storage class for creating the linked list nodes.
class _QueueNode(object):
	def __init__(self, pid, burst = 0, arrival=0, turnaround=0, priority=0):
		self.pid = pid
		self.burst = burst
		self.arrival = arrival
		self.turnaround = turnaround
		self.priority = priority
		self.next = None


def main():
	q = Queue()

	q.enqueue(1,3,4,0,5)
	q.enqueue(2,6,0,0,4)
	q.enqueue(3,4,6,0,1)
	q.enqueue(4,5,8,0,2)
	q.enqueue(5,2,2,0,5)

	q.schedulingFCFS()
	q.schedulingRR(4) 
	q.schedulingSJF()
	
	q.schedulingSJFNO()
	q.schedulingPriority()
	
	"""
	assert q.isEmpty(), "---> isEmpty error"
	try:
		q.dequeue()
	except AssertionError:
		pass

	q.enqueue(1)
	assert not q.isEmpty(), "---> isEmpty error"
	q.enqueue(2)
	q.enqueue(2)
	assert len(q) == 3, "---> __len__ error"
	q.enqueue(3)
	assert q.dequeue() == 1, "---> dequeue error"

	print('All tests are ok')
	"""
if __name__ == "__main__":
	main()
