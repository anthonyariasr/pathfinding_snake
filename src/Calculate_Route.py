import heapq

def calculate_route(ini, end, obstacles):
    """
    Create the Base Matrix and Turn it into a Graph

    Here we created a matrix of 20x20 that will only be used to generate
    a graph that will serve as base for the Dijkstra's Algorithm to find
    the fastes path from one point to another.

    """

    def create_matrix():
        matrix = [["" for _ in range(20)] for _ in range(20)]
        return matrix

    matrix = create_matrix()

    def add_obstacles():
        for obstacle in obstacles:
            matrix[obstacle[0]][obstacle[1]] = "x"

    add_obstacles()



    def create_graph(matrix):
        graph = {}
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != "x":  # Skip adding neighbors for obstacles
                    neighbors = []
                    # Up
                    if row - 1 >= 0 and matrix[row - 1][col] != "x":
                        neighbors.append((row - 1, col))
                    # Down
                    if row + 1 < rows and matrix[row + 1][col] != "x":
                        neighbors.append((row + 1, col))
                    # Left
                    if col - 1 >= 0 and matrix[row][col - 1] != "x":
                        neighbors.append((row, col - 1))
                    # Right
                    if col + 1 < cols and matrix[row][col + 1] != "x":
                        neighbors.append((row, col + 1))

                    graph[row, col] = neighbors
        return graph

    graph = create_graph(matrix)


    "---------------------------------------------------------------------"

    """
    Dijkstra's Algorithm

    We are using the Dijkstra's Algorithm to calculate a
    shortest path from one point to another. This algorithm recieves
    the full original graph created from the base matrix and due to it's
    efficiancy it returns a list that represents the "shortest path"

    """

    def shortest_path(graph, initial_coordinate, end_coordinate):
        # Initialize distances to all nodes as infinity
        distances = {coordinate: float('inf') for coordinate in graph}
        distances[initial_coordinate] = 0

        # Priority queue to keep track of the next node to visit
        priority_queue = [(0, initial_coordinate)]

        # Keep track of the previous node for each node in the shortest path
        previous = {}

        while priority_queue:
            # Pop the node with the smallest distance from the priority queue
            current_distance, current_coordinate = heapq.heappop(priority_queue)

            # If we have found the end coordinate, reconstruct the path and return it
            if current_coordinate == end_coordinate:
                path = []
                while current_coordinate in previous:
                    path.insert(0, current_coordinate)
                    current_coordinate = previous[current_coordinate]
                path.insert(0, initial_coordinate)
                return path

            # Check distances to neighboring coordinates and update if shorter path found
            for neighbor_coordinate in graph[current_coordinate]:
                distance = current_distance + 1  # Assuming uniform edge weights of 1
                if distance < distances[neighbor_coordinate]:
                    distances[neighbor_coordinate] = distance
                    heapq.heappush(priority_queue, (distance, neighbor_coordinate))
                    previous[neighbor_coordinate] = current_coordinate

        # If no path found, return an empty list
        return []

    shortest_path_Dijkstra = shortest_path(graph, ini, end)
    
    return shortest_path_Dijkstra


