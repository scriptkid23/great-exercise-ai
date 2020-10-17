# -*- coding: utf-8 -*-
from AutomaticallyGenerating import AutomaticallyGenerating
class Graph(object):

    def __init__(self, graph_dict=None, start = None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        self.start = start
        self.height = 0
    def vertices(self):
       
        return list(self.__graph_dict.keys())

    def edges(self):
      
        return self.__generate_edges()

    def child(self,vertice):
     
        return self.__graph_dict[vertice]

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def deep(self,vertex_):
        if ( vertex_ == self.start):
            return self.height
        else:
         
            for i in self.__graph_dict:
                if vertex_ in self.child(i):
                    self.height = self.height + 1
                    self.deep(i)
                    return self.height

def get(open):
    return open.pop(0)
def depthwise_search(graph:Graph, src:str, dest:[] , h:int):
    Open  = [src]
    Close = []
    DS    = h 
    result = []
    while len(Open) != 0:
        S = get(Open)
        Close.append(S)
        result.append(S)
        if( S in dest ):
            
            return result
        if (len(graph.child(S)) != 0 and (graph.child(S) not in Open and Close)):
            dS  = graph.deep(S)
            if(dS >= 0 or dS <= DS - 1):
                for i in graph.child(S):
                    Open.insert(0,i)
            if(dS == DS):
                for i in graph.child(S):
                    Open.append(i)
            if(dS == DS + 1):
                DS = DS + h
                if( h == 1):
                    for i in graph.child(S):
                        Open.append(i)
                else:
                    for i in graph.child(S):
                        Open.insert(0,i)

    return False

g = AutomaticallyGenerating([[3,2,1],[],[]])
g.process(g.node)
graph = Graph(g.get_graph(),'A1')
temp = {k:v for k, v in g.get_defined().items() if v == [[],[],[3,2,1]]}

step = []
for i in depthwise_search(graph,'A1',[list(temp.keys())[0]],2):
    step.append(g.get_defined()[i])
print(step)