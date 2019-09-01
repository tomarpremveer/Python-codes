from collections import defaultdict

class Graph:

    def __init__(self,V):
        self.V=V
        self.adj=[[] for i in range(V)]

    def addEdge(self,u,v):
        self.adj[u].append(v)

    def Bfs(self,s,V):
        visited=[False]*(V+1)
        level=[0]*(V+1)

        queue=[]
        queue.append(s)
        visited[s]=True
        level[s]=0

        while queue:
            s=queue.pop(0)

            for i in self.adj[s]:
                if visited[i]==False:
                    level[i]= level[s]+1
                    queue.append(i)
                    visited[i]=True
        count=0
        for i in range(0,len(self.adj)):
            if level[i]!=0:
                print(6*level[i])

    def DFSUtil(self,v,visited):
        visited[v]=True
        print(v)

        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
    def DFS(self,v):
        visited=[False]*(len(self.graph))

        self.DFSUtil(v,visited)
if __name__=="__main__":
    g=Graph(6)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(2,5)
    g.addEdge(3,6)
    print("the bfs traversal of the graph is")
    print(g.Bfs(0,6))
    #print("the dfs traversal of the graph is")
    #g.DFS(2)