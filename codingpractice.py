#!/usr/bin/env python3

# ONLINE PRACTICE PROBLEMS

#Check for pair in an array with a given sum:

def checkpair(l, sum):
	for i in range(len(l) - 1):
		if l[i] + l[i+1] == sum:
			return True
	return False


# print(checkpair([1,2,3,4,5,6], 9))
# print(checkpair([1,2,3,4,5,6], 30))

#Find whether an array is a subset of another array

def subsetArray(subl, l):
	for i in range(len(l) - len(subl) + 1):
		j = 0
		while l[i+j] == subl[j] and i + j < len(l):
			if j + 1 == len(subl):
				return True
			j+=1
	return False
# print(subsetArray([4,5,6], [1,2,3,4,5,6,7]))
# print(subsetArray([1,2,3], [1,2,3,4]))
# print(subsetArray([3,4], [1,2,3,4]))

# print(subsetArray([3,2], [1,2,3,4]))

# TODO
# Find the Kth smallest element in an array
#IDEAS: Technically, I could try to use a modified QuickSort, since if we 
# only want the kth smallest array, we do not need to sort the entire list.

# TODO
#Longest consecutive Sequence


#Remove duplicates from an unsorted array
def remdup(arr):
	seen = dict()

	#using a new array

	# ret = []
	# for i in range(len(arr)):
	# 	if arr[i] not in seen:
	# 		seen[arr[i]] = True
	# 		ret.append(arr[i])
	# return ret

	#altering the current array

	i = 0
	while i < len(arr):
		if arr[i] not in seen:
			seen[arr[i]] = True
			i += 1
		elif i + 1 == len(arr):
			arr = arr[:-1]
			return arr
		else:
			arr = arr[:i] + arr[i+1:]
	return arr

# print(remdup([1,1,1,2,3,4,4,5,6,6,6,7,7]))





#Palindrome Practice
# def pal(s):
# 	return s == reverse(s)
# def reverse(s):
# 	ret = ''
# 	for i in range(len(s)):
# 		ret += s[-i-1]
# 		i+=1
# 	return ret
# print(pal('hello'), pal('calac'))


def str_compress(s):
	curr = ''
	count = 0
	ret = ''
	for i in range(len(s)):
		print('Count before increase: ' + str(count))
		count+=1
		if curr == s[i]:
			print('i+1 =' + str(i+1))
			print(len(s))
			if i+1 > len(s):
				print('here!')
				ret += curr +str(count)
				print(ret)
				return
		else:
			ret += curr + str(count)
			curr = s[i]
			count = 0
	print('ret= ' + ret)

# str_compress('abbcccdddd')






#FizzBuzz
# for i in range(100):
# 	if (i%3) == 0:
# 		if (i %5) == 0:
# 			print('FizzBuzz')
# 		else:
# 			print('Fizz')
# 	else:
# 		if (i%5) == 0:
# 			print('Buzz')
# 		else:
# 			print(str(i))


#Practice
#Generate all the lowest-valued integer outputs that exhaustively test 
#all combinations of 4 conditionals.
#Conditionals: Contains a 7, is a multiple of 7. contains a 3,
#is a multiple of 3



# Generate all the lowest-valued valid integer inputs 
# that exhaustively test all combinations of 4 conditionals. 
# Conditionals: contains a 7, is a multiple of 7, contains a 3,
#  and is a multiple of 3.


# for i in range(1000):
# 	if '7' in str(i):
# 		print(i)
# 	elif '3' in str(i):
# 		print(i)
# 	elif i % 7 == 0:
# 		print(i)
# 	elif i % 3 == 0:
# 		print(i)

# Now, run the code but only output elements that have unique
# combinations of the above criteria, with a code to show which
# criteria they satisfy


#Helper functions

# def mult_7(x):
# 	return str(int((x%7 == 0)))
# def mult_3(x):
# 	return str(int((x%3 == 0)))

# def cont_7(x):
# 	return str(int('7' in str(x)))
# def cont_3(x):
# 	return str(int('3' in str(x)))

