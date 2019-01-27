graph = {
	"A": ["B","C"],
	"B": ["A","C","D"],
	"C": ["A","B","D","E"],
	"D": ["B","C","E","F"],
	"E": ["C","D"],
	"F": ["D"]
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