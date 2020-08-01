class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None



class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next=self.head
        #print(new_node.next)
        if (self.head):
        	print ('before',self.head.data)
        self.head = new_node
        print ('after',self.head.data)
    def printList(self): 
        temp = self.head 
        while(temp): 
            print temp.data, 
            temp = temp.next
  
    def skipMdeleteN(self, M, N): 
        curr = self.head 
          
        # The main loop that traverses through the 
        # whole list 
        while(curr): 
            # Skip M nodes 
            for count in range(1, M): 
                if curr is None: 
                    return 
                curr = curr.next
                      
            if curr is None : 
                return 
  
            # Start from next node and delete N nodes 
            t = curr.next 
            for count in range(1, N+1): 
                if t is None: 
                    break
                t = t.next
      
            # Link the previous list with reamining nodes 
            curr.next = t 
            # Set Current pointer for next iteration 
            curr = t  

LL=LinkedList()
LL.head=Node(3)
LL.head.data
LL.push(1)
LL.head.data
LL.head.data


llist = LinkedList() 
M = 2 
N = 3
llist.push(10) 
llist.push(9) 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 