gr={0:[5,1,2,11],5:[0,6,7],1:[7,0,3],7:[8,1],3:[9,4,1],2:[0,10,12],11:[0],6:[5],8:[7],9:[3],4:[3],10:[2],12:[2]}
open_list1=[]
closed_list1=[]
def bfs(gr,open_list,closed_list):
    now=open_list[0]
    open_list.remove(now)
    if(now not in gr.keys()):
        closed_list.append(now)
    if now not in closed_list:
        temp=gr[now]
        #print(now)
        for i in temp:
            if i not in open_list:
                open_list.append(i)
        closed_list.append(now)
open_list2=[]
closed_list2=[]
open_list1.append(5)
open_list2.append(4)
def intersection_list(list1, list2):
   list3 = [value for value in list1 if value in list2]
   return list3
def intersection(l1,l2):
    if len(intersection_list(l1, l2)):
        return True
    return False
while(not intersection(open_list1,open_list2)):
    bfs(gr,open_list1,closed_list1)
    bfs(gr,open_list2,closed_list2)
print(intersection_list(open_list1, open_list2))
print(closed_list1)
print(closed_list2)
