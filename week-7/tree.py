#!/usr/bin/env python

class binaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None

    def __str__(self):
        return self.value

    def setLeftBranch(self, node):
        self.leftBranch = node

    def setRightBranch(self, node):
        self.rightBranch = node

    def setParent(self, parent):
        self.parent = parent


def DFSBinary(root, fcn):
    '''Depth first search binary tree.'''
    stack = [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return True
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
    return False


if __name__=="__main__":
    # set nodes
    n5 = binaryTree(5)
    n2 = binaryTree(2)
    n1 = binaryTree(1)
    n4 = binaryTree(4)
    n8 = binaryTree(8)
    n6 = binaryTree(6)
    n7 = binaryTree(7)

    # connect nodes
    n5.setLeftBranch(n2)
    n2.setParent(n5)
    n5.setRightBranch(n8)
    n8.setParent(n5)
    n2.setLeftBranch(n1)
    n1.setParent(n2)
    n2.setRightBranch(n4)
    n4.setParent(n2)
    n8.setLeftBranch(n6)
    n6.setParent(n8)
    n6.setRightBranch(n7)
    n7.setParent(n6)
