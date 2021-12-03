from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next

#        temp_node = self.head

#        while temp_node.next is not None:
#            temp_node = temp_node.next

#        temp_node.next = node

