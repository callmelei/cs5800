def subsets(n):
    '''
    Generate the subsets that no two adjacent positions are in the same subset.

    type:
    n: int
    return: [[]]
    
    '''
    
    res = []
    dfs(res, [], n, 0)
    return res

def dfs(res, path, n, start):
    '''
    Helper function to find all the qualified subsets.
    
    type:
    res: [[]]
    path: []
    n: int
    start: int
    '''
    res.append(path)
    
    for i in range(start, n):
        dfs(res, path + [i], n, i + 2)
    
    return

R, C = 2, 2
happiness = [[5, 0],
             [10, 6]]

S = subsets(C)

# Find compatible arrangements between two rows
matches = dict()
for i, p in enumerate(S):
    matches[i] = []
    for j, q in enumerate(S):
        if not set(p).intersection(set(q)):
            matches[i] += [j]

# Dynamic Programming:
# Use OPT(i,j) to presents the optimal happiness 
# when ith rowis arranged by the jth subset in S.
# Bellman equation:
# OPT(i,j) = max{OPT(i-1,*)}
OPT = []
for i, h in enumerate(happiness):
    print(i)
    tempOPT = []
    
    # Base case
    if i == 0:
        for j, s in enumerate(S):
            total = sum([h[x] for x in s])
            tempOPT.append(total)
    else:
        # Recursion
        for j, s in enumerate(S):
            currentRow = sum([h[x] for x in s])
            previous = max([OPT[i-1][y] for y in matches[j]])
            total = currentRow + previous
            tempOPT.append(total)
        
    OPT.append(tempOPT)
    
print(max(OPT[-1]))
        