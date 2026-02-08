# Enter your code here. Read input from STDIN. Print output to STDOUT

class calculator:
    
    def init(self):
        self.operation = None
        
    def analyseInput(self, input):
        self.operation = input.split(' ')

    def executeOperation(self):
        if len(self.operation) != 3:
            return "Error"
        try:
            num_1 = int(self.operation[0])
            num_2 = int(self.operation[2])
        except:
            return "Error"
        result = None
        if self.operation[1] == '+':
            result = num_1 + num_2
        elif self.operation[1] == '/':
            if num_2 == 0:
                return "Error"
            result = num_1 / num_2    
        else:
            return "Error"
        return result
    
calcInput = input()
newClac = calculator()
newClac.analyseInput(calcInput)
print(newClac.operation)
print(newClac.executeOperation())