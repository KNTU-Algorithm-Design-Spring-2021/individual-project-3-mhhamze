from collections import defaultdict   
class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = defaultdict(list) 
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def printAllPathsUtil(self, u, d, visited, path):
        visited[u]= True
        path.append(u)
        if u == d:
            print(path)
        else:
            for i in self.graph[u]:
                if visited[i]== False:
                    self.printAllPathsUtil(i, d, visited, path)
        path.pop()
        visited[u]= False
    def printAllPaths(self, s, d):
        visited =[False]*(self.V)
        path = []
        self.printAllPathsUtil(s, d, visited, path)

if __name__ == "__main__":   
    start = 1
    number = 1
    f = open("input.txt")
    while True:
        g = Graph(22)
        line = str(f.readline()).removeprefix("\n")
        if  line == "":
            break
        end = int(line)
        while True:
            edge = str(f.readline()).removeprefix("\n").split()
            a = int(edge[0])
            b = int(edge[1])
            if a == 0 and b == 0:
                break
            g.addEdge(a,b)
            g.addEdge(b,a)
        print("CASE "+str(number)+":")
        number += 1
        g.printAllPaths(start, end)