# bubble sort 
# time : O(n^2)
# space : O(1)
A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
def bubblesort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i] , arr[i-1]
bubblesort(A)
print(A)