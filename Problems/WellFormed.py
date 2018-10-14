import sys
def wellformed(x): 
#When passed a string of various forms of brackets, checks if they are "well formed", i.e. for every open bracket there is a closing bracket
    stack = []
    for i in x:
        if i=="(":
            stack.append(")")
        elif i=="[":
            stack.append("]")
        elif i=="{":
            stack.append("}")
        elif i=="<":
            stack.append(">")
        else:
            if (stack.pop() != i):
                return "NO"
    if len(stack)!=0:
        return "NO"
    return "YES"

def driver():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            x = f.readline().strip()
            print(wellformed(x))
            

if __name__ == "__main__":
    driver()