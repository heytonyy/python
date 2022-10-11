class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val) #new node
        current_head = self.head #temp to remember head
        new_node.next = current_head #links new node to head of list
        self.head = new_node #put new node at heads, next is the old head or None if it was empty
        return self
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    def add_to_back(self, val):
        if self.head == None:	# if the list is empty
            self.add_to_front(val)	# run the add_to_front method
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next # on to the next one... on to the next one
        runner.next = new_node
        return self
        
class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None