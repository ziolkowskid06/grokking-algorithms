"""
Calculate the shortest path for weighted graph.
"""

# Hash table to represent all nodes and weights
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["finish"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["finish"] = 5
graph["finish"] = {}

# Hash table to store costs for each node
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["finish"] = infinity

# Hash table for the parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None

# Keep track of all nodes, which has been already processed.
processed = []


# Find the lowest-cost node, that haven't been processed
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)

# Check all nodes
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # Go through all the neighbors of this node
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it is cheaper to get this neighbor
        if costs[n] > new_cost:
            costs[n] = new_cost      # Update the cost for this node
            parents[n] = node       # This node become parent for this neighbor
    # Mark node as processed
    processed.append(node)
    # Find the next node to process, and loop
    node = find_lowest_cost_node(costs)

# Show the cheapest path
print(costs)
