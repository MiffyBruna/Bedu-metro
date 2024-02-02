from collections import defaultdict
import heapq
from lineas import  linea_1, linea_2,linea_3, linea_4, linea_5, linea_6, linea_7, linea_8, linea_9, linea_A, linea_B, linea_12


# Inicializamos el grafo
metro_graph = defaultdict(list)


def add_to_graph(line):
    for i in range(len(line) - 1):
        metro_graph[line[i]].append(line[i + 1])
        metro_graph[line[i + 1]].append(line[i])


for line in [linea_1, linea_2, linea_3, linea_4, linea_5, linea_6, linea_7, linea_8, linea_9,linea_A, linea_B, linea_12]:
    add_to_graph(line)

# Implementación del algoritmo de Dijkstra 
def dijkstra_station_count(graph, start, end):
    queue = [(0, start, [])]  
    seen = set()
    while queue:
        (station_count, node, path) = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            path = path + [node]

            if node == end:
                return station_count, path

            for next_node in graph[node]:
                if next_node not in seen:
                    heapq.heappush(queue, (station_count + 1, next_node, path))

    return float("inf"), []  
