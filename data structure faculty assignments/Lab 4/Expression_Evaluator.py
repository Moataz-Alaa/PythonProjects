
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

def validateExpression(infixExpression):
    #Valid first character test
    if not (infixExpression[0] in ["a", "b", "c", "+", "-", "("]):
        raise
    #Only valid characters and valid last character test
    validCharacters = ["a", "b", "c", "+", "-", "*", "/", "^", "(", ")"]
    for char in infixExpression:
        if not (char in validCharacters):
            raise
    if not (char in ["a", "b", "c", ")"]):
        raise
    #Symbols placement test
    i = 1
    while i < len(infixExpression):
        char = infixExpression[i-1]
        charNext = infixExpression[i]
        if char in ["a", "b", "c"] and not (charNext in ["+", "-", "*", "/", "^", ")"]):
            raise
        elif char in ["+", "*", "/", "^"] and not (charNext in ["a", "b", "c", "+", "-", "("]):
            raise
        elif char == "-" and not (charNext in ["a", "b", "c", "+", "-", "("]):
            raise
        elif char == "(" and not (charNext in ["a", "b", "c", "+", "-", "("]):
            raise
        elif char == ")" and not (charNext in ["+", "-", "*", "/", "^", ")"]):
            raise
        i = i + 1
    #Matching parentheses test
    parentheses = Stack()
    for char in infixExpression:
        if char == "(":
            parentheses.push(char)
        elif char == ")":
            if parentheses.isEmpty() or not parentheses.peek() == "(":
                raise
            parentheses.pop()
    if not parentheses.isEmpty():
        raise

def removeConsectiveMinuses(infixExpression):
    #Check for more than two Consective Minuses
    prevResult = infixExpression
    result = ""
    i = 0
    while i < (len(prevResult) - 2):
        if prevResult[i] == "-" and prevResult[i+1] == "-" and prevResult[i+2] == "-":
            result = result + prevResult[i]
            i = i + 3
        else:
            result = result + prevResult[i]
            i = i + 1
    result = result + prevResult[i:]

    #Check for two Consective Minuses at the start
    while (result[0] == "-" and result[1] == "-"):
        result = result[2:]
    
    #Check for two Consective Minuses after a symbol
    prevResult = result
    result = ""
    i = 0
    while i < (len(prevResult) - 2):
        if prevResult[i] in ["+", "*", "/", "^", "("] and prevResult[i+1] == "-" and prevResult[i+2] == "-":
            result = result + prevResult[i]
            i = i + 3
        elif (prevResult[i] in ["a", "b", "c"] and prevResult[i+1] == "-" and prevResult[i+2] == "-"):
            result = result + prevResult[i]
            result = result + "+"
            i = i + 3
        else:
            result = result + prevResult[i]
            i = i + 1
    result = result + prevResult[i:]
    
    #Check for plus at the start
    while (result[0] == "+"):
        result = result[1:]
    
    #Check for plus as a sign
    prevResult = result
    result = ""
    i = 0
    while i < (len(prevResult) - 1):
        if prevResult[i] in ["+", "-", "*", "/", "^", "("] and prevResult[i+1] == "+":
            result = result + prevResult[i]
            i = i + 2
        else:
            result = result + prevResult[i]
            i = i + 1
    result = result + prevResult[i:]
    return result

def precedence(operator1, operator2):
    if (operator1 == "^"):
        return 1
    if (operator1 in ["*", "/"]):
        return operator2 != "^"
    if (operator1 in ["+", "-"]):
        return not (operator2 in ["^", "*", "/"])
    return 0

def associativity(operator):
    if operator in ["+", "-", "*", "/"]:
        return "left"
    elif operator == "^":
        return "right"

def infixToPostfix(infixExpression):
    operators = Stack()
    postfix = ""
    for char in infixExpression:
        if char in ["a", "b", "c"]:
            postfix = postfix + char
        elif char == '(':
            operators.push(char)
        elif char == ')':
            topOperator = operators.pop()
            while topOperator != '(':
                postfix = postfix + topOperator
                topOperator = operators.pop()
        else:
            while not operators.isEmpty() and precedence(operators.peek(), char):
                if associativity(char) == "left":
                    postfix = postfix + operators.pop()
                elif associativity(char) == "right" and associativity(operators.peek()) == "right":
                    break
                else:
                    postfix = postfix + operators.pop()
            operators.push(char)  
    while not (operators.isEmpty()):
        postfix = postfix + operators.pop()
    return postfix

def evaluatePostfix(postfixExpression,a,b,c):
    operands = Stack()
    for char in postfixExpression:
        if char in ["a", "b", "c"]:
            if char == "a":
                operands.push(a)
            elif char == "b":
                operands.push(b)
            elif char == "c":
                operands.push(c)
        else:
            result = 0
            operand2 = operands.pop()
            if operands.isEmpty() and char == "-":
                operand1 = 0
            else:
                operand1 = operands.pop()
            if char == "^":
                if operand1 == 0 and operand2 == 0:
                    raise
                elif operand1 == 0 and operand2 != 0:
                    result = 0
                else:
                    result = int(operand1 ** operand2)
            elif char == "*":
                result = int(operand1 * operand2)
            elif char == "/":
                if operand2 == 0:
                    raise
                result = int(operand1 // operand2)
            elif char == "+":
                result = int(operand1 + operand2)
            elif char == "-":
                result = int(operand1 - operand2)
            operands.push(result)
    return operands.pop()



def mainFunction():
    try:
        infixExpression = input()
        a = input()
        if a[0:2] != "a=":
            raise
        a = int(a[2:len(a)])
        b = input()
        if b[0:2] != "b=":
            raise
        b = int(b[2:len(b)])
        c = input()
        if c[0:2] != "c=":
            raise
        c = int(c[2:len(c)])
        validateExpression(infixExpression)
        simplifiedInfixExpression = removeConsectiveMinuses(infixExpression)
        postfixExpression = infixToPostfix(simplifiedInfixExpression)
        print(postfixExpression)
        print(evaluatePostfix(postfixExpression,a,b,c))
    except:
        print("Error")
        return



mainFunction()

