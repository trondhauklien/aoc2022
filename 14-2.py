data = []
with open(f"14.txt", "r") as file:
    data = file.read().splitlines()

def parsePoints(array):
    out = []
    for row in array:
        out.append([int(e) for e in row.split(",")])
    return out

for i, row in enumerate(data):
    data[i] = row.split(" -> ")

for i, row in enumerate(data):
    data[i] = [(int(x), int(y)) for x, y in [e.split(",") for e in row]]

filled = set()
for row in data:
    for i in range(1, len(row)):
        px, py = row[i-1]
        cx, cy = row[i]
        if cx == px:
            for y in range(min(py, cy), max(py, cy) + 1):
                filled.add((cx, y))
        if cy == py:
            for x in range(min(px, cx), max(px, cx) + 1):
                filled.add((x, cy))

m = max([e[1] for e in filled]) + 2

bottom = [(x, m) for x in range(-1000, 10000)]
for e in bottom:
    filled.add(e)

def simulate_sand():
    x, y = 500, 0
    while (500, 0) not in filled:
        if (x, y+1) not in filled:
            y += 1
        elif (x-1, y+1) not in filled:
            x -= 1
        elif (x+1, y+1) not in filled:
            x += 1
        else:
            filled.add((x, y))
            return True
    return False

ans = 0
while True:
    if simulate_sand():
        ans += 1
    else:
        break

print(ans)
