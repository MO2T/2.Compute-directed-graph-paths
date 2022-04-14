#graph表示一张图
#start表示起始节点
#target表示终止节点
#cut表示最大路长
def searchpaths(graph, start, target, cut):
    paths = []
    path = []

    def dfs(start, target):
        #如果起始节点不在图中，则结束
        if start not in graph:
            return
        #如果路长大于阈值，则结束
        if len(path) >= cut:
            return
        #遍历起始节点的邻居节点
        for neighbor in graph[start]:
            #如果起始节点没有在单条path出现，则追加
            if neighbor not in path:
                path.append(neighbor)
            #出现环，则结束
            else:
                return
            #如果单条path没有出现在paths里且满足终点等于target，则在结果中追加
            if path not in paths and path[-1] == target:
                #拷贝
                paths.append(path[:])
            #以新的邻居节点dfs
            dfs(neighbor, target)
            #last的追加了neighbor，需要返回
            path.pop()
    path.append(start)
    dfs(start, target)
    return paths
