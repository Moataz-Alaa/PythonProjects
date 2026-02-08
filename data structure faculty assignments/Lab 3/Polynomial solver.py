
def analyseInput():
    inputString = input()
    cleanedInput = inputString[1:len(inputString)-1]
    if (len(cleanedInput) == 0):
        raise
    cleanedInput = cleanedInput.split(',')     # Notice that the separator is ',' not ', ' like in the previous problems
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
    
    #The method called when the list is first created
    #This methods supports giving an initial list of values to create the linked list 
    #if its not given or given an empty array it will create an empty linked list

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

    #The method called when the list is being printed

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    #This method checks if the linked list is empty, returns true if empty and false otherwise

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    #This method inserts a node in the last index with the given value

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

    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length - 1 or index < 0:
            raise
        elif index == 0:
            self.prepend(value)
            return
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
    #This method inserts a node in the given index with the given value
    #This method returns 'Error' and does nothing if the index is out of bound 
    #This method calls the special cases methods in case of special case 

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    #This method passes through each node and prints its value

    def copy(self):
        list_copy = []
        current = self.head
        while current is not None:
            list_copy.append(current.value)
            current = current.next
        return LinkedList(list_copy)

    #This method returns a deep copy of the linked list

    def sublist(self, fromIndex, toIndex):
        if fromIndex > self.length - 1 or fromIndex < 0:
            raise
        if toIndex > self.length - 1 or toIndex < 0:
            raise
        if fromIndex > toIndex:
            raise
        sublist = LinkedList()
        current = self.get(fromIndex)
        sublist.head = current
        for _ in range(toIndex - fromIndex):
            current = current.next
        sublist.tail = current
        sublist.tail.next = None
        return sublist

    #This method returns a sublist of the linked list starting from fromIndex to toIndex inclusively
    #This method returns 'Error' and does nothing if the fromIndex or the toIndex are out of bound
    #or if the fromIndex is greater than the toIndex

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False
    
    #This method passes through each node 
    #and searches for the node with target value 
    #returns true if found, false if not found

    def searchIndex(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return None
    
    #This method passes through each node 
    #and searches for the node with target value
    #returns the node's index if found and returns none if not found

    def get(self, index):
        if index > (self.length - 1) or index < 0:
            raise
        elif index == 0:
            return self.head
        elif index == (self.length - 1):
            return self.tail
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
    
    #This method returns the node in the given index
    #This method returns an error if the index is out of bound 
    #This method returns the special nodes dircetly (head or tail) in case of edge cases

    def getValue(self, index):
        if index > (self.length - 1) or index < 0:
            raise
        elif index == 0:
            return self.head.value
        elif index == (self.length - 1):
            return self.tail.value
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.value
    
    #Same as the get() method but returns the value of the node instead of the node itself

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    #This method sets the value of the node in the given index to the given value

    def getMiddle(self):
        mid_index = self.length // 2
        return self.get(mid_index)
    
    #This method returns the middle node of the linked list
    #If the list has an even number of nodes, it returns the second of the two middle nodes

    def popFirst(self):
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

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped_node.value

    #This method removes the last node in the linked list and returns its value

    def remove(self, index):
        if index > (self.length - 1) or index < 0:
            raise
        elif index == 0:
            self.popFirst()
            return self
        elif index == (self.length - 1):
            self.pop()
            return self
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return self
        
    #This method removes the node in the given index and returns the linked list
    #This method returns error if the index is out of bound
    #This method calls the special cases methods in case of special case

    def removeValue(self, target):
        while self.searchIndex(target) is not None:
            self.remove(self.searchIndex(target))
        return self
    
    #This method deletes all ocurences of the given target value from the linked list and returns the linked list
    
    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0

    #This method deletes the linked list

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        temp = self.head
        self.head = self.tail
        self.tail = temp
        return self

    #This method reverses the linked list in place and returns it

    def removeDuplicates(self):
        unique_arr = []
        current_node = self.head
        for _ in range(self.length):
            found = 0
            for j in range(len(unique_arr)):
                if current_node.value == unique_arr[j]:
                    found = 1
                    break
            if not found:
                unique_arr.append(current_node.value)
            current_node = current_node.next
        return LinkedList(unique_arr)
    
    #This methods returns a new linked list without duplicates from another linked list

    def selectOperation(self):
        try:
            operation = input()
            if operation == "add":
                value = int(input())
                self.append(value)
                print(self)
            elif operation == "addToIndex":
                index = int(input())
                value = int(input())
                self.insert(index,value)
                print(self)
            elif operation == "get":
                index = int(input())
                print(self.getValue(index))
            elif operation == "set":
                index = int(input())
                value = int(input())
                self.set(index,value)
                print(self)
            elif operation == "clear":
                self.delete()
                print(self)
            elif operation == "isEmpty":
                print(self.isEmpty())
            elif operation == "remove":
                index = int(input())
                print(self.remove(index))
            elif operation == "size":
                print(self.length)
            elif operation == "sublist":
                fromIndex = int(input())
                toIndex = int(input())
                print(self.sublist(fromIndex,toIndex))
            elif operation == "contains":
                target = int(input())
                print(self.search(target))
            else:
                print("Error")
        except:
            print("Error")
            return


class PolySolver:

    def __init__(self):
        self.A = LinkedList()
        self.B = LinkedList()
        self.C = LinkedList()
        self.R = LinkedList()

    def set(self, equ, arr):
        if equ == "A":
            self.A = LinkedList(arr)
        elif equ == "B":
            self.B = LinkedList(arr)
        elif equ == "C":
            self.C = LinkedList(arr)
        else:
            raise

    def print(self, equ):
        temp_node = equ.head
        exp = equ.length - 1
        result = ""

        if temp_node == None:
            raise

        while temp_node.value == 0 and temp_node != None and exp != 0:
            temp_node = temp_node.next
            exp = exp - 1

        if exp == 0:
            result = result + str(temp_node.value)
            temp_node = temp_node.next
            exp = exp - 1
        elif exp == 1 and temp_node.value == 1:
            result = result + "x"
            temp_node = temp_node.next
            exp = exp - 1
        elif exp == 1 and temp_node.value != 1:
            result = result + str(temp_node.value) + "x"
            temp_node = temp_node.next
            exp = exp - 1
        elif temp_node.value == 1:
            result = result + "x^" + str(exp)
            temp_node = temp_node.next
            exp = exp - 1
        else:
            result = result + str(temp_node.value) + "x^" + str(exp)
            temp_node = temp_node.next
            exp = exp - 1


        while temp_node != None and exp >= 0:
            if exp == 0:
                if temp_node.value > 0:
                    result = result + "+" + str(temp_node.value)
                    temp_node = temp_node.next
                    exp = exp - 1
                elif temp_node.value < 0:
                    result = result + str(temp_node.value)
                    temp_node = temp_node.next
                    exp = exp - 1
                else:
                    temp_node = temp_node.next
                    exp = exp - 1
            elif exp == 1:
                if temp_node.value > 1:
                    result = result + "+" + str(temp_node.value) + "x"
                    temp_node = temp_node.next
                    exp = exp - 1
                elif temp_node.value < 0:
                    result = result + str(temp_node.value) + "x"
                    temp_node = temp_node.next
                    exp = exp - 1
                elif temp_node.value == 1:
                    result = result + "+" + "x"
                    temp_node = temp_node.next
                    exp = exp - 1
                else:
                    temp_node = temp_node.next
                    exp = exp - 1
            else:
                if temp_node.value > 1:
                    result = result + "+" + str(temp_node.value) + "x^" + str(exp)
                    temp_node = temp_node.next
                    exp = exp - 1
                elif temp_node.value < 0:
                    result = result + str(temp_node.value) + "x^" + str(exp)
                    temp_node = temp_node.next
                    exp = exp - 1
                elif temp_node.value == 1:
                    result = result + "+" + "x^" + str(exp)
                    temp_node = temp_node.next
                    exp = exp - 1
                else:
                    temp_node = temp_node.next
                    exp = exp - 1
        return result
    
    def add(self, equ1, equ2):
        res = LinkedList()
        if equ1.head == None or equ2.head == None:
            raise
        if equ1.length > equ2.length:
            for _ in range(equ1.length - equ2.length):
                equ2.prepend(0)
        elif equ1.length < equ2.length:
            for _ in range(equ2.length - equ1.length):
                equ1.prepend(0)
        
        equ1Node = equ1.head
        equ2Node = equ2.head

        while equ1Node != None:
            res.append(equ1Node.value + equ2Node.value)
            equ1Node = equ1Node.next
            equ2Node = equ2Node.next
        
        self.R = res
    
    def sub(self, equ1, equ2):
        res = LinkedList()
        if equ1.head == None or equ2.head == None:
            raise
        if equ1.length > equ2.length:
            for _ in range(equ1.length - equ2.length):
                equ2.prepend(0)
        elif equ1.length < equ2.length:
            for _ in range(equ2.length - equ1.length):
                equ1.prepend(0)
        
        equ1Node = equ1.head
        equ2Node = equ2.head

        while equ1Node != None:
            res.append(equ1Node.value - equ2Node.value)
            equ1Node = equ1Node.next
            equ2Node = equ2Node.next
        
        self.R = res

    def mult(self, equ1, equ2):
        if equ1.head == None or equ2.head == None:
            raise
        arr = [0]*(equ1.length + equ2.length -1)
        res = LinkedList(arr)
        equ1Node = equ1.head
        index1 = 0
        exp2 = equ2.length - 1
        while equ1Node != None:
            equ2Node = equ2.head
            exp1 = equ1.length - 1 - index1
            resExp = exp1 + exp2
            resIndex = res.length - 1 - resExp
            resNode = res.get(resIndex)
            while equ2Node != None:
                prod = equ1Node.value * equ2Node.value
                resNode.value = resNode.value + prod
                equ2Node = equ2Node.next
                resNode = resNode.next
            equ1Node = equ1Node.next
            index1 = index1 + 1

        self.R = res

    def clear(self, equ):
        equ.delete()
        return equ

    def eval(self, equ, value):
        if equ.head == None:
            raise
        res = 0
        equNode = equ.head
        exp = equ.length - 1
        while(equNode != None):
            res = res + equNode.value * value ** exp
            equNode = equNode.next
            exp = exp - 1
        return res

    def selectOperation(self, operation):
        if operation == "set":
            equ = input()
            arr = analyseInput()
            self.set(equ, arr)
        elif operation == "print":
            equ = input()
            if equ == "A":
                print(self.print(self.A))
            elif equ == "B":
                print(self.print(self.B))
            elif equ == "C":
                print(self.print(self.C))
            else:
                raise
        elif operation == "add":
            equ1 = input()
            equ2 = input()
            if equ1 == "A":
                if equ2 == "A":
                    self.add(self.A, self.A)
                    print(self.print(self.R))
                elif equ2 == "B":
                    self.add(self.A, self.B)
                    print(self.print(self.R))
                elif equ2 == "C":
                    self.add(self.A, self.C)
                    print(self.print(self.R))
                else:
                    raise
            elif equ1 == "B":
                if equ2 == "A":
                    self.add(self.B, self.A)
                    print(self.print(self.R))
                elif equ2 == "B":
                    self.add(self.B, self.B)
                    print(self.print(self.R))
                elif equ2 == "C":
                    self.add(self.B, self.C)
                    print(self.print(self.R))
                else:
                    raise
            elif equ1 == "C":
                if equ2 == "A":
                    self.add(self.C, self.A)
                    print(self.print(self.R))
                elif equ2 == "B":
                    self.add(self.C, self.B)
                    print(self.print(self.R))
                elif equ2 == "C":
                    self.add(self.C, self.C)
                    print(self.print(self.R))
                else:
                    raise
            else:
                raise
        elif operation == "sub":
            equ1 = input()
            equ2 = input()
            if equ1 == "A":
                if equ2 == "A":
                    self.sub(self.A, self.A)
                    print(self.print(self.R))
                elif equ2 == "B":
                    self.sub(self.A, self.B)
                    print(self.print(self.R))
                elif equ2 == "C":
                    self.sub(self.A, self.C)
                    print(self.print(self.R))
                else:
                    raise
            elif equ1 == "B":
                if equ2 == "A":
                    self.sub(self.B, self.A)
                    print(self.print(self.R))
                elif equ2 == "B":
                    self.sub(self.B, self.B)
                    print(self.print(self.R))
                elif equ2 == "C":
                    self.sub(self.B, self.C)
                    print(self.print(self.R))
                else:
                    raise
            elif equ1 == "C":
                if equ2 == "A":
                    self.sub(self.C, self.A)
                    print(self.print(self.R))
                elif equ2 == "B":
                    self.sub(self.C, self.B)
                    print(self.print(self.R))
                elif equ2 == "C":
                    self.sub(self.C, self.C)
                    print(self.print(self.R))
                else:
                    raise
            else:
                raise
        elif operation == "mult":
            equ1 = input()
            equ2 = input()
            if equ1 == "A":
                if equ2 == "A":
                    self.mult(self.A, self.A)
                    print(self.print(self.R))
                elif equ2 == "B":
                    self.mult(self.A, self.B)
                    print(self.print(self.R))
                elif equ2 == "C":
                    self.mult(self.A, self.C)
                    print(self.print(self.R))
                else:
                    raise
            elif equ1 == "B":
                if equ2 == "A":
                    self.mult(self.B, self.A)
                    print(self.print(self.R))
                elif equ2 == "B":
                    self.mult(self.B, self.B)
                    print(self.print(self.R))
                elif equ2 == "C":
                    self.mult(self.B, self.C)
                    print(self.print(self.R))
                else:
                    raise
            elif equ1 == "C":
                if equ2 == "A":
                    self.mult(self.C, self.A)
                    print(self.print(self.R))
                elif equ2 == "B":
                    self.mult(self.C, self.B)
                    print(self.print(self.R))
                elif equ2 == "C":
                    self.mult(self.C, self.C)
                    print(self.print(self.R))
                else:
                    raise
            else:
                raise
        elif operation == "clear":
            equ = input()
            if equ == "A":
                print(self.clear(self.A))
            elif equ == "B":
                print(self.clear(self.B))
            elif equ == "C":
                print(self.clear(self.C))
            else:
                raise
        elif operation == "eval":
            equ = input()
            value = int(input())
            if equ == "A":
                print(self.eval(self.A, value))
            elif equ == "B":
                print(self.eval(self.B, value))
            elif equ == "C":
                print(self.eval(self.C, value))
            else:
                raise
        else:
            raise




ps = PolySolver()
while(1):
    try:
        operation = input()
    except EOFError:
        break
    try:
        ps.selectOperation(operation)
    except:
        print("Error")
        break


