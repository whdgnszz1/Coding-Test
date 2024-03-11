// pseudocode
DFS(u, adj)
  u.visited = true
  for each v ∈ adj[u]
    if v.visited == false
      DFS(v, adj)