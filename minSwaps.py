# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    #calculate the distance from destination
    distance = []
    for i in range(0,len(arr)):
        distance.append((arr[i] - 1 - i))
    #determine the swaps that mazimizes the reduced distance

    pass

my_arr = [7,1,3,2,4,5,6]
minimumSwaps(my_arr)