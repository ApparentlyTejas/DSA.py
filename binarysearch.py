A = [1, 2, 3, 4, 5]
def binary_search(arr, Target):
    
    N = len(arr)
    L = 0
    R = N - 1
    while L <= R:
        M = L + ((R - L) // 2)
        if arr[M] == Target:
            return True
        elif Target < arr[M]:
            R = M -1 
        else:
            L = M + 1
    return False
print(binary_search(A, 10))
