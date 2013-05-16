import tempfile
import unittest
import os
import operator
import binarySearchTree
import splayTree
import optimalBinarySearchTree

class Testing(unittest.TestCase):
    #setUp------------------------------------------
    def setUp(self):
        self.splayTree = splayTree.SplayTree()
        self.optimalBinarySearchTree = None
        self.binarySearchTree = binarySearchTree.BinarySearchTree()
    #tests----------------------------------------
    def testBinarySearchTree(self):
        self.binarySearchTree.insert(1)
        self.binarySearchTree.insert(4)
        self.binarySearchTree.insert(2)
        self.binarySearchTree.insert(8)
        self.binarySearchTree.insert(1)
        self.assertEquals(self.binarySearchTree.maximum(),8)
        self.assertEquals(self.binarySearchTree.minimum(),1)
        self.binarySearchTree.insert(12)
        self.assertEquals(self.binarySearchTree.maximum(),12)
        self.binarySearchTree.insert(-6)
        self.binarySearchTree.insert(-14)
        self.assertEquals(self.binarySearchTree.minimum(),-14)
    def testSplayTree(self):
        self.splayTree.insert(1)
        self.splayTree.insert(4)
        self.splayTree.insert(2)
        self.splayTree.insert(8)
        self.splayTree.insert(1)
        self.assertEquals(self.splayTree.root.val,1)
        self.splayTree.find(8)
        self.assertEquals(self.splayTree.root.val,8)
        self.splayTree.find(2)
        self.splayTree.find(2)
        self.assertEquals(self.splayTree.root.val,2)
    def testOptimalBinarySearchTree0(self):
        numberOfAccessesDictionary = {1:1,2:3,3:5,4:2,5:3,6:1}
        self.optimalBinarySearchTree = optimalBinarySearchTree.OptimalBinarySearchTree(numberOfAccessesDictionary)
        self.assertEquals(self.optimalBinarySearchTree._root[2], 2)
        self.assertEquals(self.optimalBinarySearchTree._root[0][2], 1)
        self.assertEquals(self.optimalBinarySearchTree._root[0][0][2], 0)
        self.assertEquals(self.optimalBinarySearchTree._root[1][2], 4)
        self.assertEquals(self.optimalBinarySearchTree._root[1][1][2], 5)
        self.assertEquals(self.optimalBinarySearchTree._root[1][0][2], 3)
    def testOptimalBinarySearchTree1(self):
        numberOfAccessesDictionary = {1:30,2:5,3:8,4:45,5:12}
        self.optimalBinarySearchTree = optimalBinarySearchTree.OptimalBinarySearchTree(numberOfAccessesDictionary)
        self.assertEquals(self.optimalBinarySearchTree._root[2], 3)
        self.assertEquals(self.optimalBinarySearchTree._root[0][2], 0)
        self.assertEquals(self.optimalBinarySearchTree._root[0][1][2], 2)
        self.assertEquals(self.optimalBinarySearchTree._root[0][1][0][2], 1)
        self.assertEquals(self.optimalBinarySearchTree._root[1][2], 4)

if __name__ == "__main__":
    unittest.main()