from queue import PriorityQueue
def greedybestfirstsearch(gr,goal,heuristic):
    open_list=PriorityQueue()
    closed_list=[]
    open_list.put((8,'A',0))
    while open_list.empty()==False:
        heu_cost,now,cost=open_list.get()
        if now==goal:
            print("min cost required is",cost)
            break
        closed_list.append(now)
        for edge in gr[now].keys():
            if edge not in closed_list:
                open_list.put((heuristic[edge],edge,cost+gr[now][edge]))
    print(closed_list)
graph={'A':{'B':1,'C':2},'B':{'D':7,'E':9,'F':4},'C':{'G':4,'H':3,'I':6,'J':8},'H':{'I':1}}
heuristic={'A':8,'B':10,'C':4,'D':15,'E':14,'F':12,'G':7,'H':2,'I':0,'J':4}
greedybestfirstsearch(graph,'I',heuristic)
