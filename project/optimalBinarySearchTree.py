import binarySearchTree
import numpy

class OptimalBinarySearchTree(binarySearchTree.BinarySearchTree):
    def __init__(self, accessFrequenciesDictionary, sort_key = None):
        super(OptimalBinarySearchTree, self).__init__(sort_key)
        self.accessFrequencies = list(sorted(accessFrequenciesDictionary.iteritems()))
        #use dynamic programming to find the optimal binary search tree
        #dynamic programming will work because a optimal binary search tree consists of
        #root and two smaller optimal binary search trees
        self.dynamicProgrammingMatrix = numpy.zeros(shape = (len(self.accessFrequencies),len(self.accessFrequencies)))
        self.treeRootsMatrix = numpy.zeros(shape = (len(self.accessFrequencies),len(self.accessFrequencies)))
            
        matrixDiagonal = numpy.zeros(shape = (len(self.accessFrequencies),2))
        for i in range(len(matrixDiagonal)):
            matrixDiagonal[i] = [i,i]
        #move along diagonal lines in the matrix, since cost 
        #function depends on element to the left and element below
        for i in range(len(self.dynamicProgrammingMatrix)):
            for ele in matrixDiagonal:
                if(ele[1] < len(self.dynamicProgrammingMatrix)):
                    self.dynamicProgrammingMatrix[ele[0]][ele[1]] = self.findTotalCost(ele[0],ele[1])
                ele[1] += 1
        """print "dyn prog "
        print str(self.dynamicProgrammingMatrix)
        print "root "
        print str(self.treeRootsMatrix)
        print "matr d "+str(matrixDiagonal)
        """
        for d in self.determineTreeList():
            self.insert(d)
    def recursiveDetermineTreeList(self,left,right,list):
        indexRoot = int(self.treeRootsMatrix[left][right])
        list.append(indexRoot)
        if(indexRoot < right):
            list = self.recursiveDetermineTreeList(indexRoot+1,right,list)
        if(indexRoot > left):
            list = self.recursiveDetermineTreeList(left,indexRoot-1,list)
        return list
    #make a list that is a permutation of the elements that are accessed in order from 1st to last to
    #be put into the tree
    def determineTreeList(self):
        return self.recursiveDetermineTreeList(0,len(self.accessFrequencies)-1,[])
    def findTotalCost(self,left,right):
        cost = self.costFunction(left,right)
        x = 0
        y = 0
        if(left-1 < len(self.dynamicProgrammingMatrix)):
            x = self.dynamicProgrammingMatrix[left][left-1]
        if(left+1 < len(self.dynamicProgrammingMatrix)):
            y = self.dynamicProgrammingMatrix[left+1][right]
        minimalIndex = left
        minimalCost = x + y
        for n in range(int(left),int(right+1)):
            x = 0
            y = 0
            if(n-1 < len(self.dynamicProgrammingMatrix)):
                x = self.dynamicProgrammingMatrix[left][n-1]
            if(n+1 < len(self.dynamicProgrammingMatrix)):
                y = self.dynamicProgrammingMatrix[n+1][right]
            c = x + y
            if(c < minimalCost):
                minimalCost = c
                minimalIndex = n
        self.treeRootsMatrix[left][right] = minimalIndex
        return cost + minimalCost
    def costFunction(self,left,right):
        right = int(right)
        left = int(left)
        if(left < 0 or right < 0 or left > right or left > self.accessFrequencies.__len__() - 1 or right > self.accessFrequencies.__len__() - 1):
            return 0
        else:
            cost = 0
            for x in range(left,right+1):
                cost += self.accessFrequencies[x][1]
            return cost