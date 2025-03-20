from collections import deque

def bfs_maze_solver(maze, start, end):
    """
    BFS Maze Solver

    Args:
        maze (list of list): Maze matrix (0 -> passable, 1 -> obstacle)
        start (tuple): Start position (row, col)
        end (tuple): End position (row, col)

    Returns:
        list: Shortest path from start to end (step by step)
    """

    # Direction vectors: represents up, down, left, right movements
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS queue (current position and the road so far)
    queue = deque([(start, [start])])
    visited = set() # Already visited nodes

    while queue:
        (current, path) = queue.popleft()

        # Mark the current node as visited
        visited.add(current)

        # Check if end is reached
        if current == end:
            return path
        
        # Explore neighbors
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            # Check if neighbor is valid, not visited and not an obstacle
            if (0 <= neighbor[0] < len(maze) and # Check for valid row
                0 <= neighbor[1] < len(maze[0]) and # Check for falid col
                maze[neighbor[0]][neighbor[1]] == 0 and # Check if not an obstacle
                neighbor not in visited): # Check if already visited

                queue.append((neighbor, path + [neighbor]))

    # If no path is found, return None
    return None

# Example maze
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

# Start and end positions
start = (0, 0) # Left upper corner
end = (4, 4) # Right lower corner

# Run BFS maze solver
if __name__ == "__main__":
    shortest_path = bfs_maze_solver(maze, start, end)
    if shortest_path:
        print("Shortest path:", shortest_path)
    else:
        print("No path found")

