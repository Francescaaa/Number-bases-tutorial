#Octal to binary

n = str(input("Please input a octal number:"))
n_list = list(n)
binary = ["000","001","010","011","100","101","110","111"]
output =[]
for i in n_list:
    output.append(binary[int(i)])
print("".join(output))

