import itertools
l=[]
w1=input()
w2=input()
w3=input()
carry=0
if(len(w1)+1==len(w3)):
  carry=1
l.extend(list(set(w1)))
l.extend(list(set(w2)))
l.extend(list(set(w3)))
l=set(l)
l=tuple(l)
digits=range(10)
def val(w,d):
  c=0
  n=len(w)
  for i in range(n):
    c+=10**(n-1)*d[w[i]]
    n-=1
  return c
for j in itertools.permutations(digits,len(l)):
  d=dict(zip(l,j))
  if d[w1[0]]!=0 and d[w2[0]]!=0 and d[w3[0]]==carry:
    k1=val(w1,d)
    k2=val(w2,d)
    k3=val(w3,d)
    if(k1+k2==k3):
      print(k1,"+",k2,"=",k3)
      break
