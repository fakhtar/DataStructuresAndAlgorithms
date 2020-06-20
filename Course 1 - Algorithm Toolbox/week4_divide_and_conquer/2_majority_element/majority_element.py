# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def majority_element(arr,left,right):
    my_dict = {}
    arr_len_div2 = right/2
    for item in arr:
        if item in my_dict:
            my_dict[item] += 1
            if my_dict[item] > arr_len_div2:
                return 1
        else:
            my_dict[item] = 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
