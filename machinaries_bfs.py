open_list=[]
closed_list=[]
def move(s):
  if s[0][2]==1:
    #move from left side to right side
    #moving 2 machinaries
    if ((s[0][0]-2>0 and s[0][0]-2>=s[0][1]) or s[0][0]-2==0) and s[1][0]+2>=s[1][1]:
      open_list.append([[s[0][0]-2,s[0][1],0],[s[1][0]+2,s[1][1],1]])
      #moving 2 cannibals
    if s[0][1]-2>=0 and ((s[0][0]>=s[0][1]-2 and s[0][0]!=0) or s[0][0]==0) and ((s[1][0]!=0 and s[1][1]+2<=s[1][0]) or s[1][0]==0):
      open_list.append([[s[0][0],s[0][1]-2,0],[s[1][0],s[1][1]+2,1]])
      #moving 1 machinary and 1 cannibal
    if s[0][1]>=0 and ((s[0][0]-1>0 and s[0][0]-1>=s[0][1]-1) or s[0][0]-1==0) and s[1][0]+1>=s[1][1]+1:
      open_list.append([[s[0][0]-1,s[0][1]-1,0],[s[1][0]+1,s[1][1]+1,1]])
    #moving 1 machinary
    if ((s[0][0]-1>0 and s[0][0]-1>=s[0][1]) or s[0][0]-1==0) and s[1][0]+1>=s[1][1]:
      open_list.append([[s[0][0]-1,s[0][1],0],[s[1][0]+1,s[1][1],1]])
    #moving 1 cannibal
    if s[0][1]-1>=0 and ((s[0][0]>=s[0][1]-1 and s[0][0]!=0) or s[0][0]==0) and ((s[1][0]!=0 and s[1][0]>=s[1][1]+1) or s[1][0]==0):
      open_list.append([[s[0][0],s[0][1]-1,0],[s[1][0],s[1][1]+1,1]])
  else:
    #move from right side to left side
    #moving 2 machinaries
    if ((s[1][0]-2>0 and s[1][0]-2>=s[1][1]) or s[1][0]-2==0) and s[0][0]+2>=s[0][1]:
      open_list.append([[s[0][0]+2,s[0][1],1],[s[1][0]-2,s[1][1],0]])
      #moving 2 cannibals
    if s[1][1]-2>=0 and ((s[1][0]!=0 and s[1][0]>=s[1][1]-2) or s[1][0]==0) and ((s[0][1]+2<=s[0][0] and s[0][0]!=0) or s[0][0]==0):
      open_list.append([[s[0][0],s[0][1]+2,1],[s[1][0],s[1][1]-2,0]])
      #moving 1 machinary and 1 cannibal
    if s[1][1]>=0 and ((s[1][0]-1>0 and  s[1][0]-1>=s[1][1]-1) or s[1][0]-1==0) and s[0][0]+1>=s[0][1]+1:
      open_list.append([[s[0][0]+1,s[0][1]+1,1],[s[1][0]-1,s[1][1]-1,0]])
    #moving 1 machinary
    if ((s[1][0]-1>0 and s[1][0]-1>=s[1][1]) or s[1][0]-1==0) and s[0][0]+1>=s[0][1]:
      open_list.append([[s[0][0]+1,s[0][1],1],[s[1][0]-1,s[1][1],0]])
    #moving 1 cannibal
    if s[1][1]-1>=0 and ((s[1][0]!=0 and s[1][0]>=s[1][1]-1) or s[1][0]==0)  and ((s[0][0]>=s[0][1]+1 and s[0][0]!=0) or s[0][0]==0):
      open_list.append([[s[0][0],s[0][1]+1,1],[s[1][0],s[1][1]-1,0]])
path=[]
def bfs(open_list,closed_list,goal):
    now=open_list[0]
    open_list.remove(now)
    if(now==goal):
        print("reached")
        return
    if now in closed_list:
        bfs(open_list,closed_list,goal)
    if now not in closed_list:
        move(now)
        closed_list.append(now)
        bfs(open_list,closed_list,goal)
        path.append(now)
initial=[[3,3,1],[0,0,0]]
move(initial)
closed_list.append(initial)
goal=[[0,0,0],[3,3,1]]
bfs(open_list,closed_list,goal)
print(closed_list)
