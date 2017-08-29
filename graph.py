class Graph:
    def __init__(self, edge_list=[], vert_list=[], directed=False):
        self.vert_list = {}
        self.num_vert = 0
        self.directed = directed
        if len(edge_list) != 0:
            self.add_edges(edge_list)
        else:
            self.add_verts(vert_list)

    def add_edge(self, frm, to, wt=1):
        if self.directed:
            if frm not in self.vert_list:
                self.vert_list[frm] = {to: wt}
                self.num_vert += 1
            else:
                self.vert_list[frm][to] = wt

            if to not in self.vert_list:
                self.vert_list[to] = {}
                self.num_vert += 1

        else:
            if frm not in self.vert_list:
                self.vert_list[frm] = {to: wt}
                self.num_vert += 1
            else:
                self.vert_list[frm][to] = wt

            if to not in self.vert_list:
                self.vert_list[to] = {frm: wt}
                self.num_vert += 1
            else:
                self.vert_list[to][frm] = wt

    def add_edges(self, edge_list=[]):
        if len(edge_list) == 0:
            raise "add_edges format is [(a,b,2),...]"
        else:
            if len(edge_list[0]) == 2:
                for tupl in edge_list:
                    self.add_edge(tupl[0], tupl[1])
            elif len(edge_list[0]) == 3:
                for tupl in edge_list:
                    self.add_edge(tupl[0], tupl[1], tupl[2])
            else:
                raise "Edge Tuple Size Can be only 2(for unDWeighted) & 3(for Weighted)"

    def add_vert(self, vert):
        if vert in self.vert_list:
            print "Vertex Already Exist ignoring Operation"
        else:
            self.vert_list[vert] = {}
            self.num_vert += 1

    def add_verts(self, vertL=[]):
        for vert in vertL:
            self.add_vert(vert)

    def show(self):
        is_dir = "Directed" if self.directed else "unDirected"
        print self.vert_list
        print "Number of Vertices in Graph:", self.num_vert, ",Type of Graph:", is_dir


if __name__ == "__main__":
    G = Graph([(1, 2), (2, 3), (4, 5)])
    G.show()
    G.add_edges([(4, 6)])
    G.show()

    Graph_ = Graph([('a', 'b'), ('b', 'c'), ('d', 'e')])
    Graph_.show()
