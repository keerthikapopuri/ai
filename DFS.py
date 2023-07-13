open_list=[]
closed_list=[]
def dfs(l,open_list,closed_list,goal):
    now=open_list[0]
    open_list.remove(now)
    if(now==goal):
        return
    if(now not in l.keys()):
        closed_list.append(now)
        dfs(l,open_list,closed_list,goal)
    if now not in closed_list:
        temp=l[now]
        #print(now)
        temp.reverse()
        for i in temp:
            if i not in open_list and i not in closed_list:
                open_list.insert(0,i)
            #print(open_list)
        closed_list.append(now)
        dfs(l,open_list,closed_list,goal)
l={"A":["B","C","D"],"B":["E","F"],"C":["F","G"]}
open_list.append("A")
goal="G"
dfs(l,open_list,closed_list,goal)
closed_list.reverse()
print(closed_list)
print(open_list)
