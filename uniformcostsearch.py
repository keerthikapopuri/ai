from queue import PriorityQueue
gr={'a':{'b':3,'c':2},'b':{'d':6,'e':5,'a':3},'c':{'f':5,'a':2},'f':{'g':2,'c':5},'e':{'b':5},'g':{'f':2},'d':{'b':6}}
parent={'a':[]}
close=[]
path=[]
def backtrack(now,cost):
  if(cost<0):
    return
  if(cost==0):
    path.append(now)
    print(path)
    return
  close.append(now)
  path.append(now)
  for i in parent[now]:
    if i not in close:
      backtrack(i,cost-gr[now][i])
  return

def bestfirst(gr,goal):
    open_list=PriorityQueue()
    closed_list=[]
    open_list.put((0,'a'))
    while open_list.empty()==False:
        cost,now=open_list.get()
        if now==goal:
            print("min cost required is",cost)
            backtrack(goal,cost);
            break
        closed_list.append(now)
        for edge in gr[now].keys():
            if edge not in closed_list:
                open_list.put((cost+gr[now][edge],edge))
                if edge not in parent.keys():
                  parent[edge]=[now]
                else:
                  parent[edge].append(now)
    #print(closed_list)
bestfirst(gr,'g')
#print(parent)
