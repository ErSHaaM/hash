class node:
    def __init__(self,value,key):
        self.value=value
        self.next=None
        self.key=key
        
  
  
l=[None for i in range(101)]   

def puthash(key,value):
    ind=0
    for i in key:
        ind+=ord(i)
        
    ind=ind%len(l)
    
    if l[ind]:
        t=l[ind]
        
        while t.next:
            t=t.next
            
        t.next=node(value,key)
        
        
    else:
        l[ind]=node(value,key)
        
def gethash(key):
    ind=0
    for i in key:
        ind+=ord(i)
        
    ind=ind%len(l)
    
    if l[ind] is None:
        print(' DNE ')
    else:
        
        t=l[ind]
        
        
        while t.next and t.key!=key:
            t=t.next
            
        if t and t.key==key:
            print(t.value)
        else:
            print(' DNE ')
        
            
     
puthash('Sheikh','Shaam')
gethash('heikhS')
