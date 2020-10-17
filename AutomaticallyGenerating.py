#Copyright by NuceTeam 
from copy import deepcopy

class Node:
    def __init__(self):
        self.state=[[],[],[]]
        self.nodeNumber=0
        self.parent=None
        self.children=[]



class AutomaticallyGenerating:
    def __init__(self,initialState):
        self.initialState_ = initialState
        self.states = [initialState]
        self.nodenumber = 1
        self.flag=False
        self.node=Node()
        self.node.state=initialState
        self.node.nodeNumber= self.nodenumber
        self.parentList=[self.node]
        self.childList=[]
        self.pegs = 3
        self.step=1
        self.defined = {}
        self.g = {}
        

    def move(self,st1,st2):
        s1=st1[:]
        s2=st2[:]

        if len(s1)>0:
            topDisc=s1[len(s1)-1]
            lastofS2=len(s2)-1

            if len(s2)==0 or s2[lastofS2]>topDisc:
                s2.append(topDisc)
                s1.pop()

                return s1,s2
            else:
                return None
        else:
            return None    

    def moveDisc(self,n):
        stacks=[]
        for x in range(0,self.pegs):
            for y in range(0,self.pegs):

                stacks=self.move(n.state[x],n.state[y])

                if stacks!=None:
                    nextnode=Node()
                    nextnode=deepcopy(n)
                    nextnode.state[x]=deepcopy(stacks[0])
                    nextnode.state[y]=deepcopy(stacks[1])
                    if nextnode.state  in self.states:
                        continue
                    else:
                        self.states.append(nextnode.state)
                        return nextnode
        return None
    
    def process(self,node):
      

        self.step+=1

        for node in self.parentList:
            if self.flag==False :
                self.defined["A{}".format(node.nodeNumber)] = node.state
                exhausted=False
                parent=deepcopy(node)
                temp = []
                self.g["A{}".format(node.nodeNumber)] = []
                while exhausted==False :
                    
                    self.childnode=self.moveDisc(node)
                   
                    if self.childnode!=None:
                        self.nodenumber+=1
                        self.childnode.nodeNumber=self.nodenumber
                        self.childnode.parent=node
                        parent.children.append(self.childnode)
                        self.childList.append(self.childnode)
                        temp.append("A{}".format(self.childnode.nodeNumber))
                        self.g["A{}".format(node.nodeNumber)] = temp

                    else:
                        
                        exhausted=True
        self.parentList=deepcopy(self.childList)
        self.childList=[]
       
        if self.flag==False :
            if(self.step == (2**len(self.initialState_[0]) + 1)):
                return 
            else:

                self.process(self.parentList)
        
    def get_graph(self):
        return self.g

    def get_defined(self):
        return self.defined
