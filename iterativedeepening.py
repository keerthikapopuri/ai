gr={'A':['B','C'],'B':['D','E'],'C':['F','G']}
def DLS(src,target,maxDepth):
        if src == target : return True
        if maxDepth < 0 : return False
        if src in gr.keys():
          for i in gr[src]:
                  if(DLS(i,target,maxDepth-1)):
                      return True
        return False
def iterative(src, target, maxDepth):
    for i in range(maxDepth):
        if (DLS(src, target, i)):
            return True
    return False
iterative('A','G',2)
