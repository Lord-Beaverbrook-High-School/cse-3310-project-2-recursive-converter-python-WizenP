
def binToDec(bin):
    if bin == "0":
        return 0
    if bin == "1":
        return 1
    return binToDec(bin[:-1]) * 2 + binToDec(bin[-1])


def decToBin(dec):
    end_string = ""
    if dec > 1:
        decToBin(dec // 2)
    end_string += str(dec % 2)


value = input("Please input a binary value: ")
print(binToDec(value))