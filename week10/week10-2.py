#week10-2.py
def gcd(a,b):
  if a==0: return b
  if b==0: return a
  return gcd(b, a%b)
a=int(input('�п�Ja:'))
b=int(input('�п�Jb:'))
print('�̤j���]��:',gcd(a,b))
