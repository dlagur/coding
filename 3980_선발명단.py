from sys import stdin
input = stdin.readline

def perm(player, score):
    global max_score
    if player == 11:
        max_score = max(max_score, score)
        return
    for i in range(11):
        if visited[i] or not graph[player][i]:
            continue
        visited[i] = 1
        order[player] = i
        perm(player+1, score+graph[player][i])
        order[player] -= 1
        visited[i] = 0

T = int(input())
for _ in range(T):
    graph = [list(map(int, input().split())) for _ in range(11)]
    max_score = 0
    order = [0]*11
    visited = [0]*11
    perm(0,0)
    print(max_score)
