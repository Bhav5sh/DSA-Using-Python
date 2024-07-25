class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list={i:[] for i in range(vno)}
        
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print('Invalid vertices')
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u]=[(vertex,weight) for vertex, weight in self.adj_list[u] if vertex!=v]
            self.adj_list[v]=[(vertex,weight) for vertex, weight in self.adj_list[v] if vertex!=u]
        else:
            print('Invalid vertices')
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex==v for vertex, _ in self.adj_list[u])             # for vertex,weight in self.adj_list[u]:
        else:                                                                      #   if vertex==v: 
            print('Invalid vertices')                                                   # return True
            return False                                                                    # return False                                                                                                                                                                 
    def print_adj_list(self):
        for vertex,n in self.adj_list.items():
            print('V',vertex ,':',n)


G=Graph(5)
G.add_edge(0,1)
G.add_edge(2,3)
G.add_edge(1,3)
G.add_edge(3,4)
G.add_edge(4,1)
G.add_edge(4,0)
G.add_edge(2,4)
print(G.has_edge(0,2))
print(G.has_edge(1,4))
G.print_adj_list()