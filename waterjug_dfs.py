open_list=[]
closed_list=[]
path=[]
def new(li,open_list,i,j):
    if(li[0]<i):
        open_list.insert(0,[i,li[1]])
    if(li[1]<j):
        open_list.insert(0,[li[0],j])
    if(li[0]>0):
        open_list.insert(0,[0,li[1]])
    if(li[1]>0):
        open_list.insert(0,[li[0],0])
    if li[0]+li[1]<=i and li[1]>0:
        open_list.insert(0,[li[0]+li[1],0])
    if li[0]+li[1]<=j and li[0]>0:
        open_list.insert(0,[0,li[0]+li[1]])
    if li[0]+li[1]>=j and li[0]>0:
        open_list.insert(0,[li[0]-(j-li[1]),j])
    if li[0]+li[1]>=i and li[1]>0:
        open_list.insert(0,[i,li[1]-(i-li[0])])

def dfs(open_list,closed_list,goal,i,j):
    now=open_list[0]
    open_list.remove(now)
    if(now==goal):
        print("reached")
        return
    if now in closed_list:
        dfs(open_list,closed_list,goal,i,j)
    if now not in closed_list:
        new(now,open_list,i,j)
        closed_list.append(now)
        dfs(open_list,closed_list,goal,i,j)

i=int(input("enter 1st jug amount"))
j=int(input("enter 2nd jug amount"))
g=int(input("enter goal state amount"))
initial=[0,0]
goal=[g,0]
closed_list.append(initial)
new(initial,open_list,i,j)
dfs(open_list,closed_list,goal,i,j)
print(list(reversed(closed_list)))
