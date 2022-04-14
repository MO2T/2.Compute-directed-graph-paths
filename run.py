from graph import build_graph
from search import searchpaths
graph = build_graph(9, 5)
#sampleing
start = list(graph.keys())[0]
target = list(graph.keys())[1]
cut = 10
print("compute the paths between node %s and node %s where the length less than %d" %(start, target, cut))
paths = searchpaths(graph, start, target, cut)
print(paths)