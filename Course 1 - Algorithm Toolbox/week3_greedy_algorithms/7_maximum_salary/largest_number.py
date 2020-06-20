#Uses python3

import sys

def largest_number(my_arr):
    n = len(my_arr) 
    for i in range(n-1):   
        for j in range(0, n-i-1): 
            if int(str(my_arr[j]) + str(my_arr[j+1])) < int(str(my_arr[j+1]) + str(my_arr[j])) : 
                my_arr[j], my_arr[j+1] = my_arr[j+1], my_arr[j]
    my_str_arr = []
    for item in my_arr:
        my_str_arr.append(str(item))
    return ''.join(my_str_arr)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))