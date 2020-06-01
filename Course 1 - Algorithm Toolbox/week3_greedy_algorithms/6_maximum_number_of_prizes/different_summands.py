# Uses python3
import sys

def optimal_summands(num_provided):
    num = 0
    numbers_picked = set()
    while num_provided != 0:
        num += 1
        num_provided -= num
        numbers_picked.add(num)
        if num_provided in numbers_picked:
            numbers_picked.remove(num)
            num_provided += num
            numbers_picked.add(num_provided)
            break
    return numbers_picked

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
