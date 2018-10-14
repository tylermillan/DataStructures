import sys

class minheap(object):
"""
Uses a priority queue data structure to service a batch of HTTP requests over a LAN in batches by completing the shortest requests first
and returns the order of completed services HTTP's 
"""
    class Node(object):
        def __init__(self,ip,est):
            self.ip = ip
            self.est = est
    def __init__(self):
        self.heap = [0]
        self.heapsize = 0

    def size(self):
        return self.heapsize

    def is_empty(self):
        return (self.heapsize == 0)

    def remove(self):
        if self.heapsize==0:
            return("HeapError")
        else:    
            minval = self.heap[1]
            self.heap[1] = self.heap[self.heapsize]
            self.heap.pop()
            self.heapsize = self.heapsize - 1
            self.bubbledown(1)
            return(minval)
    
    def insert(self,ip, est):
        node = self.Node(ip, est)
        self.heap.append(node)
        self.heapsize = self.heapsize+1
        self.bubbleup(self.heapsize)

    def look(self):
        if self.heapsize==0:
            return("HeapError")
        else:
            return(self.heap[1].est)
    
    def bubbledown(self,i):
        while (i*2) <= self.heapsize:
            sc= self.smallestchild(i)
            if self.heap[i].est > self.heap[sc].est:
                temporary = self.heap[i]
                self.heap[i] = self.heap[sc]
                self.heap[sc] = temporary
            i = sc

    def bubbleup(self,i):
        while i // 2 > 0:
            if self.heap[i].est <= self.heap[i//2].est:
                temporary = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = temporary
            i = i // 2

    def insert(self,ip,est):

        node = self.Node(ip, est)

        self.heap.append(node)
        self.heapsize = self.heapsize+1
        
        self.bubbleup(self.heapsize)

    def smallestchild(self,i):
        if i * 2 + 1 > self.heapsize:
            return (i*2)
        else:
            if self.heap[i*2].est <= self.heap[i*2+1].est:
                return i * 2
            else:
                return i * 2 + 1
    
    def to_string(self):
        if self.is_empty() is True:
            return("Empty")
        else:
            for i in range(self.heapsize):
                print(self.remove().ip)
                
def driver():
    Aheap = minheap()
    Bheap = minheap()


    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            line = f.readline().strip().split()
            ip = line[0]
            priority = str(line[1])
            time = int(line[2])

            if priority =="A":
                Aheap.insert(ip, time)
            else:
                Bheap.insert(ip, time)
    
    Aheap.to_string()
    Bheap.to_string()

if __name__ == "__main__":
    driver()
       
