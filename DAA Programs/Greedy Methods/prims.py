# Python 3 program for Prim's Algorithm
# Returns the local optimum in the hopes of finding a global optimum.

def main():
    V = 5

    G = [[0, 9, 75, 0, 0],
         [9, 0, 95, 19, 42],
         [75, 95, 0, 51, 66],
         [0, 19, 51, 0, 31],
         [0, 42, 66, 31, 0]]

    selected = [0 for _ in range(V)]
    no_edge = 0
    selected[0] = True
    print("Edge : Weight\n")
    while (no_edge < V - 1):
        minimum = float("inf")
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):  
                        # not in selected and there is an edge
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
        selected[y] = True
        no_edge += 1

if __name__ == "__main__":
    main()
    print("The worst case time complexity of Prim's Algorithm is O((|E|+|V|)log|V|) in case of Adjacency List while O(|V|*|V|) in case of Adjacency Matrix.")