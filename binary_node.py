class BinaryNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left =None
        self.right = None
        self.print_created()

    def print_created(self):
        print(f"Node with data {self.data} created !")

    def print_self(self):
        if self.left is None:
            left_str ="none"
        else:
            left_str = self.left.data
        if self.right is None:
            right_str ="none"
        else:
            right_str = self.right.data
        print(f"Node {self.data} updated with a left of {left_str} and a right of {right_str}")


    def insert_node(self,data):
        if self.data:
            if data < self.data: 
                if self.left is None:
                    self.left = BinaryNode(data)
                    self.print_self()
                else:
                    self.left.insert_node(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryNode(data)
                    self.print_self()
                else:
                    self.right.insert_node(data)
            else:
                self.data = data


    def search_node(self,root,data):
        if root:
            if data == root.data:
                print("Node Found")
            elif data < root.data:
                print('direaction left')
                self.search_node(root.left,data)
            elif data > root.data:
                print("direaction right")
                self.search_node(root.right,data)
        else:
            print("Node is not found")
        return    




