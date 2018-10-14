import sys
import copy

class Underflow(Exception):
    def __init__(self,data=None):
        super().__init__(data)
            
class LLNode:
    def __init__(self, data=None):
        self.data= data
        self.next= None
        
class LLStack(object):            
    def __init__(self):
        self.head= None
    
    def is_empty(self):
        return(self.head == None)
    
    def push(self, x):
        y = LLNode(x)
        y.next = self.head
        self.head = y
        
    def pop(self):
        if self.is_empty():
            raise Underflow('pop() was invoked on an empty stack')
        else:
            y = self.head.data
            self.head = self.head.next
            return y
        
def print_stack(x):
    s=[]
    y = copy.copy(x)
    if y.is_empty():
        print('Empty')
    else:
        while y.is_empty()==False:
            z=str(y.pop())
            s.append(z)
            s.append(" ")
        del s[-1]
        print("".join(s))
    
        
       
def driver():
    s = LLStack()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "push":
                value = int(value_option[0])
                s.push(value)
            elif action == "pop":
                try:
                    print(s.pop())
                except Underflow:
                    print("StackError")
            elif action == "print":
                print_stack(s)

if __name__ == "__main__":
    driver()
          
            
                



                
