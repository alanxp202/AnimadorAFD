import pydot_ng as pydot
import os

#os.environ["PATH"] += os.pathsep + 'C:/Users/alanq/scoop/apps/graphviz/2.44.1/bin'


graphs = pydot.graph_from_dot_file('example.dot')
graph = graphs[0]

print(graph)

graph.write_png('output.png')