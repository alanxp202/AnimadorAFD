import pydot

graphs = pydot.graph_from_dot_file('example.dot')
graph = graphs[0]

print(graph)

graph.write_png('output.png')