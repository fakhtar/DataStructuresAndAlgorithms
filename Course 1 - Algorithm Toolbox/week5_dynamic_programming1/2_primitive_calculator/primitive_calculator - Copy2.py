# Uses python3
import sys

def optimal_sequence(n):
    min_seq = [0]*n
    if n == 1:
        min_seq[0] = (1,1)
    elif n == 2:
        min_seq[0] = (1,1)
        min_seq[1] = (1,2)
    else:
        min_seq[0] = (1,1)
        min_seq[1] = (1,2)
        min_seq[2] = (1,3)
    for index in range(3,n):
        number = index + 1
        data = []
        data.append((min_seq[(index-1)][0],1))
        if number % 2 == 0: 
             data.append((min_seq[(number//2) -1][0],2))
        if number % 3 == 0:
             data.append((min_seq[(number//3) -1][0],3))
        my_min = min(data, key = lambda t: t[0])
        min_seq[index] = my_min[0] + 1,my_min[1]
    sequence = []
    while n != 0:
        sequence.append(n)
        z = min_seq[n-1]
        if z[1] != 1:
            n = n//z[1]
        else:
            n = n - z[1]
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
