from sys import argv

class splayNode:
    def __init__(self, x: "comparable"):
        self.key = x
        self.left= None
        self.right= None
        self.parent= None
        
class splayTree:
    class EmptyTree(Exception):
        def __init__(self, data=None):
            super().__init__(data)
            
    class NotFound(Exception):
        def __init__(self, data=None):
            super().__init__(data)
            
    def __init__(self):
        self.root = None

    def splay(self,x):
        while x != self.root:
            if x.parent == self.root:
                if x == x.parent.left:
                    self.right_rotate(x)
                else:
                    self.left_rotate(x)
            else:
                if x == x.parent.left:
                    if x.parent == x.parent.parent.left:
                        self.right_rotate(x)
                        self.right_rotate(x)
                    else:
                        self.right_rotate(x)
                        self.left_rotate(x)
                else:
                    if x.parent == x.parent.parent.right:
                        self.left_rotate(x)
                        self.left_rotate(x)
                    else:
                        self.left_rotate(x)
                        self.right_rotate(x)


    def left_rotate(self,x):
        p = x.parent
        x.parent = p.parent
        if p == self.root:
            self.root = x
        elif p == p.parent.left:
            p.parent.left = x
        else:
            p.parent.right = x
       
        p.right = x.left
        if p.right != None:
            p.right.parent = p
        x.left = p
        p.parent = x

    def right_rotate(self,x):
        p = x.parent
        x.parent = p.parent
        if p == self.root:
            self.root = x
        elif p == p.parent.left:
            p.parent.left = x
        else:
            p.parent.right = x
       
        p.left = x.right
        if p.left != None:
            p.left.parent = p
        x.right = p
        p.parent = x

    def insert(self, key):
        y = None
        x = self.root
        z = splayNode(key)
        while x != None:
            y = x
            if z.key< x.key:
                x = x.left
            else:
                x = x.right

        z.parent= y
        if y == None:
            self.root = z
        elif z.key< y.key:
            y.left= z
        else:
            y.right= z

        self.splay(z)

    def height(self, x): 
        if x == None:
            return 0
        else:
            return max(self.height(x.left), self.height(x.right))+1

    def root_key(self):
        if self.root == None:
            print("Empty")
        else:
            print(self.root.key)

    def search_iterative(self, x, k):
        while x != None and k != x.key:
            z = x
            if k < x.key:
                x = x.left
            else:
                x = x.right
        if x == None:
            self.splay(z)

        return x

    def search(self, x, k):
        z = self.search_iterative(x, k)
        if z == None:
            raise splayTree.NotFound('search({}) not found'.format(k))
        self.splay(z)

    def inorder_helper(self, n, l):
        if n != None:
            self.inorder_helper(n.left, l)
            l.append(n.key)
            self.inorder_helper(n.right, l)

    def to_list_inorder(self):
        l = []
        self.inorder_helper(self.root, l)
        return l

def driver():
    st = splayTree()
    f = open(argv[1], "r")
    nl = int(f.readline().strip())
    for i in range(nl):
        l = f.readline().strip()

        if l == 'root':
            st.root_key()

        elif l == 'height':
            print(st.height(st.root))

        elif l == 'inprint':
            keys = st.to_list_inorder()
            if len(keys) == 0:
                print('Empty')
            else:
                strings = [str(x) for x in keys]
                print(' '.join(strings))

        else:
            v = l.split()
            if v[0] == 'insert':
                k = int(v[1])
                st.insert(k)
            elif v[0] == 'search':
                k = int(v[1])
                try:
                    st.search(st.root, k)
                    print('Found')
                except splayTree.NotFound as e:
                    print('NotFound')

            else:
                print("illegal input line:", 1)



if __name__ == "__main__":
    driver()