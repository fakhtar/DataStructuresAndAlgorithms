# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    j2 = l
    for i in range(l + 1, r+1):
        if a[i] < x:
            b = a[i]
            del(a[i])
            a.insert(j,b)
            # a[i:i+1], a[j:j2+1] = a[j:j2+1], a[i:i+1]
            j += 1
            j2 += 1
            continue           
        if a[i] == x:
            b = a[i]
            del(a[i])
            a.insert(j,b)
            j2 += 1
            continue
    #a[l], a[j] = a[j], a[l]
    return j, j2

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort2(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    #k = l
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort2(a, l, m1 - 1)
    randomized_quick_sort2(a, m2 + 1, r)

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort2(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

# for k in range(0,100):
#     for j in range(1,100):
#         my_list = []
#         for i in range(0,k):
#             a = 0
#             my_list.append(int(random.randint(1, 500)))
#         my_list2 = my_list.copy()
#         print('---------')
#         print(my_list)
#         print(my_list2)
#         randomized_quick_sort2(my_list2,0,len(my_list2) - 1)
#         randomized_quick_sort(my_list,0,len(my_list) - 1)
#         print(j)
#         print(my_list)
#         print(my_list2)
#         assert my_list == my_list2
    
# b = [4, 7, 4, 6]
# print(randomized_quick_sort2(b, 0, 3))
# print(b)
# c = [7,4,7,1,7] 
# d = [4,7,4,1,7]
# e = [1,1,4,4,7] 
# f = [7,4,4,1,1]
# g = [9, 11, 3, 10] 
# print(partition3(c,0,4))
# print(partition3(d,0,4))
# print(partition3(e,0,4))
# print(partition3(f,0,4))
# print(randomized_quick_sort2(g,0,3))
# print(g)
# print(partition3(g,0,3))
# h = [1, 3, 1]
# print(randomized_quick_sort2(h,0,2))
# print(h)
# i = [7, 4, 7, 1, 7] 
# print(partition3(i,0,4))
# j = [3,2,1] 
# print(randomized_quick_sort2(j,0,2))