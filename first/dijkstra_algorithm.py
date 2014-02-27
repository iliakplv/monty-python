inf = 10000
no = -1


# Graph definition

adjacency = [[inf, 7, 9, inf, inf, 14],
             [7, inf, 10, 15, inf, inf],
             [9, 10, inf, 11, inf, 2],
             [inf, 15, 11, inf, 6, inf],
             [inf, inf, inf, 6, inf, 9],
             [14, inf, 2, inf, 9, inf]]

vertexes_to_visit = {0, 1, 2, 3, 4, 5}  # initially - all vertexes
predecessors = {0: no, 1: no, 2: no, 3: no, 4: no, 5: no}
paths_lengths = {0: inf, 1: inf, 2: inf, 3: inf, 4: inf, 5: inf}


# Path start/end

start_vertex = 0
end_vertex = 5


##### Initialization #####

current_vertex = start_vertex
paths_lengths[current_vertex] = 0
vertexes_to_visit.remove(current_vertex)


# Algorithm

while vertexes_to_visit:

    # visiting unvisited adjacent vertexes

    for vertex in vertexes_to_visit:
        if adjacency[current_vertex][vertex] < inf:
            temp_path_length = paths_lengths[current_vertex] + adjacency[current_vertex][vertex]
            if temp_path_length < paths_lengths[vertex]:
                paths_lengths[vertex] = temp_path_length
                predecessors[vertex] = current_vertex

    # searching for next current vertex in unvisited vertexes

    min_path_length = inf
    next_current_vertex = ''

    for vertex in vertexes_to_visit:
        if paths_lengths[vertex] < min_path_length:
            min_path_length = paths_lengths[vertex]
            next_current_vertex = vertex


    if next_current_vertex == '':
        break
    else:
        current_vertex = next_current_vertex
        vertexes_to_visit.remove(current_vertex)


# Result path calculation

vertex = end_vertex
result_path = str(vertex)
while vertex != start_vertex:
    result_path = str(predecessors[vertex]) + ' -> ' + result_path
    vertex = predecessors[vertex]


##### Results printing #####

print('\nResults:\n[ vertex | path length | predecessor ]')

for vertex in paths_lengths.keys():
    print(vertex, paths_lengths[vertex], predecessors[vertex], sep='\t\t')

print('\nResult path: ' + result_path)
print('Result path length: ' + str(paths_lengths[end_vertex]))