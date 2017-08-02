n = int(input('please enter the no. in the decimal format:'))
b = int(input('please enter the base.'))
x = n
k = []
while (n > 0):
    a = int(float(n%b))
    k.append(a)
    n = (n - a)/b
k.append(0)
string=""
for j in k[::-1]:
    string = string + str(j)
print('The base for %d is %s'%(x,string))

