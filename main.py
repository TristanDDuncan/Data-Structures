from binary_node import BinaryNode


if __name__ == '__main__':

    root =BinaryNode(55)
    root.insert_node(34)
    root.insert_node(67)
    root.insert_node(26)
    root.insert_node(60)
    root.insert_node(16)
    root.insert_node(88)


    print("\nSearch for node with the value 60")
    root.search_node(root,60)
    print("\nSearch for node with the value 11")
    root.search_node(root,11)