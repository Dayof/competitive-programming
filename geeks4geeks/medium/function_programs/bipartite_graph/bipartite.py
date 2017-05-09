def bipartite(g, s):
    v, q, color = ([False]*(len(g)), [s], [-1]*len(g))
    v[s] = True
    color[s] = 1
    while q:
        s = q.pop(0)
        for i in range(len(g)):
            if g[s][i] and color[i] == -1:
                color[i] = 1 - color[s]
                q.append(i)
            elif g[s][i] and color[i] == color[s]:
                return '0'
    return '1'

# g = {0: [1,3], 1: [0,2], 2: [1,3], 3: [0,2]}
#
# print(bipartite(g,0))
#
# g = {0: [1], 1: [2], 2: [0]}
#
# print(bipartite(g,0))

n = int(input().strip())
for i in range(n):
    g = []
    gsize = int(input().strip())
    allg = list(map(int,input().strip().split(' ')))
    for j in range(gsize):
        newg = allg[gsize*j:gsize*(j+1)]
        g.append(newg)
    print(bipartite(g,0))
