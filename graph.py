import random
#节点名称
node_name = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#构造一个有向图
def build_graph(n, neighbor):
    #n最大起始节点个数
    #neighbor最大出度个数
    #存储图结构
    graph = dict()
    #存储起始节点
    start = set()
    for i in range(n):
        node = random.choice(node_name)
        if node not in start:
            start.add(node)
        if node not in graph:
            graph[node] = list()
        for j in range(neighbor):
            target = random.choice(node_name)
            if target != node and target not in graph[node]:
                graph[node].append(target)
    nodes = []
    rela = 0
    for i in graph.keys():
        nodes.extend(graph[i])
        rela += len(graph[i])
        nodes.extend(list(graph.keys()))
    nodes = list(set(nodes))
    print("Build graph success: %d nodes, %d edges." % (len(nodes), rela))
    return graph