import  sys

class Node(object):
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key
        self.parent = None

class BST(object):

    def __init__(self):
        self.root = None
        
    def isempty(self):
        return (self.root == None)
    
    def insert(self, x):
        root = self.root
        y = None
        while root is not None:
            y = root
            if x.key < root.key:
                root = root.left
            else:
                root = root.right
        x.parent = y
        
        if y == None:
            self.root = x
        elif x.key < y.key:
            y.left = x
        else:
            y.right = x
            
    def transplant(self,u,v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def remove(self,x):
        if x.left == None:
            self.transplant(x,x.right)
        elif x.right == None:
            self.transplant(x,x.left)
        else:
            y = self.minimum(x.right)
            if y.parent is not x:
                self.transplant(y,y.right)
                y.right = x.right
                y.right.parent = y
            self.transplant(x,y)
            y.left = x.left
            y.left.parent = y
            
    def search(self,x,k):
        if x is None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left,k)
        else:
            return self.search(x.right,k)

    def maximum(self,x):
        while x.right is not None:
            x = x.right
        return x.key
    
    def minimum(self,x):
        while x.left is not None:
            x = x.left
        return x.key
    
    def to_list_preorder(self):
        prelist = []
        self.preorder(self.root, prelist)
        return prelist
    
    def preorder(self, x, prelist):
        if x:
            prelist.append(str(x.key))
            self.preorder(x.left, prelist)
            self.preorder(x.right, prelist)
            
    def to_list_inorder(self):
        reglist = []
        self.inorder(self.root, reglist)
        return reglist
            
    def inorder(self, x, reglist):
        if x:
            self.inorder(x.left, reglist)
            reglist.append(str(x.key))
            self.inorder(x.right, reglist)

    def to_list_postorder(self):
        postlist = []
        self.postorder(self.root, postlist)
        return postlist

    def postorder(self, x, postlist):
        if x:
            self.postorder(x.left, postlist)
            self.postorder(x.right, postlist)
            postlist.append(str(x.key))

def driver():
    x = BST()
    
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            line = f.readline().strip().split()
            action = line[0]
            
            if action == "insert":
                val = Node(int(line[1]))
                x.insert(val)
                
            elif action == "remove":
                if x.isempty()==True:
                    print("TreeError")
                else:
                    val = x.search(x.root,int(line[1]))
                    if not val:
                        print("TreeError")
                    else:
                        x.remove(val)
                
            elif action == "search":
                if x.isempty()==True:
                    print("NotFound")
                else:
                    val = x.search(x.root,int(line[1]))
                    if not val:
                        print("NotFound")
                    else:
                        print("Found")
                    
            elif action == "max":
                if x.isempty()==True:
                    print("Empty")
                else:
                    print(x.maximum(x.root))
                    
            elif action == "min":
                if x.isempty()==True:
                    print("Empty")
                else:
                    print(x.minimum(x.root))
                    
            elif action == "preprint":
                preprint = x.to_list_preorder()
                if x.isempty()==True:
                    print("Empty")
                else:
                    print(' '.join(x.to_list_preorder()))
                    
            elif action == "inprint":
                inprint = x.to_list_preorder()
                if x.isempty()==True:
                    print("Empty")
                else:
                    print(' '.join(x.to_list_inorder()))
                    
            elif action == "postprint":
                postprint = x.to_list_preorder()
                if x.isempty()==True:
                    print("Empty")
                else:
                    print(' '.join(x.to_list_postorder()))

if __name__ == "__main__":
    driver()
