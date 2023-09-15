import random 


process_IDs=[]
for i in range(1000):  
    process_IDs.append(i)

class Page:
    '''Create Page object with doubly linked list attributes'''
    def __init__(self, elem, prev, next):  
        self.prev=prev
        self.next=next
        self.elem=elem
        self.status="free"
        
class Block:
    '''Create  Block object with doubly linked list attributes'''
    def __init__(self, *args):
        #initiate doubly-linked list attributes
        self.prev=None
        self.next=None
        self.elem=None
        if args:
            self.num=args[0]

        #NoneType head and tails to give structure
        self.head=Page(None, None, None)  
        self.tail=Page(None, self.head, self.head)  
        self.head.next=self.tail

        #keep track of size 
        self.size=0 

        #pointers
        self.first=None
        self.current= None
        self.status="free"  
        
        #Variables used in later stages
        self.clock_cycle=True
        self.page_bit=None

    def add_pages(self, num_IDs):
        '''fill block with Page objects'''
        i=0
        List_str=""
        if num_IDs>self.num:
            print("Too many pages for block size")
            exit
        else:
            #Deal with first element being added
            while i<self.num:
                if self.size==0:
                    node=Page(None, self.head, self.tail)
                    #update attributes
                    node.status="taken"
                    self.first=node
                    self.current=node
                    #update string representation
                    List_str+=(str(node.elem)+" ")
                   
                    self.size+=1
                    
                    
                else:
                    #deal with every element other than first
                    node=Page(None, self.current, self.tail)
                    List_str+=(str(node.elem)+" ")
                    node.status="taken"
                    
                    self.size+=1
                    self.current=node
                
                i+=1
            #return string represenatation of block
            self.elem=List_str
            return List_str
           
    
    
class Process:
    '''Create object of process'''
    num_processes=0
    def __init__(self):  
        #Assign process ID
        self.process_ID=random.choice(process_IDs)
        
        self.num_processes+=1



class LinkedList:
    '''Create linked list as memory '''
    def __init__(self):
        """ Initialise an empty library. """  
        self.head=Block()
        
        #self.process=process
        self.tail=Block()
        self.head.next=self.tail
        
        self.size=0
        self.current=None  
        
    
    def add_node(self, length):
        #Deal with first element being added
        if self.size==0:
            node=Block(length)
            node.add_pages(length)
            
            node.next=self.tail
            node.prev=self.head
            
            self.first=node
            self.current=node
            
            self.size+=1
            
        else:
            #deal with every element other than first
            
            
            
            node=Block(length)
            node.add_pages(length)
      
            
            #change attributes
            node.next=self.tail
            self.tail.prev=node
            node.prev=self.current
            node.prev.next=node
            
            
            #increase size
            self.size+=1
            #change pointer
            self.current=node     
         
            
    def get_current(self):
        '''return current'''
        
        return self.current.elem
    def next(self):
        '''return pointer after pointer'''
        if self.current==None:
            return self.head
        else:
            
            if self.current==self.tail:
                return self.first
            else:
                print(self.current)
                return self.current.next
    def prev(self):
        '''return prev'''
        if self.current==None:
            return self.head
        else:
            self.current=self.current.prev
            if self.current==None:
                return self.head
            else:
                print(self.current)
                return self.current.prev
    def reset(self):
        '''return pointer back to first'''
        self.current=self.first
        print(self.current)
   
    def remove_current(self):
        '''remove pointer'''
        if self.size==0:
            return None
        else:
            removed=self.current 
            previous=self.current.prev
            after=self.current.next
            previous.next=after
            return previous, after, self.size, removed

            
    def length(self):
        '''return size'''
        return self.size
    




class nextFit:
    '''Allocate memory'''
    def __init__(self, list:LinkedList):
        '''Initialize variables'''
        self.current=list.first
        self.list=list
        
        
        
    
    def allocate(self, size, process):  
        '''allocate according to size'''
        #Size constants
        self.four=4
        self.eight=8
        self.sixt=16  
        self.thirtytwo=32
        

        self.process=process
        self.size=size  
        
        #self.current2=self.current.first
        while self.current:
            #Deal with loop
            if self.current==self.list.tail:  
                self.current=self.list.first
                
            else:
                #Compare size and constant variables to find appropriate block
                if self.current.size>=self.size: #all processes must require less/equal pages than in block
                    if self.size<=self.four:
                        if self.current.size==self.four and self.current.status=="free":
                            self.diff=self.current.size-self.size
                            self.current.elem=(str(self.process)+" ")*self.size + (str(None)+" ")*self.diff                           
                            self.current.status="taken"
                            self.current=self.current.next
                            
                            break
                    elif self.current.size==self.eight and self.size<=self.eight and self.size>=self.four:
                        if self.current.status=="free":
                            self.diff=self.current.size-self.size
                            self.current.elem=(str(self.process)+" ")*self.size + (str(None)+" ")*self.diff
                            self.current.status="taken"
                            self.current=self.current.next
                            break
                    
                    elif self.current.size==self.sixt and self.size<=self.sixt and self.size>=self.eight:
                        if self.current.status=="free":
                            self.diff=self.current.size-self.size
                            self.current.elem=(str(self.process)+" ")*self.size + (str(None)+" ")*self.diff
                            self.current.status="taken"
                            self.current=self.current.next
                            
                            break
                    elif self.current.size==self.thirtytwo and self.size<=self.thirtytwo and self.size>=self.sixt:
                        if self.current.status=="free":
                            self.diff=self.current.size-self.size
                            self.current.elem=(str(self.process)+" ")*self.size + (str(None)+" ")*self.diff
                            self.current.status="taken"
                            self.current=self.current.next
                            break
                    
                   
                  
                    else:
                        
                        self.current=self.current.next
            self.current=self.current.next

        
