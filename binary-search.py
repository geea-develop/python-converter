import math

input_num_str = input("Lets collect a some numbers...\n")
numbers = [int(_) for _ in input_num_str.split(" ")]
numbers.sort()
input_num_str = input("Please insert a number to check if it exists exists...\n")
some_number = int(input_num_str)
found = False
start_index = 0
end_index = len(numbers)

while not found:
    check_index = (start_index + end_index) / 2
    # round down
    check_index = math.floor(check_index)
    check_index = check_index

    # this is the last element
    if check_index > (len(numbers) - 1):
        break

    check_number = numbers[check_index]
    if check_number == some_number:
        found = True
        break
    
    # this is the last element
    if start_index == end_index:
        break

    if check_number > some_number:
        # check lower half
        end_index = check_index-1
    else:
        # check upper half
        start_index = check_index+1

print(f"Is Found? {found}")


