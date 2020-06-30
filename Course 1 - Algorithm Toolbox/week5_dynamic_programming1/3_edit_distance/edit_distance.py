# Uses python3
def edit_distance(s, t):
    len_s = len(s)
    len_t = len(t)
    rows, columns = len_s + 1, len_t + 1
    arr = [[0 for x in range(rows)] for y in range(columns)] 
    for i in range(0,columns):
        arr[i][0] = i
    for i in range(0,rows):
        arr[0][i] = i
    for i in range(1,columns):
        for j in range(1,rows):
            if t[i-1] == s[j-1]:
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = min (arr[i-1][j-1],arr[i-1][j],arr[i][j-1]) + 1
    return arr[len_t][len_s]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
