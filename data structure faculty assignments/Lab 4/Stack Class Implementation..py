
def analyseInput():
    inputString = input()
    cleanedInput = inputString[1:len(inputString)-1]
    if (len(cleanedInput) == 0):
        return []
    cleanedInput = cleanedInput.split(', ')
    arr = [0]*len(cleanedInput)
    for i in range(len(cleanedInput)):
        arr[i] = int(cleanedInput[i])
    return arr

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

    def __str__(self):
        temp_node = self.head
        result = '['
        while temp_node is not None:
            result += (str(temp_node.value))
            if temp_node.next is not None:
                result += ', '
            temp_node = temp_node.next
        result += ']'
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

class Stack:
    
    def __init__(self, values=[]):
        self.stackList = LinkedList(values)

    def __str__(self):
        return self.stackList.__str__()

    def push(self, value):
        self.stackList.prepend(value)

    def pop(self):
        if self.isEmpty():
            raise
        return self.stackList.pop_first()
    
    def peek(self):
        if self.isEmpty():
            raise
        return self.stackList.head.value
    
    def isEmpty(self):
        if self.stackList.head == None:
            return True
        else:
            return False
    
    def size(self):
        return self.stackList.length
    
    def selectOperation(self):
        try:
            operation = input()
            if operation == "push":
                value = int(input())
                self.push(value)
                print(self)
            elif operation == "pop":
                self.pop()
                print(self)
            elif operation == "peek":
                print(self.peek())
            elif operation == "isEmpty":
                print(self.isEmpty())
            elif operation == "size":
                print(self.size())
            else:
                print("Error")
        except:
            print("Error")
            return



testStack = Stack(analyseInput())
testStack.selectOperation()