# seen = list()
# for i in range(1000):
# 	ival = mult_3(i)+mult_7(i)+cont_7(i)+cont_3(i)
# 	if len(seen) <= 16:
# 		if ival not in seen:
# 			seen.append(ival)
# 			print('Number: ' + str(i) + ' Value: ' + ival)





# CHAPTER 2: Linked Lists

#Linked List Implementation

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


# class LinkedList(object):
# 	def __init__(self, head=None):
# 	    self.head = head

# 	def insert(self, data):
# 	    new_node = Node(data)
# 	    new_node.set_next(self.head)
# 	    self.head = new_node

# 	def deleteNode(self, data):
# 		Node ret = self

# 		if ret.data == data:
# 			return self.next

# 		while ret.next is not None:
# 			if ret.next.data == data:
# 				ret.next = ret.next.next
# 				return self
# 			ret = ret.next

# 		return self


#2.1 Remove duplicates from a linked list

# def dup(llist):
# 	seen = dict()
# 	pointer = llist
# 	while llist.next is not None:
# 		if 
# 		dict[llist.data] = True


#CHapter 4 Stacks and Queues

#Stack implementation:

class Stack:
	#First in, first out
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return len(self.items) == 0
	def pop(self):
		return self.items.pop()
	def push(self, element):
		self.items.append(element)
	def peek(self):
		return self[-1]

class Queue:
	#Last in, first out
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.append(item)
	def dequeue(self):
		ret = self.items[0]
		self.items = self.items[1:]
	def peek(self):
		return self.items[0]
	def isEmpty():
		return len(self.items) == 0

#Use a single array to implement 3 stacks:
class ThreeStack:
	#Did not include what to do when there are actual lists inputed
	def __init__(self):
		# self.first = f
		# self.len1 = len(self.first)
		# self.second = s
		# self.len2 = len(self.second)
		# self.third = t
		# self.len3 = len(self.third)
		self.items = []
		self.len1 = 0
		self.len2 = 0
		self.len3 = 0

	def get_len(self, stacknum):
		if stacknum == 1:
			return self.len1
		elif stacknum == 2:
			return self.len2
		return self.len3		

	def decrease_len(self, stacknum):
		if stacknum == 1:
			self.len1 -= 1
		elif stacknum == 2:
			self.len2 -= 1
		self.len3 -= 1

	def increase_len(self, stacknum):
		if stacknum == 1:
			self.len1 += 1
		elif stacknum == 2:
			self.len2 += 1
		self.len3 += 1		


	def isOneEmpty(self, n):
		if n == 1:
			return self.len1 == 0
		elif n == 2:
			return self.len2 == 0
		elif n == 3:
			return self.len3 == 0
		else:
			print('Invalid stack number')

	def isEmpty(self):
		return self.isOneEmpty(1) and self.isOneEmpty(2) and self.isOneEmpty(3)

	def pop(self, stacknum):
		if isOneEmpty(stacknum):
			print('This stack is empty')		
		ret = self.items[(self.get_len(stacknum)-1)*3 + (stacknum -1)]
		self.items[(self.get_len(stacknum)-1)*3 + (stacknum -1)] = 0

	def push(self, stacknum, element):
		return False

	def peek(self, stacknum):
		return self.items[(self.get_len(stacknum)-1)*3 + (stacknum -1)]



#3.2 add a min function that takes O(1) time
class MinStack:
	#First in, first out
	def __init__(self, elements =[]):
		self.items = elements
		self.minimum = float('inf')
	def isEmpty(self):
		return len(self.items) == 0
	def pop(self):
		return self.pop()
	def push(self, element):
		self.items.append(element)
		if element < self.minimum:
			self.minimum = element
	def peek(self):
		return self[-1]
	def min(self):
		return self.minimum


