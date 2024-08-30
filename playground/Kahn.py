"""
@title:      Kahn’s algorithm
@difficulty: 中等
@importance: 6/5
@tags:       拓扑排序
"""

"""
Kahn’s algorithm 是一种拓扑排序的算法实现

从点入手。
统计每个点的入度和出度。循环删除入度为 0 的点。
"""




from collections import defaultdict, deque
def topological_sort(graph):
    # 创建一个字典来记录每个节点的入度
    indegree = defaultdict(int)
    # 创建一个队列来存储入度为0的节点
    queue = deque()

    # 计算每个节点的入度
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    # 将所有入度为0的节点加入队列
    for node in graph:
        if indegree[node] == 0:
            queue.append(node)

    # 用于存储排序结果
    sorted_order = []

    # 按照拓扑顺序处理节点
    while queue:
        node = queue.popleft()
        sorted_order.append(node)

        # 将与当前节点相邻的所有节点的入度减去1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            # 如果某个节点的入度变为0，则将其加入队列
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # 如果排序结果的长度小于图中的节点数，则说明图中存在环
    if len(sorted_order) == len(graph):
        return sorted_order
    else:
        return []


# 示例
if __name__ == "__main__":
    # 构建一个有向无环图
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': [],
    }

    result = topological_sort(graph)
    print("Topological Sort Result:", result)
