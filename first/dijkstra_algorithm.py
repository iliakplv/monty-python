inf = 10000


# Graph definition

adjacency = [[inf, 7, 9, inf, inf, 14],
             [7, inf, 10, 15, inf, inf],
             [9, 10, inf, 11, inf, 2],
             [inf, 15, 11, inf, 6, inf],
             [inf, inf, inf, 6, inf, 9],
             [14, inf, 2, inf, 9, inf]]

vertexes_to_visit = {0, 1, 2, 3, 4, 5}  # initially - all vertexes
previous_vertexes = {0: '', 1: '', 2: '', 3: '', 4: '', 5: ''}
paths_lengths = {0: inf, 1: inf, 2: inf, 3: inf, 4: inf, 5: inf}


# Start and initialization

start_vertex = 0

current_vertex = start_vertex
previous_vertexes[current_vertex] = -1
paths_lengths[current_vertex] = 0
vertexes_to_visit.remove(current_vertex)


# Algorithm

while vertexes_to_visit:

    # visiting adjacent vertexes

    for vertex_in_visit in paths_lengths.keys():
        if adjacency[current_vertex][vertex_in_visit] < inf:
            temp_path_length = paths_lengths[current_vertex] + adjacency[current_vertex][vertex_in_visit]
            if temp_path_length < paths_lengths[vertex_in_visit]:
                paths_lengths[vertex_in_visit] = temp_path_length
                previous_vertexes[vertex_in_visit] = current_vertex

    # searching for next current vertex in not visited vertexes

    min_path_length = inf
    next_current_vertex = ''

    for vertex in vertexes_to_visit:
        if adjacency[current_vertex][vertex] < inf:
            if paths_lengths[vertex] < min_path_length:
                min_path_length = paths_lengths[vertex]
                next_current_vertex = vertex

    if next_current_vertex == '':
        break
    else:
        current_vertex = next_current_vertex
        vertexes_to_visit.remove(current_vertex)


# Result # todo

print('\nResults\n[vertex | path length | path]\n')
for vertex in paths_lengths.keys():
    print(vertex+1, paths_lengths[vertex], previous_vertexes[vertex]+1, sep='\t\t')
