from queue import PriorityQueue
initial=[[1,2,3],[5,6,0],[7,8,4]]
goal=[[1,2,3],[5,8,6],[0,7,4]]
cost=0
open_list=PriorityQueue()
closed_list=[]
import copy
def heuristic(now):
  cnt=0
  for i in range(len(now)):
    for j in range(len(now)):
      if now[i][j]!=0 and now[i][j]!=goal[i][j]:
        cnt+=1
  return cnt+cost

def up(nw,i,j):
  now=copy.deepcopy(nw)
  temp=now[i-1][j]
  now[i-1][j]=now[i][j]
  now[i][j]=temp
  open_list.put((heuristic(now),now))
def down(nw,i,j):
  #print("down")
  now=copy.deepcopy(nw)
  temp=now[i+1][j]
  now[i+1][j]=now[i][j]
  now[i][j]=temp
  open_list.put((heuristic(now),now))
def left(nw,i,j):
  #print("left")
  now=copy.deepcopy(nw)
  temp=now[i][j-1]
  now[i][j-1]=now[i][j]
  now[i][j]=temp
  open_list.put((heuristic(now),now))
def right(nw,i,j):
  now=copy.deepcopy(nw)
  temp=now[i][j+1]
  now[i][j+1]=now[i][j]
  now[i][j]=temp
  open_list.put((heuristic(now),now))

def possibleiter(now):
  global cost
  cost=cost+1
  for i in range(len(now)):
    for j in range(len(now)):
      if now[i][j]==0:
        x=i
        y=j
  if x==0 and y==0:
    right(now,x,y)
    down(now,x,y)
  if x==0 and y==1:
    left(now,x,y)
    right(now,x,y)
    down(now,x,y)
  if x==0 and y==2:
    left(now,x,y)
    down(now,x,y)
  if x==1 and y==0:
    right(now,x,y)
    down(now,x,y)
    up(now,x,y)
  if x==1 and y==1:
    left(now,x,y)
    right(now,x,y)
    down(now,x,y)
    up(now,x,y)
  if x==1 and y==2:
    down(now,x,y)
    up(now,x,y)
    left(now,x,y)
  if x==2 and y==0:
    right(now,x,y)
    up(now,x,y)
  if x==2 and y==1:
    left(now,x,y)
    right(now,x,y)
    up(now,x,y)
  if x==2 and y==2:
    left(now,x,y)
    up(now,x,y)
def astar(goal):
    open_list.put((0,initial))
    while open_list.empty()==False:
        heu_cost,now=open_list.get()
        if now==goal:
            print("min cost required is",cost)
            break
        closed_list.append(now)
        possibleiter(now)
astar(goal)
print(closed_list)
