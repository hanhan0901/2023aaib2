#week10-1.py 函式呼叫函式遞迴
N=int(input('請輸入N:'))
#以前適用 for迴圈寫, 今天用函式呼叫函式來寫
def func(n):
  if n==1: return 1 #終止條件,像數學歸納法 N=1成立
  return n * func(n-1) #函式呼叫函式,把大問題,改成去問小問題
ans=func(N)
print(ans)
