from heapq import heappush, heappop
data = []
with open(f"12.txt", "r") as file:
    data = file.read().splitlines()

alph = "abcdefghijklmnopqrstuvwxyz"

def alpha_to_num(c):
    c = c.lower()
    return alph.index(c)

start = None
n, m = len(data), len(data[0])
data2 = []
for i, line in enumerate(data):
    row = []
    for j, c in enumerate(line):
        if (c == "E"):
            start = [i, j]
            row.append(alpha_to_num("z"))
            continue
        if (c == "S"):
            row.append(alpha_to_num("a"))
            continue
        row.append(alpha_to_num(c))
    data2.append(row)

def neighbours(i, j):
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if 0 <= i + di < n and 0 <= j + dj < m:
            if data2[i][j] <= data2[i + di][j + dj] + 1:
                yield i + di, j + dj

visited = [[False] * m for _ in range(n)]
heap = [(0, start[0], start[1])]

while True:
    steps, i, j = heappop(heap)

    if visited[i][j]:
        continue

    visited[i][j] = True

    if data2[i][j] == alpha_to_num("a"):
        print(steps)
        break

    for ni, nj in neighbours(i, j):
        heappush(heap, (steps + 1, ni, nj))

