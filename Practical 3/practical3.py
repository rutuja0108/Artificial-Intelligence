graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}

visited = set()
stack = []
stack.append(0) 

while stack:
    node = stack.pop() 
    if node not in visited:
        visited.add(node)

        print("Popped Node:", node)
        print("Visited Nodes:", list(visited))

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

        print("Stack:", stack)
        print()

print("Final Visited Nodes:", list(visited))
