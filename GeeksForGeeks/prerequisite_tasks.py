from collections import defaultdict
class Solution:
    def isPossible(self,N,prerequisites):
        adj = defaultdict(set)
        for u,v in prerequisites:
            adj[u].add(v)
        vis = [0]*N
        def dfs(u):
            vis[u] = 1
            for v in adj[u]:
                if vis[v] == 0:
                    if dfs(v) == False:
                        return False
                elif vis[v] == 1:
                    return False
            vis[u] = 2
            return True
        for i in range(N):
            if vis[i] == 0:
                if dfs(i) == False:
                    return False
        return True