from graph import *
from ps5 import *

def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result


def DFS(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS(graph,node,end,path,shortest)
            if newPath != None:
                return newPath

def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(graph,node,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest



def testSP():
    d = load_map('/Users/robflynn/Desktop/mit_map.txt')
    print d.hasNode('32')
    sp = DFSShortest(d, 32, 36)
    print 'Shortest path found by DFS:', printPath(sp)

testSP()

'''
    path = []
    stack = [start]
    while stack != []:
        
        node = Node(stack.pop())
        if node == Node(end):
            path.append(Node(end))
            print path
        
        if node not in path:
            path.append(node)
        for dest in digraph.childrenOf(node): #reversed?
            if dest not in path:
                stack.append(dest)
    print path
#    return path
'''                