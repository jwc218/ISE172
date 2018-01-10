from coinor.gimpy import Graph, UNDIRECTED_GRAPH
from coinor.blimpy import Stack, Queue

class SocialNetwork(Graph):
    def __init__(self, display = None):
        if display is not None:
            Graph.__init__(self, display=display, graph_type = UNDIRECTED_GRAPH, splines = 'true', K = 1.5)
        else:
            Graph.__init__(self, graph_type = UNDIRECTED_GRAPH, splines = 'true', K = 1.5)


    def add_connection(self, name1, name2, label1 = None, label2 = None):
        if self.get_node(name1) is None:
            if label1 is not None:
                self.add_node(name1, label = label1)
            else:
                self.add_node(name1)
        if self.get_node(name2) is None:
            if label2 is not None:
                self.add_node(name2, label = label2)
            else:
                self.add_node(name2)
        # Add if connection does not already exist
        if self.check_edge(name1, name2) is False:
            self.add_edge(name1, name2)

    def add_entity(self, name, label = None):
        if label is not None:
            self.add_node(name, label = label)
        else:
            self.add_node(name)


    def searchConnections(self,actor):
        q = Queue()
        if isinstance(q, Queue):
            addToQ = q.enqueue
            removeFromQ = q.dequeue
        elif isinstance(q, Stack):
            addToQ = q.push
            removeFromQ = q.pop
        visited = {}
        visited [actor] = True
        addToQ(actor)
        while not q.isEmpty():
            current = removeFromQ()
            for n in self.get_neighbors(current):
                if 
                if not n in visited:
                    visited[n] = True
                    addToQ(n)
        return visited
    
    def degrees_of_seperation(self,actor1,actor2):
        q = Queue()
        if isinstance(q, Queue):
            addToQ = q.enqueue
            removeFromQ = q.dequeue
        elif isinstance(q, Stack):
            addToQ = q.push
            removeFromQ = q.pop
        visited = {}
        visited [actor1] = 0
        addToQ(actor1)
        while not q.isEmpty():
            current = removeFromQ()
            for n in self.get_neighbors(current):
                if not n in visited:
                    visited[n] = visited[current]+1
                    addToQ(n)
                if actor2 in visited:
                    return visited[actor2]
                
        return None
        
    def popularity(self,actor):
        count=0
        for n in self.get_neighbors(actor):
            count+=1
        return count
    
    
    def is_connected(self, first, second):
        self.label_components()
        first_component = self.get_node_attr(first, 'component')
        second_component = self.get_node_attr(second, 'component')
        return first_component == second_component

    def make_clusters(self):
        self.label_components()

if __name__ == '__main__':
    sn = SocialNetwork()
    sn.add_connection('a', 'b')
    sn.add_connection('b', 'c')
    sn.add_connection('c', 'd')
    sn.add_connection('b', 'd')
    sn.add_entity('e')
    sn.set_display_mode('pygame')
    sn.display()
    sn.set_display_mode('off')
    print sn.is_connected('a','c')
    print sn.is_connected('c','d')
    print sn.is_connected('a','e')
    print sn.searchConnections('b')
    print sn.degrees_of_seperation('a','c')
    print sn.popularity('d')