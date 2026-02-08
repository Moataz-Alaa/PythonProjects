
class Node:
    def __init__(self, value):
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
    
    #The method called when the list is being printed

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
        if index > self.length or index < -(self.length):
            return 'Error: index out of bound'
        elif index == 0 or index == -(self.length):
            self.prepend(value)
            return
        elif index == self.length or index == -1:
            self.append(value)
            return
        elif index < 0:
            positive_index = self.length + index
            temp_node = self.head
            for _ in range(positive_index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
    #This method inserts a node in the given index with the given value
    #This method returns 'Error: index out of bound' and does nothing if the index is out of bound 
    #This method calls the special cases methods in case of special case 
    #This method supports negative indices

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    #This method passes through each node and prints its value

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

    def search_index(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    #This method passes through each node 
    #and searches for the node with target value
    #returns the node's index if found, -1 if not found

    def get(self, index):
        if index > (self.length - 1) or index < -(self.length):
            return Node(None)
        elif index == 0 or index == -(self.length):
            return self.head
        elif index == (self.length - 1) or index == -1:
            return self.tail
        elif index < 0:
            positive_index = self.length + index
            current = self.head
            for _ in range(positive_index):
                current = current.next
            return current
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
    
    #This method returns the node in the given index
    #This method returns an empty node if the index is out of bound 
    #This method returns the special nodes dircetly (head or tail) in case of edge cases
    #This method also supports negative indices

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    #This method sets the value of the node in the given index to the given value
    #This method also supports negative indices

    def get_middle(self):
        mid_index = self.length // 2
        return self.get(mid_index)
    
    #This method returns the middle node of the linked list
    #If the list has an even number of nodes, it returns the second of the two middle nodes

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
        return popped_node
    
    #This method removes the first node in the linked list and returns it

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped_node

    #This method removes the last node in the linked list and returns it

    def remove(self, index):
        if index > (self.length - 1) or index < -(self.length):
            return Node(None)
        elif index == 0 or index == -(self.length):
            return self.pop_first()
        elif index == (self.length - 1) or index == -1:
            return self.pop()
        elif index < 0:
            positive_index = self.length + index
            prev_node = self.get(positive_index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node
        
    #This method removes the node in the given index and returns it
    #This method returns an empty node if the index is out of bound
    #This method calls the special cases methods in case of special case
    #This method also supports negative indices

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

    #This method reverses the linked list

    def remove_duplicates(self):
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



list_1 = LinkedList([1,2,4])
list_2 = LinkedList([1,3,4])
merged_list = LinkedList()
current_node_l1 = list_1.head
current_node_l2 = list_2.head
while current_node_l1 is not None and current_node_l2 is not None:
    if current_node_l1.value <= current_node_l2.value:
        merged_list.append(current_node_l1.value)
        current_node_l1 = current_node_l1.next
    elif current_node_l1.value > current_node_l2.value:
        merged_list.append(current_node_l2.value)
        current_node_l2 = current_node_l2.next

while current_node_l1 is not None:
        merged_list.append(current_node_l1.value)
        current_node_l1 = current_node_l1.next

while current_node_l2 is not None:
        merged_list.append(current_node_l2.value)
        current_node_l2 = current_node_l2.next


print (merged_list)