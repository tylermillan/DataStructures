import sys
import heapq

def rolling_median(y): 
"""
an algorithm to compute the cumulative rolling median and test it on simulated streaming data
When passed an input file, will output the median at each iteration of inputs
"""
    minheap=[]
    maxheap=[]
    for i in y:
        #should occur on first run since both heaps are empty
        if len(maxheap)==0 and len(minheap)==0:
            heapq.heappush(maxheap,-i)
            print(i)
            
        #bottom half of the numbers are maxheap
        elif len(maxheap)>0:
            if i >= (-maxheap[0]):
                heapq.heappush(minheap,i)
            else:
                heapq.heappush(maxheap,-i)

            #occurs if maxheap and minheap are equal in size, indicating the total is the min value of the minheap,
            # and the max value of the maxheap added together and divided in half
            if len(maxheap) == len(minheap):
                med=((-maxheap[0]+minheap[0])/2)
                if med%1==0:
                    print (int(med))
                else:
                    print ("%.1f" % med)
                    
            #next two cases occur when there is an odd number of total elements and whichever heap contains an extra
            #value, has its top value returned as the median value
            elif len(maxheap) == len(minheap)+1:
                med =(-maxheap[0])
                if med%1==0:
                    print (int(med))
                else:
                    print ("%.1f" % med)
            elif len(minheap)==len(maxheap)+1:
                med =(minheap[0])
                if med%1==0:
                    print (int(med))
                else:
                    print ("%.1f" % med)
            #last two cases occur if min and maxheap do not contain equal amounts of elements
            elif len(minheap)==len(maxheap)+2:
                heapq.heappush(maxheap,-heapq.heappop(minheap))
                med =((-maxheap[0]+minheap[0])/2)
                if med%1==0:
                    print (int(med))
                else:
                    print ("%.1f" % med)
            elif len(maxheap)==len(minheap)+2:
                heapq.heappush(minheap,-heapq.heappop(maxheap))
                med =((-maxheap[0]+minheap[0])/2)
                if med%1==0:
                    print (int(med))
                else:
                    print ("%.1f" % med)
def driver():
    y =[]
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            y.append(int(f.readline().strip()))
        rolling_median(y)

if __name__ == "__main__":
    driver()