class Second_Chance:  
    '''Page replacement Algorithm'''
    def __init__(self, frame_size, list:LinkedList, clock_cycle):
        
        self.clock_cycle=clock_cycle
         
        self.frame_size=frame_size
        
        self.list=list
        
        #Initialize lists
        self.elems=[None] *self.frame_size
        self.frames=[None] *self.frame_size
        
        #Create pointer
        self.current=self.list.first
        
    def change_page(self):
        '''Swap out pages'''
        i=0
        while i<len(self.frames):
            #Fill lists
            self.frames[i]=self.current #fill with object references
            self.elems[i]=self.current.elem  #fill with elems
            self.current=self.current.next #move up memory
            i+=1
        for node in self.frames: 
            node.clock_cycle=self.clock_cycle
            if node.clock_cycle==True: #Process has been there for more than a clock cycle
                node.page_bit=0 #change bit value 
                node.elem=(str(None)+" ")*16
            else:
                node.page_bit=1 #change bit value 
        for node in self.frames: 
            if node.page_bit==0:
                
                node.elem=(str(None)+" ")*node.size #change elem to wipe block clean
            elif node.page_bit==1: 
                node.page_bit=0 #change bit value 

                #remove and append node to start of lists
                self.frames.remove(node) 
                self.frames.append(node)
                self.elems.remove(node)
                self.elems.append(node)

        return self.elems
          

class Tracker:
    '''Track free memory'''
    def __init__(self, list:LinkedList):
        '''Initialize variables'''
        self.mem=list 
        self.current=self.mem.first  
        i=0
        #deal with loop and track availability
        while self.current!=self.mem.tail and i<self.mem.size:  
            print("Block "+str(i)+":"+str(self.current.status))
            if self.current.next==self.mem.tail:
                self.current=self.mem.first
            else:
                self.current=self.current.next
            i+=1

'''Testing'''

process1:Process=Process()
process2:Process=Process()
process3:Process=Process()
process4:Process=Process()
process5:Process=Process()
process6:Process=Process()
process7:Process=Process()
process8:Process=Process()
process9:Process=Process()
process10:Process=Process()
process11:Process=Process()
process12:Process=Process()
process13:Process=Process()
    
process:Process=Process()
   
block:Block=Block(16)
print((block.add_pages(16)))
   
list:LinkedList=LinkedList()
(list.add_node(4))
(list.add_node(4))
(list.add_node(4))    
(list.add_node(4))
(list.add_node(4))
(list.add_node(4))
(list.add_node(4))    
(list.add_node(4))

(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))
(list.add_node(8))

(list.add_node(16))  
(list.add_node(16))
(list.add_node(16))
(list.add_node(16))
(list.add_node(16))  
(list.add_node(16))
(list.add_node(16))
(list.add_node(16))
(list.add_node(16))  
(list.add_node(16))
(list.add_node(16))
(list.add_node(16))
(list.add_node(16))  
(list.add_node(16))
(list.add_node(16))
(list.add_node(16))

(list.add_node(32))
(list.add_node(32))


fit:nextFit=nextFit(list) 


fit.allocate(2, process1.process_ID )  
fit.allocate(5, process2.process_ID )     
fit.allocate(5, process3.process_ID )      
fit.allocate(2, process4.process_ID )
fit.allocate(10, process5.process_ID ) 
fit.allocate(31, process6.process_ID )
fit.allocate(20, process7.process_ID )
fit.allocate(2, process8.process_ID )
fit.allocate(8, process9.process_ID )
fit.allocate(16, process10.process_ID )
fit.allocate(11, process11.process_ID )
fit.allocate(7, process12.process_ID )
fit.allocate(12, process13.process_ID )

j=0 
current=list.first
while current!=list.tail:
        print("\nBlock "+str(j)+": "+ current.elem)
        
        j+=1
       

        current=current.next


SecCha:Second_Chance=Second_Chance(13,  list, True)
print("\nSecond Chance:" + str(SecCha.change_page()))

tracker:Tracker=Tracker(list)


