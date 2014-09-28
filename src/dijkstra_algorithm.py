inf = 1e12
no = -1


# Graph
# numbers of lines and rows must be equals
# value of matrix[i][j] is weight of edge (i) -> (j)
# weight of edge between non adjacent vertices must be equals to inf
# values on matrix's diagonal do not matter

graph_matrix = [[no, 7, 9, inf, inf, 14],
                [7, no, 10, 15, inf, inf],
                [9, 10, no, 11, inf, 2],
                [inf, 15, 11, no, 6, inf],
                [inf, inf, inf, 6, no, 9],
                [14, inf, 2, inf, 9, no]]


# Start and End of shortest path to search

start_vertex = 0
end_vertex = 5
search_all_paths = True
# if False only shortest path from Start to End will be found


##### Initialization #####

vertices_to_visit = set()
predecessors = {}
paths_lengths = {}
for v in range(len(graph_matrix)):
    vertices_to_visit.add(v)
    predecessors[v] = no
    paths_lengths[v] = inf
current_vertex = start_vertex
paths_lengths[current_vertex] = 0
vertices_to_visit.remove(current_vertex)


# Algorithm

while vertices_to_visit:

    if (not search_all_paths) and current_vertex == end_vertex:
        break

    # visiting unvisited adjacent vertices

    for vertex in vertices_to_visit:
        if graph_matrix[current_vertex][vertex] < inf:
            temp_path_length = paths_lengths[current_vertex] + graph_matrix[current_vertex][vertex]
            if temp_path_length < paths_lengths[vertex]:
                paths_lengths[vertex] = temp_path_length
                predecessors[vertex] = current_vertex

    # searching for next current vertex in unvisited vertices

    min_path_length = inf
    next_current_vertex = ''

    for vertex in vertices_to_visit:
        if paths_lengths[vertex] < min_path_length:
            min_path_length = paths_lengths[vertex]
            next_current_vertex = vertex

    if next_current_vertex == '':
        break
    else:
        current_vertex = next_current_vertex
        vertices_to_visit.remove(current_vertex)


# Result path calculation

vertex = end_vertex
result_path = '(' + str(vertex) + ')'
while vertex != start_vertex:
    result_path = '(' + str(predecessors[vertex]) + ') -> ' + result_path
    vertex = predecessors[vertex]


##### Results printing #####

print('\nResult path: ' + result_path)
print('Result path length: ' + str(paths_lengths[end_vertex]))

if search_all_paths:
    print('\nAll results:\n[ vertex | path length | predecessor ]')

    for vertex in paths_lengths.keys():
        print(vertex, paths_lengths[vertex], predecessors[vertex], sep='\t\t')