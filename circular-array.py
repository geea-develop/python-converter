
arr = []

arr_length = len(arr)

front_index = 0
back_index = arr_length

def push_to_front(num):
    front_index = (front_index-1)%arr_length
    arr[front_index] = num

def push_to_back(num):
    back_index = (front_index+1)%arr_length
    arr[back_index] = num