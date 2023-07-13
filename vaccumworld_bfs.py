from queue import Queue

# Initializing a queue
queue = Queue()
c=0
visited=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
mat=[[1,0,0,0],[0,1,0,1],[1,0,1,1]]
queue.put((0,0))
while(not queue.empty()):
  i,j=queue.get()
  #print(i)
  #print(j)
  if(i<0 or j<0 or i>=len(mat) or j>=len(mat[0])):
    #print("entered")
    continue
  if(visited[i][j]):
    #print("entered")
    continue
  visited[i][j]=1
  if(mat[i][j]==0):
    c+=1
  else:
    c+=2
  mat[i][j]=0
  print(mat)
  queue.put((i+1,j))
  queue.put((i,j+1))
  queue.put((i-1,j))
  queue.put((i,j-1))
print(c-1)
