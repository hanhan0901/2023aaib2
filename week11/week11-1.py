#week11-1.py ��python���n�h�j�~����2�U�ӽ��
def isPrime(n):
  for i in range(2,n):
    if n%i==0: return False
  return True

BOUND=300000
ans=0
for i in range(2,BOUND):
  if isPrime(i):
    print(i,end=' ')
    ans += 1
print()
print('��Ʀ�:',ans,'��')
