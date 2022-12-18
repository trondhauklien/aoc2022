data = []
with open(f"5-1.txt", "r") as file:
    data = file.read().splitlines()


data = [e.split() for e in data]
data = [[e.replace("[", "").replace("]", "") for e in row] for row in data]

# print(data)

def move(n=0, f=0, t=0, d=[]):
    f=f-1
    t=t-1
    for i in range(0, n):
        tmp = d[f].pop(0)
        d[t].insert(0, tmp)
    return d

instructions = []
with open(f"5-2.txt", "r") as file:
    instructions = file.read().splitlines()

instructions = [e.replace("move", "").replace("from", "").replace("to", "") for e in instructions]
instructions = [e.split() for e in instructions]

# print(instructions)

for line in instructions:
    data = move(int(line[0]), int(line[1]), int(line[2]), data)

print("".join([e[0] for e in data]))


