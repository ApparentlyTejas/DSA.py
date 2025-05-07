# time = O(N + K) K= range of data
# space = O(K)

F = [5, 3, 2, 1, 3, 3, 7, 2, 2]
def counting_sort(arr):
    n = len(arr)
    maxx = max(arr)
    counts = [0] * (maxx + 1)

    for x in arr:
        counts[x] += 1
    i = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1
counting_sort(F)
print(F)

# Time complexity is O(n log n) from using Tim Sort
G = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
G.sort()
print(G)

sorted_G = sorted(G)
print(G , sorted_G)

# sorting array of Tupples 
H = [(-5, 3), (2, 1), (-3, -3), (7, 2), (2, 2)]
sorted_H = sorted(H , key = lambda t: t[1])
print(sorted_H)