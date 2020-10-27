# python3
import math

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    len_data = len(data)
    # for i in range(math.ceil(len_data/2), -1, -1):
    #     item_index = i
    #     f_child_index, s_child_index = children(i)
    #     if f_child_index > len_data-1:
    #         continue
    #     if data[f_child_index] <= data[s_child_index]:
    #         swap_index = f_child_index
    #     else:
    #         swap_index = s_child_index
    #     if data[item_index] > data[swap_index]:
    #         data[item_index], data[swap_index] = data[swap_index], data[item_index]
    #         swaps.append((item_index, swap_index))

    for i in range(math.ceil(len_data/2), -1, -1):
        while data[i] > data[children(i)[0]] or data[i] > data[children(i)[1]]:
            f_child_index, s_child_index = children(i)
            if f_child_index > len_data-1:
                continue
            if data[f_child_index] <= data[s_child_index]:
                swap_index = f_child_index
            else:
                swap_index = s_child_index
            if data[i] > data[swap_index]:
                data[i], data[swap_index] = data[swap_index], data[i]
                swaps.append((i, swap_index))

    # for i in range(math.ceil(len_data/2), -1, -1):
    #     item_index = i
    #     f_child_index, s_child_index = children(i)
    #     if f_child_index > len_data-1:
    #         continue
    #     elif s_child_index > len_data-1:
    #         swap_index = f_child_index
    #     else:
    #         if data[f_child_index] <= data[s_child_index]:
    #             swap_index = f_child_index
    #         else:
    #             swap_index = s_child_index
    #     while data[item_index] > data[children(i)[0]] or data[i] > data[children(i)[1]]:
    #         #item_index = i
    #         while data[item_index] > data[swap_index]:
    #             data[item_index], data[swap_index] = data[swap_index], data[item_index]
    #             swaps.append((item_index, swap_index))
    #             item_index = parent (item_index)
    #             f_child_index, s_child_index = children(item_index)
    #             if f_child_index > len_data-1:
    #                 continue
    #             elif s_child_index > len_data-1:
    #                 swap_index = f_child_index
    #             else:
    #                 if data[f_child_index] <= data[s_child_index]:
    #                     swap_index = f_child_index
    #                 else:
    #                     swap_index = s_child_index

    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # len_data = len(data)
    # for i in range(len_data):
    #     f_child_index, s_child_index = children(i)
    #     if f_child_index > len_data-1:
    #         break
    #     elif s_child_index > len_data-1:
    #         swap_index = f_child_index
    #     else:
    #         if data[f_child_index] >= data[s_child_index]:
    #             swap_index = f_child_index
    #         else:
    #             swap_index = s_child_index
        
    #     if data[i] > data[swap_index]:
    #         swaps.append((i, swap_index))
    #         data[i], data[swap_index] = data[swap_index], data[i]
    #     else:
    #         continue
        # try:
        #     max_val = max(data[f_child_index],data[s_child_index])
        #     if max 
        # except IndexError:
        #     pass
        # try: 
        #     if data[i] > data[f_child_index]:
        #         swap_index = f_child_index
        #         swaps.append((i, swap_index))
        #         data[i], data[swap_index] = data[swap_index], data[i]
        #     elif data[i] > data[s_child_index]:
        #         swap_index = s_child_index
        #         swaps.append((i, swap_index))
        #         data[i], data[swap_index] = data[swap_index], data[i]
        # except IndexError:
        #     try:
        #         if data[i] > data[s_child_index]:
        #             swap_index = s_child_index
        #             swaps.append((i, swap_index))
        #             data[i], data[swap_index] = data[swap_index], data[i]
        #     except IndexError:
        #         continue
    return swaps


def swap(data,item_index):
        while data[item_index] < data[parent(item_index)]:
            data[item_index], data[parent(item_index)] = data[parent(item_index)], data[item_index]
            item_index = parent(item_index)
        return item_index

def parent (i):
    if i % 2 == 0:
        return int(i/2)
    else:
        return math.floor(i/2)

def children (i):
    return (2*i +1, 2*i +2)

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
