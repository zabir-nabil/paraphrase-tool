global vis
global edges

def dfs(node, dfs_tag):
	global vis, edges


	if vis[node] == dfs_tag:
		return True
	vis[node] = dfs_tag
	print(node)
	print(vis)
	print("---")
	for n in edges[node]:
		p = dfs(n, dfs_tag)
		if p == True:
			print("found")
			print(vis)
			print(dfs_tag)
			print(n, node)
			return p

	return False

def cycleInGraph(edges_l):
	global vis, edges
	edges = edges_l
	vis = [-1] * len(edges)
	dfs_tag_g = 2
	for n in range(len(edges)):
		if vis[n] == -1:
			dfs_tag_g += 1
			ans = dfs(n, dfs_tag_g)
			if ans == True:
				print("found")
				print(n)
				return ans
	return False
o = cycleInGraph([
    [1, 2],
    [2],
    []
  ])

print(o)