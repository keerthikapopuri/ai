import math
def minimax (curDepth,maxTurn, scores,targetDepth):
  if (curDepth == targetDepth):
    if(maxTurn):
      return max(scores)
    else:
      return min(scores)
  if (maxTurn):
    maxnow=float('-inf')
    for i in scores:
      maxnow=max(maxnow,minimax(curDepth + 1,False, i, targetDepth))
    return maxnow
  else:
    minnow=float('inf')
    for i in scores:
      minnow=min(minnow,minimax(curDepth + 1,True, i, targetDepth))
    return minnow
scores = [[[2,3,4],[4,5],[6,7]],[[8,9],[10,11]]]
treeDepth = 3
print("The optimal value is : ", end = "")
print(minimax(1, True, scores, treeDepth))
