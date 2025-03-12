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
    # makes sure alphabetical characters are in the right case
    hex = hex.lower()
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
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15
    }
    # exponent to raise 16 to
    expo = len(hex) - 1
    # stops the recursion if no further operations are necessary
    if expo == 0:
        return hex_values[hex]
    # recursive algorithm that adds the first value multiplied by the 16 to the power of the necessary exponent
    # to the output of the function, iterating through each element and giving the final value in decimal
    else:
        return hexToDec(hex[1:]) + (hex_values[hex[0]]) * (16 ** expo)


def binToDec(bin):
    # checks whether to return a 1 or 0
    if bin == "0":
        return 0
    if bin == "1":
        return 1
    # "binToDec(bin[:-1])" recursively loops back through the function, removing the last digit of the input
    # "binToDec(bin[-1])" loops the final value back to the start of the function, returning either a 1 or 0
    return binToDec(bin[:-1]) * 2 + binToDec(bin[-1])


def decToBin(dec):
    # end point for recursion
    if dec == 1:
        return dec
    # recursive loop that divides the current value by 2, and truncates, then adds the remainder of that to the output
    else:
        return str(decToBin(dec // 2)) + str(dec % 2)


# value inputs
dec_value = int(input("Please input a decimal value: "))
hex_value = str(input("Please input a hexadecimal value: "))
bin_value = input("Please input a binary value: ")

# print statements
print("Decimal to Hexadecimal:", decToHex(dec_value))
print("Hexadecimal to Decimal:", hexToDec(hex_value))
print("Decimal to Binary:", decToBin(dec_value))
print("Binary to Decimal:", binToDec(bin_value))
