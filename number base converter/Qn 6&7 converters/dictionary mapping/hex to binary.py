#Hexadecimal to binary

n = str(input("Please input a hex number:"))
n_list = list(n)
binary = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
output =[]
print(n_list)
print(binary["C"])
for i in n_list:
    output.append(binary[str(i)])
print("".join(output))
