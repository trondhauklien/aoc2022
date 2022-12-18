o = {
    'A': 1,
    'B': 2,
    'C': 3
}

p = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

data = []
with open(f"2.txt", "r") as file:
    data = file.read().splitlines()

data = [line.split(" ") for line in data]

output = 0
for i, line in enumerate(data):
    print(line)
    # Draw
    if o[line[0]] == p[line[1]]:
        points = p[line[1]] + 3

    # Lose to rock
    elif line[0] == 'A' and line[1] == 'Z':
        points = p[line[1]]

    # Win by paper or scissor
    elif o[line[0]] < p[line[1]]:
        points = p[line[1]] + 6
        
    # Win by rock
    elif line[0] == 'C' and line[1] == 'X':
        points = p[line[1]] + 6
        
    # Lose
    else:
        points= p[line[1]]
    
    print(points)
    output += points

print(output)

