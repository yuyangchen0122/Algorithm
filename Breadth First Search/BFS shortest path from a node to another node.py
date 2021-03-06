graph = {
	"A": ["B","C"],
	"B": ["A","C","D"],
	"C": ["A","B","D","E"],
	"D": ["B","C","E","F"],
	"E": ["C","D"],
	"F": ["D"]
}

def BFS(graph, starting):
	queue = []
	queue.append(starting)
	seen = set()
	seen.add(starting)
	parent = {starting: None}

	while (len(queue) > 0):
		vertex = queue.pop(0)
		neighbor_nodes = graph[vertex]
		for node in neighbor_nodes:
			if node not in seen:
				queue.append(node)
				seen.add(node)
				parent[node] = vertex
	return parent

parent = BFS(graph, "A")

v = 'E'
while v != None:
	print(v)
	v = parent[v]