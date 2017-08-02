#binary to decimal converter

def binary_to_decimal(binary_list, binary_length):
    index = 0
    power = binary_length -1
    total = 0
##  print(binary_list)
##  print(binary_length)
    while power >= 0:
        total += (int(binary_list[index])) * (2**power)
        power -= 1
        index += 1
    print(total)

def main():
    loop = 0
    while loop == 0:
        switch = 0
        while switch == 0:
            binary_number = str(input("Please input some binary number:"))
            binary_number_list = list(binary_number)
##          print(binary_number)
##          print(binary_number_list)
##          print(binary_number_list[0])
            binary_length = len(binary_number_list)
##          print(binary_length)
            for bit in binary_number_list:
                if int(bit) > 1:
                    print("please enter legit binary number")
                    print("")
                else:
                    switch = 1

        #If all goes well,
        binary_to_decimal(binary_number_list, binary_length)
            


main()
