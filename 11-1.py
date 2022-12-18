import textwrap
import math
from functools import reduce
data = []
with open(f"11.txt", "r") as file:
    data = file.read().splitlines()

class Monkey:
    def __init__(self, data):
        self.id:int = int(data[0].split()[1].split(":")[0])
        self.inventory:list[int] = [int(e) for e in data[1].split(": ")[1].split(", ")]
        self.operation:str = data[2].split("old ")[1]
        self.test:int = int(data[3].split("by ")[1])
        self.ifTrue:int = int(data[4].split("monkey ")[1])
        self.ifFalse:int = int(data[5].split("monkey ")[1])
        self.monkeyBusiness = 0

    def doTurn(self):
        global monkeys
        #print(self)
        for item in self.inventory:
            if self.operation == "* old":
                item = item * item
            elif self.operation.split()[0] == "*":
                item = item * int(self.operation.split()[1])
            elif self.operation.split()[0] == "+":
                item = item + int(self.operation.split()[1])
            #item = math.floor(item / 3)
            item = self.facRed(item)
            monkeys[self.doTest(item)].inventory.append(item)
            self.monkeyBusiness += 1
        self.inventory = []

    def facRed(self, number):
        return number % mem 

    def checkForTests(self, factors):
        global tests
        for test in tests:
            if test in factors:
                continue
            else: 
                return False
        return True

    def doTest(self, item):
        if item % self.test == 0:
            return self.ifTrue
        else:
            return self.ifFalse 
    
    def __repr__(self):
        return f"""
        Monkey {self.id}:
        Inventory: {self.inventory}
        Operation: {self.operation}
        Test: divisible by {self.test}
        If True: throw to monkey {self.ifTrue}
        If False: throw to monkey {self.ifFalse}
        Current Monkey Business: {self.monkeyBusiness}"""

monkeys = []
dataBlocks = []
i = 0
for line in data:
    if line == "":
        i += 1
    else:
        if i == len(dataBlocks):
            dataBlocks.append([])
        dataBlocks[i].append(line)

for dataBlock in dataBlocks:
    monkeys.append(Monkey(dataBlock))

mem = 1
tests = []
for monkey in monkeys:
    mem *= monkey.test
    tests.append(monkey.test)

print(mem)
for round in range(10000):
    for monkey in monkeys:
        monkey.doTurn()

print("##### FINISHED #####")
for monkey in monkeys:
    print(monkey)

monkeyBusiness = [monkey.monkeyBusiness for monkey in monkeys]
monkeyBusiness.sort()
print(monkeyBusiness[-1] * monkeyBusiness[-2])