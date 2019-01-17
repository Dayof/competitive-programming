def next_not_visited(v):
    for it, aux in enumerate(v):
        if not aux:
            return it
    return -1

def count_pattern(g):
    v = [False for k in range(len(g))]
    q_pattern, inner_pattern = 0, 0
    q, v[0] = [g[0]], True

    while len(q) != 0: 
        it = q.pop(0)
        
        if it[0] == 'X':
            inner_pattern += 1
            for aux in it[1]:
                node = g[aux]
                if not v[aux] and node[0] == 'X':  # not visited X
                    v[aux] = True
                    q.append(node)
            if len(q) == 0:
                q_pattern += 1 
                inner_pattern = 0

        if len(q) == 0:
            res = next_not_visited(v)
            if res == -1:
                return q_pattern
            else:
                q.append(g[res])
                v[res] = True

    return q_pattern

def add_row(adj, row, it, c):
    counter = it
    for v in row:
        adj.append((row[counter%c], [], counter))
        if counter > 0 and counter%c != 0:
            adj[counter-1][1].append(counter)
            adj[counter][1].append(counter-1)
        if counter-c >= 0:
            adj[counter-c][1].append(counter)
            adj[counter][1].append(counter-c)
        counter += 1

def build_graph(c, mat):
    adj = []
    aux_c = 0
    for row in mat:
        add_row(adj, row, aux_c, c)
        aux_c += c
    return adj
    
tries = int(input())

for t in range(tries):
    r, c = map(int, input().split())
    mat = input().split()
    g = build_graph(c, mat)
    print(count_pattern(g))