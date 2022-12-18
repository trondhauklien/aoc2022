from itertools import groupby
import numpy as np

data = []
with open(f"1.txt", "r") as file:
    data = file.read().splitlines()

# using itertools.groupby() + list comprehension
# divide list to siblist on deliminator
res = [list(sub) for ele, sub in groupby(data, key = bool) if ele]

output = []
for l in res:
    l = list(map(int, l))
    output.append(sum(l))

total = 0
total += output.pop(output.index(max(output)))
total += output.pop(output.index(max(output)))
total += output.pop(output.index(max(output)))

print(total)



# finished = False
# output = {}
# index = 0
# while not finished:
#     output[f"elf_{index}"] = 0
#     for i, line in enumerate(data):
#         if i == len(data) - 1:
#             finished = True
#             break
#         d = data.pop(i)
#         if d == "":
#             break
#         output[f"elf_{index}"] += int(d)
#     index += 1

# print(max(output.values()))

    
