import sys
def collage(x,y): #When passed a list of words x, checks if the list y is possible to be created out of x
    magazine = {}
    for i in x:
        if i in magazine == False:
            magazine[i] = 1
        else:
            magazine[i] = magazine.get(i,0) + 1
    for j in y:
        if j not in magazine or magazine[j]==0: 
            return "NO"
        else:
             magazine[j] = magazine.get(j,0) - 1
    return "YES"

def driver():
    with open(sys.argv[1]) as f:
        m,n = f.readline().strip().split()
        x=f.readline().strip().split()
        y=f.readline().strip().split()
        print(collage(x,y))
        
            

if __name__ == "__main__":
    driver()

