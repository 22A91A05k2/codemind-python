n=int(input())
s=0
q=n
while n!=0:
  r=n%10
  n=n//10
  s=s*10+r
if q==s:
   print('True')
else:
   print('False')