def decToHex(dec):
    # list of every hex digit
    hex_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    # returns the hex value if the current decimal number is able to be expressed in a single digit
    if dec < 16:
        return hex_values[dec]
    # recursively goes back through the method, with the decimal value being divided by 16 then truncated,
    # and adding the hexadecimal version of the "removed" value to the output, leading to a hexadecimal value
    else:
        return decToHex(dec // 16) + hex_values[dec % 16]


def hexToDec(hex):
    # dict to store the equivalents of each hex value
    hex_values = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    # exponent to raise 16 to
    expo = len(hex) - 1
    #
    if expo == 0:
        return hex_values[hex]
    else:
        return hexToDec(hex[1:]) + (hex_values[hex[0]]) * (16 ** expo)


def binToDec(bin):
    # checks whether to return a 1 or 0
    if bin == "0":
        return 0
    if bin == "1":
        return 1
    # 
    return binToDec(bin[:-1]) * 2 + binToDec(bin[-1])


def decToBin(dec):
    end_string = ""
    if dec > 1:
        decToBin(dec // 2)
    end_string += str(dec % 2)


dec_value = int(input("Please input a decimal value: "))
hex_value = input("Please input a hexadecimal value: ")
bin_value = input("Please input a binary value: ")

print(decToHex(dec_value))
print(hexToDec(hex_value))
print(decToBin(dec_value))
print(binToDec(bin_value))
