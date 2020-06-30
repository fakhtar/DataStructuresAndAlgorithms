# # Uses python3
import sys
import itertools

# def partition3(A):
#     for c in itertools.product(range(3), repeat=len(A)):
#         sums = [None] * 3
#         for i in range(3):
#             sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

#         if sums[0] == sums[1] and sums[1] == sums[2]:
#             return 1

#     return 0

def part_three_ways(my_array): 
    number_of_elements = len(my_array) 
    my_sum = 0
    j = 0
    i = 0
    for i in range(number_of_elements): 
        my_sum += my_array[i] 
    if my_sum % 3 != 0: 
        return 0 
    two_d_array = [[ True for i in range(number_of_elements + 1)]  
                   for j in range(my_sum // 3 + 1)] 
    for i in range(0, n + 1): 
        two_d_array[0][i] = True
    for i in range(1, my_sum // 3 + 1): 
        two_d_array[i][0] = False 
    for i in range(1, my_sum // 3 + 1):           
        for j in range(1, n + 1): 
            two_d_array[i][j] = two_d_array[i][j - 1] 
            if i >= my_array[j - 1]: 
                two_d_array[i][j] = (two_d_array[i][j] or 
                              two_d_array[i - my_array[j - 1]][j - 1]) 
    if two_d_array[my_sum // 3][n] == True:
        return 1      
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(part_three_ways(A))

