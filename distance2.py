# connections = ['Kitchen–LivingRoom', 'Bedroom–Bathroom', 'LivingRoom–Bedroom']
# start_room = 'Kitchen'
# end_room = 'Bathroom'

from collections import defaultdict
from collections import deque
def findingdistance(connections,start_room,end_room):
    graph=defaultdict(list)
    for connection in connections:
        room1,room2=connection.split('-')
        graph[room2].append(room1)
        graph[room1].append(room2)
    queue=deque()
    queue.append((start_room,[start_room]))
    visited=set()
    while queue:
        current,path=queue.popleft()
        if current==end_room:
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append((neighbour,path+[neighbour]))
    return []

# {'LivingRoom': ['Kitchen', 'Bedroom'], 'Kitchen': ['LivingRoom'], 'Bathroom': ['Bedroom'], 'Bedroom': ['Bathroom', 'LivingRoom']})
connections = ['Kitchen-LivingRoom', 'Bedroom-Bathroom', 'LivingRoom-Bedroom']
start_room = 'Kitchen'
end_room = 'Bathroom'
print(findingdistance(connections,start_room,end_room))