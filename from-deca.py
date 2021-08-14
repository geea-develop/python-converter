input_num_str = input("Lets collect a number...\n")
if not input_num_str:
    input_num_str = "296"

convert_to = input("What format whould you like to convert to? hex/oct/bin \n")

if convert_to == "bin":
    # convert string to num to binary. then remove leading 0b
    print(bin(int(input_num_str))[2:])

if convert_to == "oct":
    # convert string to num to octa. then remove leading 0o
    print(oct(int(input_num_str))[2:])

if convert_to == "hex":
    # convert string to num to hexa. then remove leading 0x
    print(hex(int(input_num_str))[2:])

print("Done.")