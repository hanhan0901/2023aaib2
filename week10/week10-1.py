#week10-1.py �禡�I�s�禡���j
N=int(input('�п�JN:'))
#�H�e�A�� for�j��g, ���ѥΨ禡�I�s�禡�Ӽg
def func(n):
  if n==1: return 1 #�פ����,���ƾ��k�Ǫk N=1����
  return n * func(n-1) #�禡�I�s�禡,��j���D,�令�h�ݤp���D
ans=func(N)
print(ans)
