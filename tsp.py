def solve(dist, visited, city, arr):
    if visited == arr:
        return dist[city][0]
    mini = 1e9
    for i in range(len(visited)):
        if visited[i] == 0:
            visited[i] = 1
            ans = dist[city][i]+solve(dist, visited, i, arr)
            mini = min(mini, ans)
            visited[i] = 0
    return mini


n = int(input("enter number of cities:"))
arr = [1]*n
visited = [0]*n
dist = [[0, 20, 42, 25], [20, 0, 30, 34], [42, 30, 0, 10], [25, 34, 10, 0]]
print(solve(dist, visited, 0, arr))
