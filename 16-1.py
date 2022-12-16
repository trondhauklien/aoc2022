# AOC 2022 Day 16 Part 1
# Import regex match function
from re import findall
import networkx as nx
import plotly.graph_objs as go
import matplotlib.pyplot as plt

data = []
with open('16-1.txt', "r") as f:
    data = f.read().splitlines()

#print(data)

start_room = "AA"


class Room:
    """A room in the cave system"""
    def __init__(self, name, connections, flow_rate):
        self.name = name
        self.connections = connections
        self.flow_rate = flow_rate

    def __repr__(self):
        return f'{self.name}'

def parse_line(line):
    """Convert a line of data into a Room object"""
    name = line[6:8]
    # Using regex to find integer value between = and ;
    flow_rate = int(findall(r"=([0-9]+);", line)[0])
    connections = findall(r"([A-Z]{2})", line)[1:]
    return Room(name, connections, flow_rate)

def get_room_priority(rooms):
    """Return priority of rooms bases on flow rate"""
    out = []
    for room in rooms:
        if room.flow_rate != 0:
            out.append(room)
    out.sort(key=lambda x: x.flow_rate, reverse=True)
    return out

def find_path_cost(current_pos, room, G):
    """Find the cost of a path to a room"""
    if current_pos == room:
        return 0
    path = nx.shortest_path(G, source=current_pos, target=room)
    cost = len(path)
    for node in path:
        if node.flow_rate != 0
            cost -= node.flow_rate + 1
    cost -= room.flow_rate
    return cost, path

def main():
    """Main program"""
    rooms = []
    for line in data:
        room = parse_line(line)
        rooms.append(room)
    #print(rooms)
    # for room in rooms:
    #     print(room.connections)
        
    G = nx.Graph()
    for room in rooms:
        for connection in room.connections:
            G.add_edge(room.name, connection)
    f = plt.figure()
    nx.draw(G, with_labels=True, font_size=9, labels={x.name: f"{x.name} {str(x.flow_rate)}" for x in rooms}, ax=f.add_subplot(111))
    f.savefig("graph.png", dpi=400)
    r = get_room_priority(rooms)
    total_cost = 0
    current = start_room
    for e in r:
        print(f"Current: {current} Next: {e.name} Current cost: {total_cost}")
        cost, path = find_path_cost(current, e.name, G)
        total_cost += cost
        for room in path:
            print(f"-> {room}")
        total_cost += 1
        current = e.name
    print(total_cost)
    

if __name__ == "__main__":
    main()