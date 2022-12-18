from heapq import heappush, heappop
data = []
with open(f"12.txt", "r") as file:
    data = file.read().splitlines()

data2= []
for line in data:
    row = []
    for c in line:
        if (c == "S" or c == "E"):
            row.append(c)
            continue
        row.append(ord(c))
    data2.append(row)
# Split the data into a 2D array
#print(data2)


# the data array contains topology information
# the start point is S and the end point is E
# points "a" are lowest, "z" are highest
# You can only move in the cardinal directions
# You cant only move to a point that is one step above or less than the current point
# You can move to a point that is the same height as the current point

# Define a point class
class Point:
    def __init__(self, x, y, children = []):
        self.x = x
        self.y = y
        self.children = children

class Path:
    def __init__(self, path = []):
        self.path = path
        self.length = len(path)
    
    def addPoint(self, point):
        self.path.append(point)
        self.length += 1

# X is the row, Y is the column
# Implement a dijkstra first search
class Dijkstra:
    def __init__(self, data):
        self.data = data
        self.start = self.findStart()
        self.end = self.findEnd()
        self.visited = [[False] * len(x) for x in self.data]
        self.heap = [(0, self.start[0], self.start[1])]
        self.data[self.start[0]][self.start[1]] = ord("c")
        self.data[self.end[0]][self.end[1]] = ord("z")

    def getDatapoint(self, x, y):
        return self.data[x][y]

    def findStart(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if (self.getDatapoint(i, j) == "S"):
                    return [i, j]

    def findEnd(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.getDatapoint(i, j) == "E":
                    return [i, j]

    def findNeighbors(self, point):
        x, y = point[0], point[1]
        neighbors = []
        if (x > 0):
            neighbors.append([x - 1, y])
        if (x < len(self.data) - 1):
            neighbors.append([x + 1, y])
        if (y > 0):
            neighbors.append([x, y - 1])
        if (y < len(self.data[0]) - 1):
            neighbors.append([x, y + 1])
        return neighbors

    def findValidNeighbors(self, point):
        x, y = point[0], point[1]
        neighbors = self.findNeighbors(point)
        validNeighbors = []
        for neighbor in neighbors:
            if (self.data[neighbor[0]][neighbor[1]] <= self.data[x][y] + 1):
                validNeighbors.append(neighbor)
        return validNeighbors

b = Dijkstra(data2)
while True:
    steps, x, y = heappop(b.heap)
    
    if b.visited[x][y]:
        continue

    b.visited[x][y] = True

    if [x, y] == b.end:
        print(steps)
        break

    for neighbor in b.findValidNeighbors([x, y]):
        heappush(b.heap, (steps + 1, neighbor[0], neighbor[1]))

