from GraphLib import *
from Tree import *
from Graph import *

values = []

for i in range(1000):
    graph = createSimpleGraph(10, 2)
    count = 0

    while not graph.isBipartite():
        graph = createSimpleGraph(10, 2)
        count += 1

    values.append(count)
    count = 0

total = 0
for num in values:
    total += num

print(f"mean = {total/1000}")
print(f"meadian = {(values[500] + values[499])/2}")




