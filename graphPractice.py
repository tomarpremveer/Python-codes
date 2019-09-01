class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)


def countPath(self, u, d):
    visited = [False] * self.V
    pathCount = [0]
    self.countPathUtil(u, d, visited, pathCount)
    return pathCount[0]


def countPathUtil(self, u, d, visited, pathCount):
    visited[u] = True

    if u == d:
        pathCount[0] += 1

    else:
        i = 0
        while i < len(self.adj[u]):
            if (not visited[self.adj[u][i]]):
                self.countPathUtil(self.adj[u][i], d, visited, pathCount)
            i += 1
    visited[u] = False


if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    s = 2
    d = 3
    print(g.countPath(s, d))
