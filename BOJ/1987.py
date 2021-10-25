import sys
input = sys.stdin.readlines

n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [False]*26

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
def dfs(g, v, x, y, c):
  global result
  result = max(c, result)

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<m and not v[ord(g[nx][ny])-65]:
      v[ord(g[nx][ny])-65] = True
      dfs(g, v, nx, ny, c+1)
      v[ord(g[nx][ny])-65] = False # 백트래킹시 방문 취소
  return True

visited[ord(graph[0][0])-65] = True
dfs(graph, visited, 0, 0, 1)  # 시작점 포함해서 c=1로 시작
print(result)
