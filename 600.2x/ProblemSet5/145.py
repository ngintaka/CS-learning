    def DFS(digraph, start, end, path = [], shortest = None):
        start = Node(start)
        end = Node(end)
        path = path + [start]
        
        if start == end and getOutLength(path) <= maxDistOutdoors:
#            print 'path', path, 'Out', getOutLength(path), 'tot', getTotLength(path), 'max', maxTotalDist
            return path

        for node in digraph.childrenOf(start):
            
            
            if node not in path:
                
                
                if shortest == None or getTotLength(path) < shortest:
                    
                    
                    newPath = DFS(digraph,node,end, path, shortest)
                    if getTotLength(newPath) > maxTotalDist:
                        break
                    if newPath != None:
                        shortest = newPath

        if shortest == None: raise ValueError
        shortest = [str(n) for n in shortest]
        return shortest       
