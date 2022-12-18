data = []
with open(f"13.txt", "r") as file:
    data = file.read().splitlines()

data = list(filter(None, data))

for i, row in enumerate(data):
    data[i] = eval(row)

def compare_lists(left, right):
    print(f"  Compare: {left} vs {right}")
    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    if isinstance(left, list) and isinstance(right, int):
        right = [right]

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        if left > right:
            return 0
        return 2
    
    i = 0
    while i < len(left) and i < len(right):
        match compare_lists(left[i], right[i]):
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                i += 1
                continue
    
    if i == len(left):
        if len(left) == len(right):
            return 2
        return 1
    
    return 0


output = 0
for i, row in enumerate(data):
    if i % 2 != 0:
        continue
    print(f"== Pair {i/2+1} ==")
    if compare_lists(row, data[i+1]):
        print("Correct order")
        output += i / 2 + 1

print(output)