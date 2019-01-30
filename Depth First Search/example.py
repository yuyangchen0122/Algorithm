graph = {
	"A": ["B","S"],
	"B": ["A"],
	"C": ["D","E","F","S"],
	"D": ["C"],
	"E": ["C","H"],
	"F": ["C","G"],
	"G": ["S","F","H"],
	"H": ["G","E"],
	"S": ["A", "C", "G"]
}

def DFS(graph, starting):
	stack = []
	stack.append(starting)
	seen = set()
	seen.add(starting)
	while (len(stack) > 0):
		vertex = stack.pop()
		neighbor_nodes = graph[vertex]
		for node in neighbor_nodes:
			if node not in seen:
				stack.append(node)
				seen.add(node)
		print(vertex)

DFS(graph, "A")