#3.3 Stack of Plates
#Start a new stack when the previous one exceeds some threshold
class SetOfStacks:
	def __init__(self, threshold):
		self.threshold = threshold
		self.stacks = [[]]
		self.lastStackIndex = 0
	def isEmpty(self):
		return len(self.stacks[0]) == 0
	def pop(self):
		self.stacks[self.lastStackIndex].pop()
		if len(self.stacks[self.lastStackIndex]) == 0 and len(self.stacks) != 1:
			return self.Stacks.pop()
	def push(self, element):
		if len(self.stacks[self.lastStackIndex]) == self.threshold:
			self.lastStackIndex += 1
			self.stacks.append([element])
		else:
			self.stacks[self.lastStackIndex].append(element)
	def peek(self):
		return self.stacks[self.lastStackIndex][-1]
	#Implementing without rollover
	def popAt(self, index):
		if index > self.lastStackIndex:
			print('Invalid stack index')
			return
		else:
			return self.stacks[index].pop()

# x = SetOfStacks(5)
# x.push(1)
# x.push(1)
# x.push(1)
# x.push(1)
# x.push(1)
# x.push(1)
# x.push(1)
# x.push(1)
# x.push(1)
# x.push(1)
# x.push(1)
# x.push(1)
# print(x.stacks)
# x.popAt(3)
# print(x.popAt(1))
# print(x.stacks)



#3.4 Queue via Stacks
class MyQueue:
	#Last in, first out
	def __init__(self):
		self.addStack = Stack()
		self.remStack = Stack()
	def enqueue(self, item):
		self.addStack.push(item)
	def dequeue(self):
		while not self.addStack.isEmpty() :
			self.remStack.push(self.addStack.pop())
		ret = self.remStack.pop()
		while not self.remStack.isEmpty():
			self.addStack.push(self.remStack.pop())
		return ret
	def peek(self):
		while not self.addStack.isEmpty():
			self.remStack.push(self.addStack.pop())
		ret = self.remStack.peek()
		while not self.remStack.isEmpty():
			self.addStack.push(self.remStack.pop())
		return ret
	def isEmpty(self):
		return self.addStack.isEmpty()

# thingy = MyQueue()

# thingy.enqueue(5)
# thingy.enqueue(4)
# thingy.enqueue(3)
# thingy.enqueue(2)
# thingy.enqueue(1)

# def sortStack(stack1):
# 	stack2 = Stack()
# 	currmin = -float('inf')
# 	while not stack1.isEmpty():





#CHAPTER 4 TREES AND GRAPHS

class Node:
	def __init__(self, name = '', children =[]):
		self.name = name
		self.children = children

#4.1 Given a directed graph, make an algorithm to find whether there
#is a route between two nodes
def isRoute(start, end):
	tovisit = Stack()
	tovisit.push(start)
	visited = []

	print('=======================')
	while not tovisit.isEmpty():

		branch = tovisit.pop()

		if branch in visited:
			continue
		if branch == end:
			return True
		if branch not in visited:
			visited.append(branch)
			for i in range(len(branch.children)):
				tovisit.push(branch.children[i])
	return False

# f = Node('f')
# e = Node('e', [f])
# b = Node('b', [e])
# x = Node('x')
# c = Node('c', [x])
# a = Node('a', [x,b,c])
# g = Node('g', [a])

# print(isRoute(f,f))
# print('Should be true')
# print(isRoute(a, g))
# print('Should be false')
# print(isRoute(g,f))
# print('Should be true')


class BinaryTreeNode:
	def __init__(self, num =None, left =None, right =None):
		self.num = num
		self.left = left
		self.right = right



# 4.2: 
def MinimalTree(lis):
	ret = BinaryTreeNode()
	length = len(lis)
	if length == 1:
		ret.num = lis[0]
		return ret
	elif length == 2:
		ret.num = lis[1]
		ret.left = lis[0]
		return ret
	else:
		ret.num = lis[int(length/2)]
		ret.left = MinimalTree(lis[:int(length/2)])
		ret.right = MinimalTree(lis[int(length/2) + 1:])
		return ret





# mytree = MinimalTree([1])
mytree = MinimalTree([1,2,3,4,5,6,7])
print(mytree.num)
print(mytree.left.num, mytree.right.num)
print(mytree.left.left.num, mytree.left.right.num, mytree.right.left.num, mytree.right.right.num)





    			
    			