import random

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        

        

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

def build_maze(n):
    grid_size = n * n
    uf = UnionFind(grid_size)

    horizontal_edges = [((i, j), (i + 1, j)) for i in range(n - 1) for j in range(n)]
    vertical_edges = [((i, j), (i, j + 1)) for i in range(n) for j in range(n - 1)]

    edges = horizontal_edges + vertical_edges

    # Remove boundary edges
    edges = [edge for edge in edges if 0 < edge[0][0] < n - 1 and 0 < edge[0][1] < n - 1]

    random.shuffle(edges)

    maze = set()
    for edge in edges:
        (x1, y1), (x2, y2) = edge
        idx1 = x1 * n + y1
        idx2 = x2 * n + y2

        if not uf.connected(idx1, idx2):
            uf.union(idx1, idx2)
            maze.add(edge)

        # Ensure a path between start and finish
        if uf.connected(0, grid_size - 1):
            break

    return maze

def print_maze(maze, n):
    grid = [["#"] * (2 * n + 1) for _ in range(2 * n + 1)]

    for i in range(n):
        for j in range(n):
            grid[2 * i + 1][2 * j + 1] = " "

    for (x1, y1), (x2, y2) in maze:
        if x1 == x2:  # Horizontal edge
            grid[2 * x1 + 1][2 * y1 + 2] = " "
        else:  # Vertical edge
            grid[2 * x1 + 2][2 * y1 + 1] = " "

    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    n = 60
    maze = build_maze(n)
    print_maze(maze, n)
