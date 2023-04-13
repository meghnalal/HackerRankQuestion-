'''Backtracking is a useful technique to solve problems that require finding all (or some)
solutions to a problem that incrementally builds candidates to the solutions, and abandons
a candidate ("backtracks") as soon as it determines that the candidate cannot be part of a
solution.

One of the reasons you may use backtracking is when you don't know how many steps you need
to take to find a solution or when you need to explore all possible solutions. It is often
used to solve problems that involve combinatorial search, such as finding all possible
combinations, permutations, or subsets of a set of items.

Backtracking is often more efficient than generating all possible combinations and then
testing them because it prunes the search tree as soon as it determines that a branch
cannot lead to a solution.

In contrast, looping through all possible combinations can take a lot of time and memory,
especially when the size of the input grows.

Overall, backtracking can be a powerful tool when used in the right situations.'''

candidates=[2,3,4,5,6]
targets=7

res=[]
def dfs(i,cur,total):
    #the pruning
    if total == targets:
        res.append(cur.copy())
        return res
    if i >= len(candidates) or  total > targets:
        return res
    #appends the current candidates [2]
    cur.append(candidates[i])
    #and it adds the weight of [2] [accepting weight scenario] -cur=[2] total=[0+2]
    # cur=[2]
    # cur=[2,2]
    # cur=[2,2,2]
    # cur=[2,2,2,2] = 8 exist and comes to this
    # now we increase index i=1 means =3
    # cur=[2,2,2]
    # cur=[2,2,2,3] no
    # cur=[2,2,2,4] and so on
    dfs(i,cur,total+candidates[i])
    cur.pop() # removes last element
    dfs(i+1,cur,total)

dfs(0,[],0)
print(res)