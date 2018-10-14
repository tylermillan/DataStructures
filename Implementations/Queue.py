import sys
import copy

class Underflow(Exception):
    def __init__(self, data=None):
        super().__init__(data)
        
class LLNode:
    def __init__(self, data=None):
        self.data= data
        self.next= None
        
class LLQueue(object):
    def __init__(self):
        self.head= None
        self.tail= None
            
    def enqueue(self, x):
        next_node = LLNode(x)
        if self.is_empty():
            self.head= next_node
            self.tail= self.head
        else:
            self.tail.next = next_node
            self.tail = next_node

    def is_empty(self):
        return(self.head == None and self.tail == None)
        
    def dequeue(self):
        if self.head == None:
            raise Underflow('dequeue() invoked on Empty Queue')
        else:
            temp = self.head.data
            next = self.head.next
            if next== None:
                self.head = None
                self.tail = None
            else:
                self.head = next
            return temp
            
def print_queue(q):
    s=[]
    y = copy.copy(q)
    if y.is_empty():
        print('Empty')
    else:
        while y.is_empty()==False:
            z=str(y.dequeue())
            s.append(z)
            s.append(" ")
        del s[-1]
        print("".join(s))
        
def driver():
    q = LLQueue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "enqueue":
                value = int(value_option[0])
                q.enqueue(value)
            elif action == "dequeue":
                try:
                    print(q.dequeue())
                except Underflow:
                    print("QueueError")
            elif action == "print":
                print_queue(q)

if __name__ == "__main__":
    driver()