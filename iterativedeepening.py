graph={1:[2,3],2:[4,5],3:[6,7],4:[8,9],5:[10,11]}
n=int(input("enter number of nodes"))
goal=11
def dfid(graph,goal,n):
    depth=1
    l=[1]
    while(depth<=n):
        p=[]
        for j in l:
            if j in graph.keys():
                for i in graph[j]:
                    if i not in l:
                        p.append(i)
                        if i==goal:
                          return depth
            l=l+p
            print(l)
        depth=depth+1
    return -1;
ans=dfid(graph,goal,n)
if(ans==-1):
    print("not found")
else:
    print("found at depth",ans)
