#Other Bases to decimal converter

def OB_to_decimal(OB_list, OB_length, bases):
    index = 0
    power = OB_length -1
    total = 0
    while power >= 0:
        total += (int(OB_list[index])) * (bases**power)
        power -= 1
        index += 1
    print(total)

def main():
    OB_number = str(input("Please input some number:"))
    OB_number_list = list(OB_number)
    OB_length = len(OB_number_list)
    b = input("Please input the base:")

    #If all goes well,
    OB_to_decimal(OB_number_list, OB_length, b)
            
main()
