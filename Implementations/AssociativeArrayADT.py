import sys
from enum import Enum
"""
Uses a red black tree to create a associative array abstract data type

"""

class Color(Enum):
    RED = 1
    BLACK = 2

class RBNode:
    def __init__(self, x: "comparable", t_dot_nil, other=1):
        self.key= x
        self.other = 1
        self.color = Color.RED
        self.left= t_dot_nil
        self.right= t_dot_nil
        self.parent= t_dot_nil
        
class RBTree:
    class EmptyTree(Exception):
        def __init__(self, data=None):
            super().__init__(data)
            
    class NotFound(Exception):
        def __init__(self, data=None):
            super().__init__(data)
            
    def __init__(self):
        self.root= self.nil = RBNode(None, None)
        self.nil.color = Color.BLACK

    def left_rotate(self,x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
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
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x==x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y
 
    def rb_insert_fixup(self,z):
        while z.parent.color== Color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z==z.parent.right:
                        z=z.parent
                        self.left_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color =Color.RED
                    self.left_rotate(z.parent.parent)
        self.root.color = Color.BLACK

    def insert(self, z):
        s = self.search_iterative(self.root, z.key)
        if s != self.nil:
            s.other +=1
            return
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key< x.key:
                x = x.left
            else:
                x = x.right
        z.parent= y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = z.right = self.nil
        z.color = Color.RED
        self.rb_insert_fixup(z)

    def rb_transplant(self,u,v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
            
        v.parent = u.parent

    def rb_delete(self,x):
        z = self.search_iterative(self.root, x)
        if z == self.nil:
            raise RBTree.NotFound('delete() cannot find element')
        y = z
        y_og_color = y.color
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z,z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z,z.left)
        else:
            y=self.rb_minimum(z.right)
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
        if y_og_color == Color.BLACK:
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x==x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right 
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left 
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = Color.BLACK


    def rb_minimum(self, x):
        if x == self.nil:
            raise RBTree.EmptyTree('minimum() invoked on empty tree')
        while x.left!= self.nil:
            x = x.left
        return x

    def rb_maximum(self, x):
        if x == self.nil:
            raise RBTree.EmptyTree('maximum() invoked on empty tree')
        while x.right!= self.nil:
            x = x.right
        return x
    
    def search_iterative(self, x, k):
        while x != self.nil and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
    
    def search(self, x, k):
        z = self.search_iterative(x, k)
        if z == self.nil:
            raise RBTree.NotFound('search({}) not found'.format(k))
        return z
    def lookup(self, k):
        z = self.search_iterative(self.root, k)
        if z == self.nil:
            return False
        elif z.other ==1:
            self.rb_delete(k)
            return True
        else:
            z.other -= 1
            return Trueß

    def preorder_helper(self, n , l):
        if n != self.nil:
            l.append(n.key)
            self.preorder_helper(n.left, l)
            self.preorder_helper(n.right, l)

    def to_list_preorder(self):
        l = []
        self.preorder_helper(self.root, l)
        return l


    def inorder_helper(self, n, l):
        if n != self.nil:
            self.inorder_helper(n.left, l)
            l.append(n.key)
            self.inorder_helper(n.right, l)

    def to_list_inorder(self):
        l = []
        self.inorder_helper(self.root, l)
        return l

    def postorder_helper(self, n ,l):
        if n!= self.nil:
            self.postorder_helper(n.left, l)
            self.postorder_helper(n.right, l)
            l.append(n.key)

    def to_list_postorder(self):
        l = []
        self.postorder_helper(self.root, l)
        return l


def driver():
    st = RBTree()
    with open(sys.argv[1]) as f:
        m,n = f.readline().strip().split()
        x=f.readline().strip().split()
        y=f.readline().strip().split()
        for i in x:
            z = RBNode(i,None)
            st.insert(z)

        for j in y:
            z = RBNode(j,None)
            value = "YES"
            x = st.lookup(j)
            if x == False:
                value = "NO"
                break
        print (value)

        
            

if __name__ == "__main__":
    driver()
