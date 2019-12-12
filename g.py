class AdjNode:
    def __init__(self,data):
        self.value=data
        self.next=None
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[None]*self.v

    def add_edge(self,src,dest):
        node=AdjNode(dest)
        node.next=self.graph[src]
        self.graph[src]=node

        node=AdjNode(src)
        node.next=self.graph[dest]
        self.graph[dest]=node
    def printGraph(self):
        for i in range(self.v):
            print("Adjancy list of {}\n head".format(i),end="")
            temp=self.graph[i]
            while temp:
                print("-> {}".format(temp.value),end=" ")
                temp=temp.next
            print("\n")
if __name__=="__main__":
    v=5
    graph=Graph(v)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.printGraph()

