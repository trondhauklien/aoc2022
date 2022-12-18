o = {
    'A': 1,
    'B': 2,
    'C': 3
}
l = {
    'A': 3,
    'B': 1,
    'C': 2
}
w = {
    'A': 2,
    'B': 3,
    'C': 1
}

data = []
with open(f"2.txt", "r") as file:
    data = file.read().splitlines()

data = [line.split(" ") for line in data]

output = 0
for i, line in enumerate(data):
    print(line)
    # Lose
    if line[1] == 'X':
        points = l[line[0]]

    # Draw
    elif line[1] == 'Y':
        points = o[line[0]] + 3

    # Win
    else:
        points = w[line[0]] + 6
    
    
    print(points)
    output += points

print(output)

