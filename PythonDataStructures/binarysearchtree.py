from node import Node



from node import Node



class BinarySearchTree:
    def __init__(self):
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
        current_node = self.head
        
        if self.head == None:
            print('list is empty')
            return
        while current_node != None:
            if current_node.data == data:
                print('node found')
                break
            current_node = current_node.next
        
        
            
        
    
  
      
        
            
            
 
            
            

            
            

    

        
          
 
  
            
