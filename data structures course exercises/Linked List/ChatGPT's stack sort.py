
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self, initial_nodes_values=[]):
        if len(initial_nodes_values) == 0:
            self.head = None
            self.tail = None
        elif len(initial_nodes_values) == 1:
            self.head = self.tail = Node(initial_nodes_values[0])
        else:
            self.head = Node(initial_nodes_values[0])
            temp_node = self.head
            for i in range(1, len(initial_nodes_values) - 1):
                new_node = Node(initial_nodes_values[i])
                temp_node.next = new_node
                temp_node = new_node
            self.tail = Node(initial_nodes_values[len(initial_nodes_values) - 1])
            temp_node.next = self.tail
        self.length = len(initial_nodes_values)
    
    #The method called when the list is first created
    #This methods supports giving an initial list of values to create the linked list 
    #if its not given or given an empty array it will create an empty linked list

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    #This method inserts a node in the first index with the given value

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value
    
    #This method removes the first node in the linked list and returns its value

class Stack:
    
    def __init__(self, values=[]):
        self.stackList = LinkedList(values)

    def __str__(self):
        return self.stackList.__str__()

    def push(self, value):
        self.stackList.prepend(value)

    def pop(self):
        return self.stackList.pop_first()
    
    def peak(self):
        return self.stackList.head.value
    
    def isEmpty(self):
        if self.stackList.head == None:
            return True
        else:
            return False
        
    def copy(self):
        copyStack = Stack()
        temp = Stack()
        while(not self.isEmpty()):
            temp.push(self.pop())
        while(not temp.isEmpty()):
            top = temp.pop()
            self.push(top)
            copyStack.push(top)
        return copyStack
    
    def sortStackDescending(self):
        if self.isEmpty():
            return Stack()

        sorted_stack = Stack()
        while not self.isEmpty():
            temp = self.pop()

            # Pop elements from sorted_stack greater than temp and push them back to self
            while not sorted_stack.isEmpty() and sorted_stack.peak() > temp:
                self.push(sorted_stack.pop())

            # Push temp to sorted_stack
            sorted_stack.push(temp)

        return sorted_stack


testStack = Stack([6,5,5,1,8,7,2,4])
print(testStack)
print(testStack.sortStackDescending())