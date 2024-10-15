class FixedSizeStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [0] * capacity  
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.top]

class FixedSizeQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0] * capacity  
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def front_value(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

class FixedSizeSinglyLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = [{'value': 0, 'next': -1} for _ in range(capacity)]  
        self.head = -1  
        self.size = 0
        self.next_free = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def add(self, value):
        if self.is_full():
            raise OverflowError("List is full")
        new_index = self.next_free
        self.nodes[new_index]['value'] = value
        self.nodes[new_index]['next'] = self.head
        self.head = new_index
        self.size += 1
        self.next_free += 1

    def remove(self):
        if self.is_empty():
            raise IndexError("List is empty")
        value = self.nodes[self.head]['value']
        self.head = self.nodes[self.head]['next']
        self.size -= 1
        return value

    def traverse(self):
        result = []
        current = self.head
        while current != -1:
            result.append(self.nodes[current]['value'])
            current = self.nodes[current]['next']
        return result


stack = FixedSizeStack(5)
queue = FixedSizeQueue(5)
linked_list = FixedSizeSinglyLinkedList(5)

# Stack operations
stack.push(10)
stack.push(20)
stack.push(30)

# Queue operations
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Linked List operations
linked_list.add(10)
linked_list.add(20)
linked_list.add(30)

stack_pop = stack.pop()
queue_dequeue = queue.dequeue()
list_traversal = linked_list.traverse()

print(f"Stack pop result: {stack_pop}")
print(f"Queue dequeue result: {queue_dequeue}")
print(f"Singly Linked List traversal: {list_traversal}")
