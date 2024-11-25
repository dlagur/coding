import sys

INF = sys.maximize

def Floyd_Warshall():
    dist = [[INF]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = a[i][j]

    for k in range(n): 
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

