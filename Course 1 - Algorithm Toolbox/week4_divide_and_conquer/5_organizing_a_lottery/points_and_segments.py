# Uses python3
import sys
import math

def merge4(L,R):
    arr = []
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i].start < R[j].start:
            arr.append(L[i])
            i+= 1
        else:
            arr.append(R[j])
            j+= 1
        k+= 1

    # Checking if any element was left
    while i < len(L):
        arr.append(L[i])
        i+= 1
        k+= 1

    while j < len(R):
        arr.append(R[j])
        j+= 1
        k+= 1
    return arr

def merge_sort4(arr):
    len_arr = len(arr)
    if len_arr == 1:
        return arr
    arr_len_div_2 = math.ceil(len_arr/2)
    x= merge_sort4(arr[0:arr_len_div_2])
    y= merge_sort4(arr[arr_len_div_2:len_arr])
    return merge4(x,y)


class segment(object):
    def __init__(self,start,end):
        self.start = start
        self.end = end

def findStart(segments,point,index,segLen):
    if index == 0:
        return 0
    elif index == segLen - 1 and segments[index].start <= point:
        return index
    elif segments[index].start <= point and segments[index + 1].start > point:
        return index
    elif segments[index].start < point:
         return findStart(segments,point,math.floor((index+segLen)/2),segLen)
    elif segments[index].start > point:
         return findStart(segments,point,math.floor((index)/2),segLen)

    # if expression:
    #     pass
    # if ((len(segments) == 1) or (index == 0 and segments[index].start < point)):
    #      return index
    # elif (index == segLen -1 and segments[index].start < point):
    #      return index
    # elif segments[index].start <= point and segments[index + 1].start > point:
    #     return index
    # elif segments[index].start < point:
    #      return findStart(segments,point,math.floor((index+segLen)/2),segLen)
    # elif segments[index].start > point:
    #      return findStart(segments,point,math.floor((index)/2),segLen)
    # else:
    #     return -1




def fast_count_segments(starts, ends, points):
    lenStarts = len(starts)
    cnt = [0] * len(points)
    segments = []
    for i in range(0,lenStarts):
        myseg = segment(starts[i],ends[i])
        segments.append(myseg)
    segments = merge_sort4(segments)
    #write your code here
    lenPoints = len(points)
    segLen = len(segments)
    seg_len_div_2 = math.floor(segLen/2)
    for i in range(0,lenPoints):
        foundindex = findStart(segments,points[i],seg_len_div_2,segLen)
        if foundindex == -1:
            continue
        while foundindex != -1 and segments[foundindex].start <= points[i] and segments[foundindex].end >= points[i]:
            cnt[i] += 1
            foundindex -= 1
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


# input = sys.stdin.read()
# data = list(map(int, input.split()))
# n = data[0]
# m = data[1]
# starts = data[2:2 * n + 2:2]
# ends   = data[3:2 * n + 2:2]
# points = data[2 * n + 2:]
# #use fast_count_segments
# cnt = fast_count_segments(starts, ends, points)
# for x in cnt:
#     print(x, end=' ')

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
