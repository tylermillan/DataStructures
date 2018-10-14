from sys import argv

RED = "RED"
BLACK = "BLACK"

class NilNode(object):
    def __init__(self):
        self.color = BLACK

NIL = NilNode()

class RBNode:
    def __init__(self, key, color=RED, left=NIL, right=NIL, parent=NIL):
        assert color in (RED, BLACK)
        self.color = color
        self.key= key
        self.left= left
        self.right= right
        self.parent= parent
        
class RBTree:
    class EmptyTree(Exception):
        def __init__(self, data=None):
            super().__init__(data)
            
    class NotFound(Exception):
        def __init__(self, data=None):
            super().__init__(data)
            
    def __init__(self, root=NIL):
        self.root= root

    def left_rotate(self,x):
        y = x.right
        x.right = y.left
        if y.left != NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == NIL:
            self.root = y
        elif x==x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self,x):
        y = x.left
        x.left = y.right
        if y.right != NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == NIL:
            self.root = y
        elif x==x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
 
    def rb_insert_fixup(self,z):
        while z.parent.color==RED:
            if z.parent ==z.parent.parent.left:
                y = z.parent.parent.right
                if y.color ==RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z==z.parent.right:
                        z=z.parent
                        self.left_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_rotate(z.parent.parent)
        self.root.color = BLACK

    def insert(self, z):
        y = NIL
        x = self.root
        while x != NIL:
            y = x
            if z.key< x.key:
                x = x.left
            else:
                x = x.right
        z.parent= y
        if y == NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = z.right = NIL
        z.color = RED
        self.rb_insert_fixup(z)


    def rb_transplant(self,u,v):
        if u.parent == NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def rb_delete(self,z):
        y = z
        y_og_color = y.color
        if z.left == NIL:
            x = z.right
            self.rb_transplant(z,z.right)
        elif z.right == NIL:
            x = z.left
            self.rb_transplant(z,z.left)
        else:
            y = self.rb_minimum(z.right)
            y_og_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y,y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z,y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_og_color == BLACK:
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x==x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right 
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                elif w.right.color == BLACK:
                    w.left.color = BLACK
                    w.color = RED
                    self.right_rotate(w)
                    w = x.parent.right
                    w.color = x.parent.color
                    x.p.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    w = x.parent.left 
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                elif w.left.color == BLACK:
                    w.right.color = BLACK
                    w.color = RED
                    self.left_rotate(w)
                    w = x.parent.left
                    w.color = x.parent.color
                    x.p.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = BLACK


    def rb_minimum(self, x):
        if x == NIL:
            raise RBTree.EmptyTree('minimum() invoked on empty tree')
        while x.left!= NIL:
            x = x.left
        return x

    def rb_maximum(self, x):
        if x == NIL:
            raise RBTree.EmptyTree('maximum() invoked on empty tree')
        while x.right!= NIL:
            x = x.right
        return x
    
    def search_iterative(self, x, k):
        while x != NIL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
    
    def search(self, x, k):
        z = self.search_iterative(x, k)
        if z == NIL:
            raise RBTree.NotFound('search({}) not found'.format(k))
        return z

    def inorder_helper(self, n, l):
        if n != NIL:
            self.inorder_helper(n.left, l)
            l.append(n.key)
            self.inorder_helper(n.right, l)

    def to_list_inorder(self):
        l = []
        self.inorder_helper(self.root, l)
        return l

def driver():
    st = RBTree()
    f = open(argv[1], "r")
    nl = int(f.readline().strip())
    for i in range(nl):
        l = f.readline().strip()
        if l == 'max':
            try:
                x = st.rb_maximum(st.root)
                print(x.key)
            except RBTree.EmptyTree as e:
                print('Empty')

        elif l == 'min':
            try:
                x = st.rb_minimum(st.root)
                print(x.key)
            except RBTree.EmptyTree as e:
                print('Empty')

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
                z = RBNode(k)
                st.insert(z)
            elif v[0] == 'remove':
                k = int(v[1])
                try:
                    z = st.search(st.root, k)
                    st.rb_delete(z)
                except RBTree.NotFound as e:
                    print('TreeError')
            elif v[0] == 'search':
                k = int(v[1])
                try:
                    z = st.search(st.root, k)
                    print('Found')
                except RBTree.NotFound as e:
                    print('NotFound')



if __name__ == "__main__":
    driver()