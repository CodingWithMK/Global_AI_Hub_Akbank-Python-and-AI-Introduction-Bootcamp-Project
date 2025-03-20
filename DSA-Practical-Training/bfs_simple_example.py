'''
Breadth First Search Graph Traversal
'''

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": [],
    "F": []
}

def bfs(graph, source):
    queue = []
    queue.append(source)
    while queue:
        current = queue.pop(0)
        print(current)
        for node in graph[current]:
            queue.append(node)

bfs(graph, "A")


def BFS(root):
    queue = []
    queue.append(root)

    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)