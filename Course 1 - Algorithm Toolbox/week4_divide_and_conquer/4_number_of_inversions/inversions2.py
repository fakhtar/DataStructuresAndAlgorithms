# Uses python3
import sys
import math

def merge4(L,R,numInv):
    midindex = len(L)
    arr = []
    i = j = 0
    while i < len(L) and j < len(R): 
        if L[i] < R[j]: 
            arr.append(L[i]) 
            i+= 1
        elif L[i] > R[j]:
            numInv += midindex - i
            arr.append(R[j]) 
            j+= 1
        else:            
            arr.append(R[j]) 
            i+= 1
        
    # Checking if any element was left 
    while i < len(L): 
        arr.append(L[i]) 
        i+= 1

        
    while j < len(R): 
        arr.append(R[j]) 
        j+= 1
    return arr, numInv

def merge_sort4(arr):
    len_arr = len(arr)
    if len_arr == 1:
        return arr, 0
    arr_len_div_2 = math.ceil(len_arr/2)
    x, xinv = merge_sort4(arr[0:arr_len_div_2])
    y, yinv = merge_sort4(arr[arr_len_div_2:len_arr])
    return merge4(x,y,xinv+yinv)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # b = n * [0]
    print(merge_sort4(a)[1])
