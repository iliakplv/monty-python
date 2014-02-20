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


# Result

print('\nResults\n[vertex | path length | path]\n')
for vertex in paths.keys():
    print(vertex, paths_lengths[vertex], paths[vertex], sep='\t\t')

