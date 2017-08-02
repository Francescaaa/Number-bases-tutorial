n=int(input('please enter the no. in decimal format: '))
x=n
k=[] #empty list
while (n>0):
    a=int(float(n%2)) #remainder
    k.append(a)
    n=(n-a)/2 #quotient
k.append(0) # append 0 becus reverse slice excludes end index
string=""
for j in k[::-1]: # reverse slice
    string=string+str(j)
print('The binary no. for %d is %s'%(x, string))
