
input_bits_str = input("Lets collect some strings...\n")

convert_from = input("What format whould you like to convert from? hex/oct/bin \n")

if convert == "bin":
    # Binary
    print(int("0b" + input_bits_str, 2))

if convert == "oct":
    # Octa
    print(int("0o" + input_bits_str, 8))

if convert == "hex":
    # Hexa
    print(int("0x" + input_bits_str, 16))

print("Done.")