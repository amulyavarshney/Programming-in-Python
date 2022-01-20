# To find the shortest possible route that visits every city exactly once and returns to the starting point.
import numpy as np
from itertools import combinations
import sys

INF = sys.maxsize

def TSP(G):
    n = len(G)
    C = [[np.inf for _ in range(n)] for __ in range(1 << n)]
    C[1][0] = 0 # {0} <-> 1

    for size in range(1, n):
        for S in combinations(range(1, n), size):
            S = (0,) + S
            k = sum([1 << i for i in S])
            for i in S:
                if i == 0: continue
                for j in S:
                    if j == i: 
                        continue
                    cur_index = k ^ (1 << i)
                    C[k][i] = min(C[k][i], C[cur_index][j]+ G[j][i])     
                                            
    all_index = (1 << n) - 1
    return min([(C[all_index][i] + G[0][i], i) for i in range(n)])

if __name__ == '__main__':
    graph = [[0, 5, INF, 10],
    		[INF, 0, 3, INF],
    		[INF, INF, 0, 1],
    		[INF, INF, INF, 0]]

    print(TSP(graph))
    print("The worst case time complexity is O(n*n*(2^n)).")