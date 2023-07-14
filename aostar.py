def AOstar(g,c):
  kys=list(c.keys())[::-1]
  for key in kys:
    edges=c[key]
    l=[]
    condn=edges.keys()
    for cond in condn:
      for ind in range(len(edges[cond])):
        edges[cond][ind]=g[edges[cond][ind]]+1
      if cond=='OR':
        l.append(min(edges[cond]))
      else:
        now=0
        for i in range(len(edges[cond])):
          now+=edges[cond][i]
        l.append(now)
        edges[cond]=now
    g[key]=min(l)

g={'A':0,'B': 0,'C': 0,'D': 0,'E': 7,'F': 9,'G': 3,'H': 0,'I': 0,'J': 0}
c={'A': {'OR': ['B'], 'AND': ['C', 'D']},'B': {'OR': ['E', 'F']},'C': {'OR': ['G'],'AND':['H','I']},'D': {'OR': ['J']}}
AOstar(g,c)
print(g)
