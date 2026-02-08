import os
import networkx as nx
import matplotlib.pyplot as plt
import heapq

def create_graph_from_file(file_path):

    network = nx.Graph()

    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Parse first line to get number of nodes and edges
    num_nodes, num_edges = map(int, lines[0].strip().split(','))
    
    # add edges
    for i in range(1, num_edges + 1):
        u, v, weight = lines[i].strip().split(',')
        network.add_edge(u, v, weight=int(weight))
    
    return network

def draw_weighted_graph(graph):
    # pos = nx.circular_layout(graph)
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edge_labels(
        graph, pos, edge_labels={(u, v): d["weight"] for u, v, d in graph.edges(data=True)}
    )
    plt.show()

def dijkstra_shortest_path(graph, start_node):

    # Initialize distances and predecessors
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start_node] = 0
    predecessors = {node: None for node in graph.nodes()}
    
    # Priority queue for Dijkstra
    # Elements are tuples of (distance, node)
    priority_queue = [(0, start_node)]
    
    # Set to track visited nodes
    visited = set()
    
    # For tracing the algorithm execution
    trace = []
    settled_nodes = []
    
    step = 0
    
    while priority_queue:
        # Get node with minimum distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we've already processed this node, skip it
        if current_node in visited:
            continue
        
        # Mark as visited
        visited.add(current_node)
        settled_nodes.append(current_node)
        
        # If current distance is greater than stored distance, skip
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighbors
        for neighbor in graph.neighbors(current_node):
            # Get edge weight
            weight = graph[current_node][neighbor]['weight']
            
            # Calculate potential new distance
            distance = current_distance + weight
            
            # If we found a shorter path to neighbor
            if distance < distances[neighbor]:
                # Update distance and predecessor
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                
                # Add to priority queue
                heapq.heappush(priority_queue, (distance, neighbor))
        
        # Record the state after this step
        step_data = {
            'step': step,
            'settled_nodes': settled_nodes.copy(),
            'distances': distances.copy(),
            'predecessors': predecessors.copy()
        }
        trace.append(step_data)
        step += 1
    
    return distances, predecessors, trace

def print_trace_table(graph, start_node):

    distances, predecessors, trace = dijkstra_shortest_path(graph, start_node)

    other_nodes = [node for node in graph.nodes if node != start_node]
    
    num_of_cols = len(other_nodes) + 2
    col_width = 12
    table_width = num_of_cols*col_width

    # Table header
    header = f"{'Step':<6}{'N′':<{col_width}}"
    for node in other_nodes:
        header += f"{f'D({node}),p({node})':<{col_width}}"

    print(f"Running link-state algorithm for node {start_node}:")
    print("-"*table_width)
    print(header)
    print("-"*table_width)

    for data in trace:
        step = data['step']
        settled = "".join(data['settled_nodes'])

        row = f"{step:<6}{settled:<{col_width}}"
        for node in other_nodes:
            dist = data['distances'][node]
            pred = data['predecessors'][node]

            dist_str = "∞" if dist == float('infinity') else str(dist)
            pred_str = "" if pred is None else pred
            if dist == float('infinity'):
                cell_content = f"    {dist_str}"
            else:
                cell_content = f"   {dist_str},{pred_str}"
            row += f"{cell_content:<{col_width}}"

        print(row)
    print("-"*table_width)

def get_shortest_path(distances, predecessors, target_node):

    if distances[target_node] == float('infinity'):
        return None, float('infinity')
    
    path = []
    current = target_node
    
    # Reconstruct path by following predecessors
    while current is not None:
        path.append(current)
        current = predecessors[current]
    
    # Reverse to get path from start to end
    path.reverse()
    
    return path, distances[target_node]

def print_forwarding_table(graph, start_node):

    distances, predecessors, _ = dijkstra_shortest_path(graph, start_node)
    forwarding_table = {}
    
    for destination in graph.nodes():
        if destination == start_node:
            continue
            
        path, _ = get_shortest_path(distances, predecessors, destination)
        
        if path and len(path) > 1:
            # First hop in the path from source to destination
            next_hop = path[1]
            forwarding_table[destination] = next_hop

    print(f"\nForwarding table for node {start_node}:")
    print("-" * 25)
    print(f"{'Destination':<15} {' Link':<15}")
    print("-" * 25)
    
    for destination, next_hop in forwarding_table.items():
        link = f"({start_node}, {next_hop})"
        print(f"     {destination:<10} {link:<15}")
    print("-" * 25)
    print(f"\n")

# file_path = "d:/Projects/PythonProjects/Networks task/extra example.txt"
file_path = "d:/Projects/PythonProjects/Networks task/input.txt"

network = create_graph_from_file(file_path)

for node in network.nodes:
    print_trace_table(network, node)
    print_forwarding_table(network, node)

draw_weighted_graph(network)
