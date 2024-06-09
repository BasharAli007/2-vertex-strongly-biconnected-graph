# Collecting the pieces of code and making them compatible is done by #مازن وكيل اسبر 6121
# Uploading the code to Github is done by بشار بديع علي 6152
class Vertex:
    def __init__(self, name):   #محمد صادق جمعه عوض 6375
        self.name = name
        self.dfs_num = -1
        self.state = "new"
        self.comp = -1
    def __str__(self):
        return (
            "Vertex: "
            + str(self.name)
            + " / dfs_num: "
            + str(self.dfs_num)
            + " / State: "
            + self.state
            + " / Component: "
            + str(self.comp)
        )

class Edges:    #مازن وكيل اسبر 6121
    edges = []
    num_of_edges = 0
    @staticmethod
    def new_edge(x, y):
        Edges.edges.append((x, y))
        Edges.num_of_edges += 1

class Stack:       #نمر وائل الحلبي 6542 and بشار بديع علي 6152
    def __init__(self):
        self.a = []

    def push(self, x):
        self.a.append(x)

    def pop(self):
        if len(self.a) == 0:
            return None
        x = self.a[-1]
        self.a = self.a[:-1]
        return x

    def top_value(self):
        if len(self.a) == 0:
            return None
        return self.a[-1]

    def contains(self, x):
        return x in self.a

def cheriyan_mehlhorn_gabow(array, num_of_vertexes):    #علي محمد جديد 6305
    o_stack = Stack()
    r_stack = Stack()
    for v in array:
        if v.state == "new":
            dfs(array, num_of_vertexes, v, o_stack, r_stack)

    return array

def dfs(array, num_of_vertexes, v, o_stack, r_stack): #محمود احمد الأصلان 6318 and إبراهيم خضر جاموس 6369
    v.state = "active"
    v.dfs_num = len(o_stack.a) + 1
    o_stack.push(v)
    r_stack.push(v)
    for i in range(Edges.num_of_edges):
        if Edges.edges[i][0] == v.name:
            w = identify_vertex(array, Edges.edges[i][1])
            if w.state == "new":
                dfs(array, num_of_vertexes, w, o_stack, r_stack)
            elif w.state == "active":
                while w.dfs_num < r_stack.top_value().dfs_num:
                    trash = r_stack.pop()
    v.state = "finish"  #عبدالله زياد العبدالله 6157
    if v == r_stack.top_value() and v.state == "finish":
        trash = r_stack.pop()
        while True:
            w = o_stack.pop()
            w.comp = v.name
            if w == v:
                break

def identify_vertex(arr, name): #حسن زهير داود 4978
    for vertex in arr:
        if vertex.name == name:
            return vertex
    return None

def main(): #عبد العزيز ماهر الصيادي 5950 and أمل عادل عكو 6392
    num_of_vertexes = int(input("How many vertices are in the graph: "))
    vertexes = []
    print("Adjacency Matrix:")
    for i in range(num_of_vertexes):    #علي احمد اسعد 6462
        v = Vertex(i)
        vertexes.append(v)
        row = list(map(int, input().split()))
        for j, value in enumerate(row):
            if value == 1:
                Edges.new_edge(i, j)

    output = cheriyan_mehlhorn_gabow(vertexes, num_of_vertexes)
    for v in output:
        print(v)
    
    is_2_vertex_strongly_biconnected = True #مهند أنيس حسن 6449 and مجد عبدالله جرجب 6651
    for v in vertexes:
        back_neighbors = [w for w in vertexes if w.comp == v.name and w.dfs_num < v.dfs_num]
        if len(back_neighbors) < 2:
            is_2_vertex_strongly_biconnected = False
            break

    if is_2_vertex_strongly_biconnected:
        print("The graph is 2-vertex strongly biconnected.")
    else:
        print("The graph is not 2-vertex strongly biconnected.")

if __name__ == "__main__":
    main()