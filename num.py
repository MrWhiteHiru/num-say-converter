
r ='\033[91m' # red
g ='\033[92m' # green
b = '\033[94m' # blue
y = '\033[93m' # yellow
s_b ='\033[96m' # sky_blue
pi = '\033[35m' # pink
reset = '\033[0m' # reset
blink = "\033[5;92m" # blink

def bin_to_dec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal


def dec_to_bin(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal%2) + binary
        decimal //= 2
    return binary


def hex_to_dec(hexadecimal):
    decimal = 0
    for digit in hexadecimal:
        if digit.isdigit():
            decimal = decimal*16 + int(digit)
        else:
            decimal = decimal*16 + (ord(digit) - 55)
    return decimal


def dec_to_hex(decimal):
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder + 55) + hexadecimal
        decimal //= 16
    return hexadecimal

def main():
    print(g+"""
    ███╗░░██╗██╗░░░██╗███╗░░░███╗░░░░░░░██████╗░█████╗░██╗░░░██╗░░░░░░░█████╗░░█████╗░███╗░░██╗
    ████╗░██║██║░░░██║████╗░████║░░░░░░██╔════╝██╔══██╗╚██╗░██╔╝░░░░░░██╔══██╗██╔══██╗████╗░██║
    ██╔██╗██║██║░░░██║██╔████╔██║█████╗╚█████╗░███████║░╚████╔╝░█████╗██║░░╚═╝██║░░██║██╔██╗██║
    ██║╚████║██║░░░██║██║╚██╔╝██║╚════╝░╚═══██╗██╔══██║░░╚██╔╝░░╚════╝██║░░██╗██║░░██║██║╚████║
    ██║░╚███║╚██████╔╝██║░╚═╝░██║░░░░░░██████╔╝██║░░██║░░░██║░░░░░░░░░╚█████╔╝╚█████╔╝██║░╚███║
    ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░░░░░╚════╝░░╚════╝░╚═╝░░╚══╝
    """)
    print(b+"                                                                 [#] Tool by : MR WHITE HIRU")
    print(y+"Choose an option:")
    print(y+"[1] Binary to Decimal          ")
    print(y+"[2] Decimal to Binary")
    print(y+"[3] Hexadecimal to Decimal")
    print(y+"[4] Decimal to Hexadecimal"+reset)
    option = int(input(g+"Enter your choice: "))
    if option == 1:
        binary = input("[#] Enter a binary number: ")
        decimal = bin_to_dec(binary)
        print("[*] Decimal equivalent: ", decimal)
    elif option == 2:
        decimal = int(input("[#] Enter a decimal number: "))
        binary = dec_to_bin(decimal)
        print("[*] Binary equivalent: ", binary)
    elif option == 3:
        hexadecimal = input("[#] Enter a hexadecimal number: ")
        decimal = hex_to_dec(hexadecimal)
        print("[*]Decimal equivalent: ", decimal)
    elif option == 4:
        decimal = int(input("[#] Enter a decimal number: "))
        hexadecimal = dec_to_hex(decimal)
        print("[*] Hexadecimal equivalent: ", hexadecimal)
    else:
        print(r+"[!] Invalid option. Please try again.")

if __name__ == '__main__':
    main()
