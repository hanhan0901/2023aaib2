#week11-2.py �n�οz�l�k
#�H�e���g�k,�n30�U*30�U=900����
#�οz�l�k,�u�n30�U+���������Ǯ�l,��20�U��
BOUND=300000
table=[True]*BOUND
ans=0
for i in range(2,BOUND):
  if table[i]==True:
    #print(i,end=' ')
    ans += 1
    for k in range(i*i,BOUND,i):
      table[k]=False
print('��Ʀ�:',ans,'��')
