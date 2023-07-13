c=0
visited=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def dfs(mat,i,j):
  if(i<0 or j<0 or i>=len(mat) or j>=len(mat[0])):
    return
  if(visited[i][j]):
    return
  visited[i][j]=1
  global c
  if(mat[i][j]==0):
    c+=1
  else:
    c+=2
  mat[i][j]=0
  print(mat)
  dfs(mat,i+1,j)
  dfs(mat,i,j+1)
  dfs(mat,i-1,j)
  dfs(mat,i,j-1)
mat=[[1,0,0,0],[0,1,0,1],[1,0,1,1]]
dfs(mat,0,0)
print(c-1)
