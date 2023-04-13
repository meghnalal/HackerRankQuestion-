'''subset backtracking way '''

candidates=[1,2,3]
res=[]
subset=[]
def dfs(i):
    if i >= len(candidates) :
        res.append(subset.copy())
        return
    subset.append(candidates[i])
    dfs(i+1)
    subset.pop()
    dfs(i+1)

dfs(0)
print(res)

''' '''

