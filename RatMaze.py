import random
from collections import deque

def generate_maze(n):
    maze = [[' ' for _ in range(n)] for _ in range(n)]

    # Add random walls
    num_walls = n * n // 3
    for _ in range(num_walls):
        row = random.randint(0, n - 1)
        col = random.randint(0, n - 1)
        maze[row][col] = 'I'  # Wall

    # Set start and end points
    maze[0][0] = 'S'
    maze[n - 1][n - 1] = 'E'

    return maze

def print_maze(maze):
    for row in maze:
        for cell in row:
            if cell == 'I':
                print('\033[1;31m' + '█' + '\033[0m', end=' ')  # Red for walls (█)
            elif cell == 'S' or cell == 'E':
                print('\033[1;33m' + cell + '\033[0m', end=' ')  # Yellow for start and end
            elif cell == ' ':
                print('\033[1;36m' + '◌' + '\033[0m', end=' ')  # Blue for open space (◌)
            else:
                print('\033[1;32m' + '◍' + '\033[0m', end=' ')  # Green for path (◍)
        print()

def bfs_find_path(maze, start, end):
    n = len(maze)
    visited = [[False] * n for _ in range(n)]

    queue = deque([(start, [])])

    while queue:
        current_node, current_path = queue.popleft()

        if current_node == end:
            mark_path(maze, current_path)
            return True  # Reached the end

        row, col = current_node
        if not (0 <= row < n and 0 <= col < n) or maze[row][col] == 'I' or visited[row][col]:
            continue

        visited[row][col] = True

        for neighbor in get_neighbors(current_node, n):
            queue.append((neighbor, current_path + [current_node]))

    return False  # No path found

def get_neighbors(node, n):
    row, col = node
    neighbors = []

    if row > 0:
        neighbors.append((row - 1, col))
    if row < n - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < n - 1:
        neighbors.append((row, col + 1))

    return neighbors

def mark_path(maze, path):
    for node in path:
        row, col = node
        if maze[row][col] not in ('S', 'E'):  # Skip marking start and end points
            maze[row][col] = '◍'  # Marking the path


def main():
    random.seed()

    n = int(input("Enter the size of the maze (n*n): "))
    maze = generate_maze(n)
    print("\nGENERATED MAZE:")
    print_maze(maze)

    start = (0, 0)
    end = (n - 1, n - 1)

    while True:
        choice = int(input("\nOptions:\n1. Print Path (BFS)\n2. Generate Another Puzzle\n3. Exit\nEnter your choice(1/2/3): "))

        if choice == 1:
            if bfs_find_path(maze, start, end):
                print("\nMAZE WITH PATH:")
                print_maze(maze)
            else:
                print("No path found.")
        elif choice == 2:
            n = int(input("Enter the size of the maze (n*n): "))
            maze = generate_maze(n)
            print("\nGENERATED MAZE:")
            print_maze(maze)
            start = (0, 0)
            end = (n - 1, n - 1)
        elif choice == 3:
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

