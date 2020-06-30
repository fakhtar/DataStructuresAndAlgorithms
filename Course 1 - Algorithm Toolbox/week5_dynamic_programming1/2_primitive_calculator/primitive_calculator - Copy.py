# Uses python3
import sys

def optimal_sequence(n):
    min_seq = [0]*n
    min_seq[0] = 1
    min_seq[1] = 1
    min_seq[2] = 1
    for index in range(3,n):
        number = index + 1
        data = []
        data.append(min_seq[(index-1)])
        if number % 2 == 0: 
             data.append(min_seq[(number//2) -1])
        if number % 3 == 0:
             data.append(min_seq[(number//3) -1])
        my_min = min(data)
        min_seq[index] = my_min + 1
    # min_seq[0] = (1,1)
    # min_seq[1] = (1,2)
    # min_seq[2] = (1,3)
    # for index in range(3,n):
    #     number = index + 1
    #     data = [] 
    #     data.append(min_seq[(index-1)])
    #     if number % 2 == 0: 
    #         data.append(min_seq[(number//2) -1])
    #     if number % 3 == 0:
    #         data.append(min_seq[(number//3) -1])
    #     my_min = min(data, key = lambda t: t[0])
    #     min_seq[index] = my_min[0] + 1, my_min[1]
        # if number % 3 == 0:
        #     min_seq[index] = (min_seq[(number//3) -1][0] + 1,3)
        # elif number % 2 == 0:
        #     min_seq[index] = (min_seq[(number//2) -1][0] + 1,2)
        # else:
        #     min_seq[index] = (min_seq[(index-1)][0] + 1,1)
    print(min_seq[n-1])
    sequence = []
    while n != 0:
        sequence.append(n)
        z = min_seq[n-1]
        if z != 1:
            n = n//z
        else:
            n = n - z
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
