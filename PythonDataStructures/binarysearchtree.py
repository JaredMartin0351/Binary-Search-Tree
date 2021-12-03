from node import Node



class BinarySearchTree:
    def __init__(self):
        self.next = None
        self.link = None
        self.head = None
        self.tail = None
        
        

    
        
    def insert_node(self, data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next
            
    def search_for_node(self, data):
        self.data = data
        
        if self.data == None:
            print('Nothing in tree')
        
        elif self.data == 50:
            print('good')
            
            

    

        
          
 
  
            
