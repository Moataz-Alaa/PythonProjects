
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularLinkedList:
    
    def __init__(self, initial_nodes_values=[]):
        if len(initial_nodes_values) == 0:
            self.head = None
            self.tail = None
        elif len(initial_nodes_values) == 1:
            temp_node = Node(initial_nodes_values[0])
            self.head = self.tail = temp_node
            temp_node.next = temp_node
        else:
            self.head = Node(initial_nodes_values[0])
            temp_node = self.head
            for i in range(1, len(initial_nodes_values) - 1):
                new_node = Node(initial_nodes_values[i])
                temp_node.next = new_node
                temp_node = new_node
            self.tail = Node(initial_nodes_values[len(initial_nodes_values) - 1])
            temp_node.next = self.tail
            self.tail.next = self.head
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
            if temp_node == self.head:
                break
        return result
    
    #The method called when the list is being printed

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.length += 1
    
    #This method inserts a node in the last index with the given value

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1

    #This method inserts a node in the first index with the given value

    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length or index < -(self.length):
            return 'Error: index out of bound'
        elif index == 0 or index == -(self.length):
            self.prepend(value)
            return
        elif index == self.length:
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
            if current == self.head:
                break
    
    #This method passes through each node and prints its value

    def copy(self):
        list_copy = []
        current = self.head
        while current is not None:
            list_copy.append(current.value)
            current = current.next
            if current == self.head:
                break
        return CircularLinkedList(list_copy)

    #This method returns a deep copy of the linked list

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
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
            if current == self.head:
                break
            index += 1
        return None
    
    #This method passes through each node 
    #and searches for the node with target value
    #returns the node's index if found and returns none if not found

    def get(self, index):
        if index > (self.length - 1) or index < -(self.length):
            return Node()
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
            self.tail.next = self.head
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
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node.value

    #This method removes the last node in the linked list and returns its value

    def remove(self, index):
        if index > (self.length - 1) or index < -(self.length):
            return None
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
            return popped_node.value
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node.value
        
    #This method removes the node in the given index and returns its value
    #This method returns none if the index is out of bound
    #This method calls the special cases methods in case of special case
    #This method also supports negative indices

    def remove_value(self, target):
        while self.search_index(target) is not None:
            self.remove(self.search_index(target))
        return self
    
    #This method deletes all ocurences of the given target value from the linked list and returns the linked list
        
    def delete(self):
        self.tail.next = None
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
            if current_node == self.head:
                break
        temp = self.head
        self.head = self.tail
        self.tail = temp
        self.tail.next = self.head
        return self

    #This method reverses the linked list in place and returns it

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
        return CircularLinkedList(unique_arr)
    
    #This methods returns a new linked list without duplicates from another linked list



# creating and printing tests:

linked_list = CircularLinkedList([10, 20, 40, 40, 50, 60])
print(linked_list)
print(linked_list.length)

# linked_list1 = CircularLinkedList([10])
# print(linked_list1)
# print(linked_list1.length)

# linked_list2 = CircularLinkedList([])
# print(linked_list2)
# print(linked_list2.length)

# linked_list3 = CircularLinkedList()
# print(linked_list3)
# print(linked_list3.length)


# inserting tests:

# linked_list.insert(0, 1)
# print(linked_list)
# print(linked_list.length)

# linked_list.insert(-6, 1)
# print(linked_list)
# print(linked_list.length)

# linked_list.insert(6, 1)
# print(linked_list)
# print(linked_list.length)

# linked_list.insert(-1, 1)
# print(linked_list)
# print(linked_list.length)

# linked_list.insert(3, 1)
# print(linked_list)
# print(linked_list.length)

# linked_list.insert(-3, 1)
# print(linked_list)
# print(linked_list.length)

# linked_list.insert(8, 1)
# print(linked_list)
# print(linked_list.length)

# linked_list.insert(-7, 1)
# print(linked_list)
# print(linked_list.length)



# print(linked_list.remove(-5))
# print(linked_list)
# print(linked_list.length)

# print(linked_list.reverse())
# print(linked_list)
# print(linked_list.length)

# print(linked_list.get_middle().value)
# print(linked_list.remove_duplicates())
# print(linked_list.head.value)

# head1 = CircularLinkedList([1,2,6,3,4,5,6])
# print(head1.remove_value(6))
# head2 = CircularLinkedList([])
# print(head2.remove_value(1))
# head3 = CircularLinkedList([7,7,7,7])
# print(head3.remove_value(7))

# linked_list1 = linked_list.copy()
# print(linked_list)
# print(linked_list1)
# linked_list1.pop()
# print(linked_list)
# print(linked_list1)

