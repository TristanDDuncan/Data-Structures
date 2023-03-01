class Node:
    def __init__(self,data):
        self.next =  None
        self.data = data




class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
    def append_node (self,data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        else:
            self.tail.next = node
            self.tail = self.tail.next
    
    def find_node(self,data):
        current_node =self.head
        while current_node is not None: 
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False


        


class main:
    def __init__ (self):
        self.list = Linklist()

    def append_node (self):
        print("\n Add a new node with the value of 40")
        self.list.append_node(40)
        print("\n Add a new node with the value of 55")
        self.list.append_node(55)
        print("\n Add a new node with the value of 75")
        self.list.append_node(75)
    
        
    def find_values (self):
        print("\nSearch for a node with the value of 55")
        print(self.list.find_node(55))
        print("\nSearch for a node with the value of 88")
        print(self.list.find_node(88))








link_list =Linklist()
link_list.append_node(23)
link_list.append_node(45)
link_list.append_node(67)
runmain = main()
runmain.append_node()
runmain.find_values()