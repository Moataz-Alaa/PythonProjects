
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

class Queue:
    
    def __init__(self, values=[]):
        self.queueArray = values

    def __str__(self):
        return self.queueArray.__str__()

    def enqueue(self, value):
        self.queueArray.insert(0, value)

    def dequeue(self):
        if self.isEmpty():
            raise
        return self.queueArray.pop(-1)
    
    def front(self):
        if self.isEmpty():
            raise
        return self.queueArray[-1]
    
    def isEmpty(self):
        if self.queueArray == []:
            return True
        else:
            return False
    
    def size(self):
        return len(self.queueArray)
    
    def selectOperation(self):
        try:
            operation = input()
            if operation == "enqueue":
                value = int(input())
                self.enqueue(value)
                print(self)
            elif operation == "dequeue":
                self.dequeue()
                print(self)
            elif operation == "isEmpty":
                print(self.isEmpty())
            elif operation == "size":
                print(self.size())
            else:
                print("Error")
        except:
            print("Error")
            return



testStack = Queue(analyseInput())
testStack.selectOperation()