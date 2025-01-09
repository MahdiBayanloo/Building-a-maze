import random

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

def generate_maze(n):
    # Define grid cells and their unique IDs
    def cell_id(i, j):
        return i * n + j

    uf = UnionFind(n * n)

    # Collect all non-boundary segments
    horizontal_segments = []
    vertical_segments = []

    for i in range(n):
        for j in range(n):
            if i < n - 1 and j != 0 and j != n - 1:  # Horizontal segments (excluding boundaries)
                horizontal_segments.append(((i, j), (i + 1, j)))
            if j < n - 1 and i != 0 and i != n - 1:  # Vertical segments (excluding boundaries)
                vertical_segments.append(((i, j), (i, j + 1)))

    # Combine and shuffle segments
    all_segments = horizontal_segments + vertical_segments
    random.shuffle(all_segments)

    # Remove segments until a path is formed
    for seg in all_segments:
        (x1, y1), (x2, y2) = seg

        cell1 = cell_id(x1, y1)
        cell2 = cell_id(x2, y2)

        if not uf.connected(cell1, cell2):
            uf.union(cell1, cell2)

            # Remove the segment from its respective list
            if seg in horizontal_segments:
                horizontal_segments.remove(seg)
            elif seg in vertical_segments:
                vertical_segments.remove(seg)

        # Check if a path is formed
        if uf.connected(cell_id(0, 0), cell_id(n - 1, n - 1)):
            break

    # Output the remaining segments
    return horizontal_segments, vertical_segments

def display_maze(n, horizontal_segments, vertical_segments):
    maze = [[" "] * (4 * n + 1) for _ in range(4 * n + 1)]

    # Draw cells as squares with segments
    for i in range(n):
        for j in range(n):
            # Top horizontal segment
            if ((i, j), (i + 1, j)) in horizontal_segments or i == 0:
                for x in range(4 * j + 1, 4 * j + 4):
                    maze[4 * i][x] = "_"
            # Bottom horizontal segment
            if ((i + 1, j), (i + 2, j)) in horizontal_segments or i == n - 1:
                for x in range(4 * j + 1, 4 * j + 4):
                    maze[4 * i + 4][x] = "_"
            # Left vertical segment
            if ((i, j), (i, j + 1)) in vertical_segments or j == 0:
                for y in range(4 * i + 1, 4 * i + 4):
                    maze[y][4 * j] = "|"
            # Right vertical segment
            if ((i, j + 1), (i, j + 2)) in vertical_segments or j == n - 1:
                for y in range(4 * i + 1, 4 * i + 4):
                    maze[y][4 * j + 4] = "|"

    # Print the maze
    for row in maze:
        print("".join(row))

if __name__ == "__main__":
    n = 10  # Change to desired grid size
    horizontal_segments, vertical_segments = generate_maze(n)
    display_maze(n, horizontal_segments, vertical_segments)
