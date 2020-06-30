# Uses python3
import sys

def get_change(m):
    coin1 = 1
    coin2 = 3
    coin3 = 4
    coin_list = []
    for i in range(0,m):
        currVal = i + 1
        if currVal - coin1 == 0:
            coin_list.append(coin1)
        elif currVal - coin2 < 0:
            coin_list.append(coin_list[currVal - 1 - coin1] +1)
        elif currVal - coin2 == 0:
            coin_list.append(1)
            # minimum of value at index (currval - coin1) + 1
        elif currVal - coin3 == 0:
            coin_list.append(1)
        elif currVal - coin3 < 0:
            coin_list.append(min(coin_list[currVal - 1 - coin1] +1,coin_list[currVal - 1 - coin2] +1))
            # minimum of (value at index (currval - coin1) + 1,value at index (currval - coin2) + 1)
        else:
            coin_list.append(min(coin_list[currVal - 1 - coin1] +1,coin_list[currVal - 1 - coin2] +1,coin_list[currVal - 1 - coin3] +1))
    return coin_list[m-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
