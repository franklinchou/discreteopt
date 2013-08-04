class Node(object):
    def __init__(self, lvl, val, wt, contains):
        self.lvl = lvl
        self.val = val        
        self.wt = wt                         
        self.contains = contains
    
    # v is a list given by a parent node
    def copyList(self, v):
        if not v:
            self.contains = list()
            # should assert that the list pointed to by v should _not_
            # reference the same address of the list pointed to by contains
            # i.e. the list has been COPIED, not just pointer reassignment
            assert(id(v) != id(self.contains))
        else:
            # construct a new list 
            # note the [] construct has been avoided here
            self.contains = list(v);

    # ommission of add function, as function operates on python list

def solveIt(inputData):   
    # define some globals:
    global values       
    global weights
    global items        # total items to be evaluated
    global Capacity     # capacity of the knapsack

    # Modify this code to run your optimization algorithm
    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
  
    Capacity = int(firstLine[1])
    values = []
    weights = []

    # list where best map is stored
    best = []    

    # data must be ordered by val/wt ratio:
    presorted = list()
    postsorted = list()

    # can this be optimized for python??
    for i in range(1, items+1):
        parts = lines[i].split()
        values.append(int(parts[0]))
        weights.append(int(parts[1]))

        # for readability the following line has been
        # extracted from its own loop and added here
        presorted.append([i - 1, float(parts[0])/float(parts[1])])

    # sort
    postsorted = sorted(presorted, key = lambda x: x[1], reverse = True)

    for i, item in enumerate(presorted):
        postsorted[i][1] = i

    print(postsorted)

    # branchbound method
    maximumVal = 0

    # make and insert root node:
    root = Node(-1, 0, 0, [])
    q = []
    q.append(root)

    # reclaim unused variables:
    del inputData
    del firstLine
    del parts
    del i
    del lines

    # prematurely terminate if the script runs longer than 5 hours (18000 sec)
    start = time.time()
    while q:
        if time.time() >= start + 18000:
            print('algorithm has overflowed execution time. terminating...')
            exit(0)
        # get next item on queue
        p = q.pop()
        if calcBound(p) > maximumVal and p.lvl < items - 1:
            # current node with next item added
            klvl = p.lvl + 1
            
            kwt = p.wt + weights[klvl]
            kval = p.val + values[klvl]

            if kwt <= Capacity:
                if kval > maximumVal:              
                    maximumVal = kval

                k = Node(klvl, kval, kwt, [])
                k.copyList(p.contains)
                k.contains.append(klvl)
                best = list(k.contains)

                # if node is promising accept the node and add to the queue
                if calcBound(k) > maximumVal:
                    q.append(k)

            # node without next item added
            k = Node(klvl, p.val, p.wt, [])            
            if calcBound(k) > maximumVal:
                k.copyList(p.contains)
                k.contains.append(klvl)
                q.append(k)             

    # benchmark
    print('job completed in %.2fs' % (time.time() - start))

    print(best)
    
    # prepare the solution in the specified output format
    
    return maximumVal

# calculate the best possible solution using a greedy algorithm
# uses : linear relaxation of the weight constraint
def calcBound(node):
    if node.wt >= Capacity :
        return 0
    else :
        upperValBnd = node.val
        totalWt = node.wt
        n = node.lvl + 1
        while n < items and totalWt + weights[n] <= Capacity:
            upperValBnd = values[n] + upperValBnd
            totalWt = weights[n] + totalWt
            n = n + 1
        if n < items:
            upperValBnd = upperValBnd + (Capacity - totalWt)\
                * (float(values[n])/(weights[n]))
    return upperValBnd

# main
import sys
import Queue

# benchmark
import time

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)

    else:
        print 'This test requires an input file.  Please select one from the'\
        'data directory. (i.e. python solver.py ./data/ks_4_0)'
