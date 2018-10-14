import sys
class minheap(object):
    def __init__(self):
        self.heap = [0]
        self.heapsize = 0
        
    def size(self):
        return self.heapsize
    
    def insert(self,i):
        self.heap.append(i)
        self.heapsize = self.heapsize+1
        self.bubbleup(self.heapsize)
        
    def is_empty(self):
        return (self.heapsize == 0)
    
    def bubbledown(self,i):
        while (i*2) <= self.heapsize:
            sc= self.smallestchild(i)
            if self.heap[i] > self.heap[sc]:
                temporary = self.heap[i]
                self.heap[i] = self.heap[sc]
                self.heap[sc] = temporary
            i = sc
    def bubbleup(self,i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                temporary = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = temporary
            i = i // 2

    def smallestchild(self,i):
        if i * 2 + 1 > self.heapsize:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
        
    def look(self):
        if self.heapsize==0:
            return("HeapError")
        else:
            return(self.heap[1])
    
    def remove(self):
        if self.heapsize==0:
            return("HeapError")
        else:    
            minval = self.heap[1]
            self.heap[1] = self.heap[self.heapsize]
            self.heapsize = self.heapsize - 1
            self.heap.pop()
            self.bubbledown(1)
            return(minval)
    
    def to_string(self):
        list=[]
        if self.is_empty() is True:
            return("Empty")
        else:
            for x in self.heap[1:]:
                if self.heap[-1]==x:
                    list.append(x)
                else:
                    list.append(x)
                    list.append(" ")
            return("".join(list))
def driver():
    s = minheap()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action = in_data[0]
            if action == "insert":
                value = in_data[1]
                s.insert(value)
            elif action == "remove":
                print(s.remove())
            elif action == "print":
                print(str(s.to_string()))
            elif action == "size":
                print(s.size())
            elif action == "best":
                print(s.look())
if __name__ == "__main__":
    driver()
          
