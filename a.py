import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == end:
            break
#nbksdbnslkfgnskl
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    path = []
    current_node = end
    while current_node != start:
        path.insert(0, current_node)
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] == distances[neighbor] + weight:
                current_node = neighbor
                break
    path.insert(0, start)
    return path, distances[end]


graph = {
    '1': {'2': 5, '3': 5, '4': 6},
    '2': {'1': 5, '5': 4, '6': 7, '7': 8},
    '3': {'1': 5, '5': 8, '6': 10, '7': 5},
    '4': {'1': 6, '5': 5, '6': 5, '7': 4},
    '5': {'2': 4, '3': 8, '4': 5, '8': 7},
    '6': {'2': 7, '3': 10, '4': 5, '8': 5, '9': 8},
    '7': {'2': 8, '3': 5, '4': 4, '9': 5},
    '8': {'5': 7, '6': 5, '9': 7, '10': 5},
    '9': {'8': 7, '6': 8, '7': 5, '10': 6},
    '10': {'8': 5, '9': 6}
}


start_node = '1'
end_node = '10'

path, cost = dijkstra(graph, start_node, end_node)
print("Shortest path from node", start_node, "to node", end_node, ":", path)
print("Cost:", cost)
