'''
Created on April 1, 2014

@author: Ted Ralphs
'''
from coinor.gimpy import Graph 
from coinor.gimpy import UNDIRECTED_GRAPH as UNDIRECTED_NETWORK
#from coinor.blimpy import PriorityQueue
from priority_queue import PriorityQueue




import doctest

class Network(Graph):
    
    def shortest_path(self,source, destination = None, q = None):
        '''
        API: shortest_path(self, source, destination = None, display = None)
        Description:
        Generic implementation of Dijkstra's Algorithm.
        if destination is not specified:
           This method determines all nodes reachable from "source" ie. creates
           precedence tree and returns it (dictionary).
        if destination is given:
           If there exists a path from "source" to "destination" it will return
           list of the nodes is a shortest path. If there is no such path, it will
           return the precedence tree constructed from source (dictionary).
        Input:
            source: Search starts from node with this name.
            destination: Destination node name.
        Return:
            Returns predecessor tree in dictionary form if destination is
            not specified, returns list of node names in the path from source
            to destination if destination is specified and there is a path.
            If there is no path returns predecessor tree in dictionary form.
            See description section.

        Unit Test:
        >>> G = Network(type = UNDIRECTED_NETWORK, splines = 'true', K = 1.5, display = 'off')
        >>> G.random(numnodes = 7, density = 0.7, Euclidean = True, seedInput = 9)
        >>> print G.shortest_path(0)
        {1: 4, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        '''


# example how to modify some attribute for node
#        neighbors = self.neighbors
#        for i in self.get_node_list():
#            self.get_node(i).set_attr('label', '-')
#            self.get_node(i).set_attr('distance', 0)
        q= PriorityQueue()
        s= PriorityQueue()
        for j in self.get_node_list():
            q.push(j,float('inf'))
        q.push(source,0)
        while not q.isEmpty():
            current=q.peek()
            value= q.get_priority(current)
            q.remove(current)
            s.push(current,value)
            for i in self.get_neighbors(current):
                if i in q.aList:
                    temp = value +self.get_edge_attr(current,i,'cost')
#                 if temp<q.get_priority(i):
#                     q.push(i,temp)
                    q.push(i,min(temp,q.get_priority(i)))
                if i is destination:
                    break

        return q.aList,s.aList
                
            
            
  
       
if __name__ == '__main__':
    #doctest.testmod()
    G = Network(type = UNDIRECTED_NETWORK, splines = 'true', K = 1.5)
    G.random(numnodes = 7, density = 0.7, Euclidean = False, seedInput = 9)
#    G.set_display_mode('xdot')
#    G. display()
    print G.shortest_path(0)
    
