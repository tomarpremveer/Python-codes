from collections import defaultdict
class Graph(object):
    def __init__(self,V):
        self.V=V
        self.graph=defaultdict(list)
    def connect(self,u,v):
        self.graph[u].append(v)
    def find_all_distances(self,s):
        ro=s
        Visited=[False]*(self.V)
        level=[0]*(self.V)
        level[s]=0
        Visited[s]=True
        q=[]
        q.append(s)
        while q:
            s=q.pop(0)
            for i in self.graph[s]:
                if Visited[i]==False:
                    Visited[i] = True
                    level[i]=level[s]+1
                    q.append(i)
        for a in range(0,(self.V)):
            if a==ro:
                continue
            if level[a]!=0 and a!=ro:
                print(6*level[i],end=" ")
            else:
                print(-1,end=" " )
        print()
if __name__=="__main__":
    n,m = 4,2
    graph = Graph(n)
    graph.connect(0,1)
    graph.connect(0,2)
    #graph.connect(2,3)
    #graph.connect(1,4)
    s = 1
    graph.find_all_distances(s-1)

