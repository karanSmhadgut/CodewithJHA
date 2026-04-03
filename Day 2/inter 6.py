name='nitin'

n=len(name)
nname=''

for i in range(n-1,-1,-1):
    nname += name[i]
    
if name==nname:
    print('palindrme')
else:
    print('not palindrome')