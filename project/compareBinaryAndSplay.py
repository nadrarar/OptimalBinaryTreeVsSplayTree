import optimalBinarySearchTree
import splayTree
import sys
import time
import math
import random
from collections import Counter
def accessesList(function,accessNumber = 10):
    l = []
    for i in range(accessNumber):
        l.append(function(i))
    return l
#sine test - entries in sequence, repeated multiple times
def testSine(accesses,wavePeriod=20):
    print "test sine, with wave period of "+str(wavePeriod)+":"
    def fSine(input):
        return int(1000*math.sin(input*math.pi/wavePeriod))
    dataTest(accessesList(fSine,accesses))
#every entry is different
def testLinear(accesses):
    print "test linear:"
    def fLinear(input): 
        return int(input)
    dataTest(accessesList(fLinear,accesses))
#only 1 entry
def testConstantValue(accesses, constant = 50):
    print "test constant value of " + str(constant) + ":"
    def fConstantValue(input):
        return constant
    dataTest(accessesList(fConstantValue,accesses))
#random values between 0 and the maxValue
def testRandom(accesses, maxValue = 100,seed = 1000):
    print "test random max value = " + str(maxValue) + ":"
    random.seed(seed)
    def fRandom(input):
        return random.randint(0,maxValue)
    dataTest(accessesList(fRandom,accesses))
#gaussian random
def testGaussian(accesses, variance = .1, maxValue = 100, seed = 1000):
    print "test gaussian random max value = " + str(maxValue) +" and a variance = "+str(variance)+ ":"
    random.seed(seed)
    def fGaussian(input):
        return int(maxValue*random.gauss(0,variance))
    dataTest(accessesList(fGaussian,accesses))

#longer cycles between 100 different values, ie is 1 for 20 accesses, then 2 for 20 accesses, 3,...100,1,2...
#deltaAccessesPerValue edits AccessesPerValue, so that the cycles get longer or
#shorter.  For example, if maxAccessesPerValue = 20, deltaAccessesPerValue = -1, 1 for 
#20 accesses, 2 for 19 accesses, 3 for 18 accesses...
def testProgression(accesses, maxValue = 100, maxAccessesPerValue = 20, deltaAccessesPerValue = 0):
    print "test progression, max value = " + str(maxValue) + "maxAccessesPerValue = "+str(maxAccessesPerValue) + "deltaAccessesPerValue = "+str(deltaAccessesPerValue) +":"
    accessesPerValue = int(maxAccessesPerValue)
    deltaAccessesPerValue = int(accessesPerValue)
    l = []
    for i in range(accesses):
        if(int(i)%accessesPerValue):
            accessesPerValue += deltaAccessesPerValue
            if(accessesPerValue<=0):
                accessesPerValue = maxAccessesPerValue
        val = int(i)/int(accessesPerValue)
        l.append(val)
    dataTest(l)
def dataTest(accesses):
    splayTreeTime = splayTest(accesses)
    optimalTreeTime = optimalTest(accesses)
    splayTreeTimeTotal = splayTreeTime[2] - splayTreeTime[0]
    optimalTreeTimeTotal = optimalTreeTime[2] - optimalTreeTime[0]
    if(splayTreeTimeTotal > optimalTreeTimeTotal):
        print "Optimal tree is faster."
    else:
        print "Splay tree is faster."
def splayTest(accesses):
    print "  splay tree:"
    initialize = time.clock()
    testSplayTree = splayTree.SplayTree()
    frequencies = Counter(accesses)
    for e in frequencies.iteritems():
        testSplayTree.insert(e[0])
    startAccessing = time.clock()
    for a in accesses:
        testSplayTree.find(a)
    completeAccessing = time.clock()
    print "    insert all items: "+str(startAccessing - initialize)
    print "    access: "+str(completeAccessing - startAccessing)
    print "    combined: "+str(completeAccessing - initialize)
    return [initialize,startAccessing,completeAccessing]
def optimalTest(accesses):
    print "  optimalTree:"
    initialize = time.clock()
    frequencies = Counter(accesses)
    optimalTree = optimalBinarySearchTree.OptimalBinarySearchTree(frequencies)
    startAccessing = time.clock()
    for a in accesses:
        optimalTree.find(a)
    completeAccessing = time.clock()
    print "    insert all items: "+str(startAccessing - initialize)
    print "    access: "+str(completeAccessing - startAccessing)
    print "    combined: "+str(completeAccessing - initialize)
    return [initialize,startAccessing,completeAccessing]
if(__name__ == "__main__"):
    if(len(sys.argv) >= 1):
        timeScale = 1
        if(len(sys.argv) > 1):
            timeScale = int(sys.argv[2])
        testSine(100000*timeScale,20)
        testSine(100000*timeScale,150)
        #can't go any higher for linear, because of the time it takes to construct optimal tree
        testLinear(120*timeScale)
        testConstantValue(10000*timeScale)
        testRandom(10000*timeScale,20)
        testRandom(10000*timeScale,140)
        testGaussian(10000*timeScale,.1,100)
        testGaussian(10000*timeScale,.5,100)
        testProgression(40000*timeScale,100,90)
        testProgression(40000*timeScale,100,90,-5)
        testProgression(40000*timeScale,100,200,-20)
        testProgression(40000*timeScale,100,90,9)
    else:
        print "error, did not give path to input file"

