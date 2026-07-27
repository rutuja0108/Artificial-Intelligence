from collections import deque

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}

visited = set()
queue = deque()

start = 0

visited.add(start)
queue.append(start)

print("Initial Queue:", list(queue))
print("Visited:", visited)
print()

while queue:
    node = queue.popleft()

    print("Removed:", node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    print("Queue:", list(queue))
    print("Visited:", visited)
    print()
