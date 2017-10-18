# File: bTree.py
#   gist.github.com/samidhtalsania/6659380
#
#======================================================================================
# IMPORTS
import random
import sys
#======================================================================================
# CLASS DECLARATIONS
nullNum = 0
class Node():
    __slots__ = ['parent', 'left', 'right', 'value']
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.left = None
        self.right = None
    def getV(self):
        return self.value
    def getPval(self):
        if self.parent:
            parent = self.parent
            return parent.value

class Tree():
    __slots__ = ['root', 'val','node']

    def __init__(self):
        self.root = None
    def getLeft(self,node):
        return node.left
    def getRight(self,node):
        return node.right
    def getVal(self, node):
        return node.val
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        current.left.parent = current
                        break
                elif val > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        current.right.parent = current
                        break
                else:
                    break
    def search(self, val, node = None):
        if node is None:
            current = self.root
        else:
            current = node

        if current.getV() == val:
            return current
        elif current.getV() < val:
            return self.search(val, current.right)
        elif current.getV() > val:
            return self.search(val, current.left)
        else:
            return None
    def remove(self, val, node = None):
        node = self.search(val)
        if node:
            #Node has no children
            if node.left is None and node.right is None:
                if node == self.root:
                    self.root = None
                elif val < node.getPval():
                    node.parent.left = None
                else:
                    node.parent.right = None
            #Left Child only
            elif node.left and node.right is None:
                if node == self.root:
                    node.left = self.root
                if val < node.getPval():
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            #Right child only
            elif node.left is None and node.right:
                if node == self.root:
                    node.right = self.root
                if val < node.getPval():
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            #Has both children
            elif node.left and node.right:
                min = self.findMin(node.right)
                node.value = min.value
                min.parent.left = None
            else:
                return False
            return True
    def findMin(self, node):
        if node.left:
            return self.findMin(node.left)
        else:
            return node
    def printT(self, node = None):
        if node == None:
            node = self.root
        if node:
            printT(node.left)
            print(node.val)
            printT(node.right)
#======================================================================================
def rWrite(f, node, nullNum):
    if node.left is None:
        f.write("\tnull{} [shape=point];\n".format(nullNum))
        f.write("\t{} -> null{};\n".format(node.value,nullNum))
    else:
        temp = node.left
        f.write("\t{} -> {};\n".format(node.value,temp.value))
        rWrite(f, node.left, nullNum)
    if node.right is None:
        f.write("\tnull{} [shape=point];\n".format(nullNum))
        f.write("\t{} -> null{};\n".format(node.value,nullNum))
    else:
        temp = node.right
        f.write("\t{} -> {};\n".format(node.value,temp.value))
        rWrite(f, node.right, nullNum)
def writeTree(t, f):
    global nullNum
    nullNum = 1
    if t:
        f.write("digraph BST{\n")
        f.write('''\tnode [fontname="Helvetica"];\n''')
        rWrite(f, t.root, nullNum)
        f.write("}")
    
#======================================================================================
def main():
#    if len(sys.argv) < 2:
#       print('Please provide the number of keys to enter.')
#        sys.exit(1)
#    s = int(sys.argv[1])
    s = 8
    parts = int(s/3)
    t = Tree()
    r = list(range(1,s+1))

    print('Randomly inserting the numbers from 1 to {}.'.format(len(r)))

    random.shuffle(r)

    for i in r:
        print('inserted {}'.format(i))
        t.insert(i)
    f = open('a.txt', 'w')
    writeTree(t, f)
    f.flush( )
    f.close( )
    random.shuffle(r)

    for n in range(1, 3):
        m = r[(n-1) * parts : (n * parts)]
        print(len(m))
        for i in m:
            print('removed {}'.format(i))
            v = t.remove(i)
            if v:
                print('\tcompleted.')
            else:
                print('\terror.')
        c = chr(n + 97)
        filename = str(c) + '.txt'
        f = open(filename, 'w')
        writeTree(t, f)
        f.flush( )
        f.close( )

main()
