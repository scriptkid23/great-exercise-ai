# -*- coding: utf-8 -*-
from AutomaticallyGenerating import AutomaticallyGenerating
# -*- coding: utf-8 -*-
from copy import copy

class Graph(object):

    def __init__(self, graph_dict=None, start = None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        self.start = start
        self.height = 0
        self.step = []
    def vertices(self):
       
        return list(self.__graph_dict.keys())

    def DLS(self,src,target,maxDepth): 
  
        if src == target : return True
  
        # If reached the maximum depth, stop recursing. 
        if maxDepth <= 0 : return False
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.__graph_dict[src]: 
                if(self.DLS(i,target,maxDepth-1)): 
                    self.step.insert(0,i)
                    return True
        return False
   
    def IDDFS(self,src, target, maxDepth): 
      
        # Repeatedly depth-limit search till the 
        # maximum depth 
        for i in range(maxDepth): 
            if (self.DLS(src, target, i)): 
                return True
        return False
    def child(self,vertice):
     
        return self.__graph_dict[vertice]

    def parent(self,vertice):
        for key, value in self.__graph_dict.items(): 
         if vertice in value: 
             return key 

    def deep(self,vertex_):

        if ( vertex_ == self.start):
            
            return self.height
        else:
         
            for i in self.__graph_dict:
                if vertex_ in self.child(i):
                    self.height = self.height + 1
                    self.deep(i)
                    return self.height



initialState = [[3,2,1],[],[]]
goal = [[],[],[3,2,1]]
number_of_discs = 3 

g = AutomaticallyGenerating(initialState)
g.process(g.node)
graph = Graph(g.get_graph(),'A1')
temp = {k:v for k, v in g.get_defined().items() if v == goal}

print(g.get_graph())
print(g.get_defined())
step = []
graph.IDDFS('A1',list(temp.keys())[0],2**number_of_discs)
graph.step.insert(0,'A1')
for i in graph.step:
    step.append(g.get_defined()[i])
print(step)