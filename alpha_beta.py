import math
path=[]
def minimax (curDepth,maxTurn, scores,targetDepth,alpha,beta):
  if (curDepth == targetDepth):
    if(maxTurn):
      path.append(scores)
      return max(scores)
    else:
      path.append(scores)
      return min(scores)
  if (maxTurn):
    maxnow=float('-inf')
    for i in scores:
      maxnow=max(maxnow,minimax(curDepth + 1,False, i, targetDepth,alpha,beta))
      alpha=max(alpha,maxnow)
      if beta<=alpha:
        break
    return maxnow
  else:
    minnow=float('inf')
    for i in scores:
      minnow=min(minnow,minimax(curDepth + 1,True, i, targetDepth,alpha,beta))
      beta=min(beta,minnow)
      if beta<=alpha:
        break
    return minnow
scores = [[[8,9],[10,11]],[[4,5],[6,7],[2,3]]]
treeDepth = 3
print("The optimal value is : ", end = "")
alpha=float('-inf')
beta=float('inf')
print(minimax(1, True, scores, treeDepth,alpha,beta))
print(path)
