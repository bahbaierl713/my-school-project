def find_shortest_path(graph, start, end):
    from collections import defaultdict

    # Build an adjacency list representation of the graph
    adj_list = defaultdict(list)
    for u, v in graph.items():
        if v is not None:
            adj_list[u].append(v)

    # Dijkstra's algorithm to find the shortest path
    queue = [(0, start)]
    while queue:
        dist, u = queue.pop(0)
        if u == end:
            return dist

        for neighbor in adj_list[u]:
            alt_dist = dist + 1  # Add a unit to each neighbor's distance
            if (neighbor, alt_dist) not in queue or alt_dist < queue[0][1]:
                queue.append((alt_dist, neighbor))

    raise ValueError("No path found between {0} and {1}".format(start, end))
