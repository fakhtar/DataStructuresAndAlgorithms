# Uses python3
import sys

def optimal_knapsack(Weight, values):
    len_val = len(values)
    for i in range(1,len_val + 1):
        for j in range(1,Weight+1):
            #print(twod_list[i][j])\
            if j >= values[i-1]:
                twod_list[i][j] = max(twod_list[i-1][j], twod_list[i-1][j - values[i-1]] + values[i-1])
            else:
                twod_list[i][j] = twod_list[i-1][j]
    return twod_list[len_val][Weight]

if __name__ == '__main__':
    input = sys.stdin.read()
    Weight, n, *values = list(map(int, input.split()))
    twod_list = []                 
    for i in range (0, n+1):                        
        new = []                
        for j in range (0, Weight+1):
            if i == 0  or j == 0:
                new.append(0)
            else:   
                new.append(-1)       
        twod_list.append(new)
    print(optimal_knapsack(Weight, values))
