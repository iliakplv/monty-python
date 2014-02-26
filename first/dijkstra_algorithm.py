inf = 10000


# Graph definition

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
vertexes_to_visit = {1, 2, 3, 4, 5, 6}  # initially - all vertexes
paths = {1: '', 2: '', 3: '', 4: '', 5: '', 6: ''}
paths_lengths = {1: inf, 2: inf, 3: inf, 4: inf, 5: inf, 6: inf}


# Start and initialization

start_vertex = 1

current_vertex = start_vertex
paths[current_vertex] = str(current_vertex)
paths_lengths[current_vertex] = 0
vertexes_to_visit.remove(current_vertex)


# Algorithm

while vertexes_to_visit:

    # visiting adjacent vertexes
    for vertex_in_visit in vertexes_to_visit:

        # creating string path
        if current_vertex < vertex_in_visit:
            path_to_vertex_from_current = str(current_vertex) + '-' + str(vertex_in_visit)
        else:
            path_to_vertex_from_current = str(vertex_in_visit) + ' ' + str(current_vertex)

        # calculating minimal path to visited vertex
        if path_to_vertex_from_current in adjacency:
            temp_path_length = paths_lengths[current_vertex] + adjacency[path_to_vertex_from_current]
            if temp_path_length < paths_lengths[vertex_in_visit]:
                paths_lengths[vertex_in_visit] = temp_path_length
                paths[vertex_in_visit] = paths[current_vertex] + '-' + str(vertex_in_visit)


    # searching for next current vertex in not visited vertexes

    min_path_length = inf + 1
    new_current_vertex = ''

    for vertex in vertexes_to_visit:

        # creating string path
        if current_vertex < vertex:
            path_to_vertex_from_current = str(current_vertex) + '-' + str(vertex)
        else:
            path_to_vertex_from_current = str(vertex) + '-' + str(current_vertex)

        # searching for adjacent vertex with minimal path
        if path_to_vertex_from_current in adjacency:
            if paths_lengths[vertex] < min_path_length:
                min_path_length = paths_lengths[vertex]
                new_current_vertex = vertex

    if new_current_vertex == '':
        break
    else:
        current_vertex = new_current_vertex
        vertexes_to_visit.remove(current_vertex)



# Result

print('\nResults\n[vertex | path length | path]\n')
for vertex_in_visit in paths.keys():
    print(vertex_in_visit, paths_lengths[vertex_in_visit], paths[vertex_in_visit], sep='\t\t')

