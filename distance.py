
from collections import deque
def bestdistance(mat):
    rows=len(mat)
    cols=len(mat[0])
    if mat[0][0]=='1' or mat[rows-1][cols-1]=='1':
        return -1
    parents={}
    directions=[(-1,0),(1,0),(0,1),(0,-1)] #up,down,right,left
    visited=[[False for _ in range(cols)] for _ in range(rows)]
    queue=deque()
    queue.append((0,0,0))
    visited[0][0]=True
    while queue:
        r,c,step=queue.popleft()
        if (r,c)==(rows-1,cols-1):
            path=[]
            curr=(r,c)
            while curr != (0,0):
                path.append(curr)
                curr=parents[curr]
            path.append((0,0))
            path.reverse()
            return path,step
        for dr,dc in directions:
            nr= r+dr
            nc=c+dc
            if nr >= 0 and nr < rows and nc >=0 and nc < cols and mat[nr][nc]=='0' and not visited[nr][nc]:
                parents[(nr,nc)]=(r,c)
                visited[nr][nc]=True
                queue.append((nr,nc,step+1))
    return -1
    
grid = [
        ['0', '0', '1', '0'],
        ['1', '0', '0', '0'],
        ['1', '0', '1', '0'],
        ['0', '0', '0', '0']
    ]
sol=bestdistance(grid)
print(sol)


    