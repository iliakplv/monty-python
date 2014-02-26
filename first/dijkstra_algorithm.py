inf = 10000


# Graph

adjacency = {
    '1-2': 7,
    '1-3': 9,
    '1-6': 14,
    '2-3': 10,
    '2-4': 15,
    '3-4': 11,
    '3-6': 2,
    '4-5': 6,
    '5-6': 9
}

vertexes_to_visit = {1, 2, 3, 4, 5, 6}

paths = {1: '', 2: '', 3: '', 4: '', 5: '', 6: ''}

paths_lengths = {1: inf, 2: inf, 3: inf, 4: inf, 5: inf, 6: inf}


# Start and Finish vertexes

start = 1


# Initialization

current_vertex = start
paths[current_vertex] = str(current_vertex)
paths_lengths[current_vertex] = 0


# TODO algorithm
# while vertexes_to_visit not empty

    # delete current_vertex from vertexes_to_visit

    # for vertex in vertexes_to_visit and adjacent
        # temp_path_length = current_vertex path_length + adjacency_value
        # if (temp_path_length < existing path to vertex)
            # init vertex path length (temp_path_length)
            # init vertex path ('current_vertex path' + 'vertex')

    # set current_vertex to vertex: adjacent, with minimal path_length, not visited (if existing)

while vertexes_to_visit:
    vertexes_to_visit.remove(current_vertex)

    for vertex_in_visit in vertexes_to_visit:
        if vertex_in_visit != current_vertex: # (removed)
            path_to_vertex_from_current = str(current_vertex) + '-' + str(vertex_in_visit)
            if path_to_vertex_from_current in adjacency:
                temp_path_length = paths_lengths[current_vertex] + adjacency[path_to_vertex_from_current]
                if temp_path_length < paths_lengths[vertex_in_visit]:
                    paths_lengths[vertex_in_visit] = temp_path_length
                    paths[vertex_in_visit] = paths[current_vertex] + '-' + str(vertex_in_visit)

    min_path_length = inf
    new_current_vertex = ''

    for vertex in vertexes_to_visit:
        path_to_vertex_from_current = str(current_vertex) + '-' + str(vertex)
        if path_to_vertex_from_current in adjacency:
            if paths_lengths[vertex] < min_path_length:
                min_path_length = paths_lengths[vertex]
                new_current_vertex = vertex

    if new_current_vertex == '':
        break
    else:
        current_vertex = new_current_vertex


# Result

print('\nResults\n[vertex | path length | path]\n')
for vertex_in_visit in paths.keys():
    print(vertex_in_visit, paths_lengths[vertex_in_visit], paths[vertex_in_visit], sep='\t\t')

