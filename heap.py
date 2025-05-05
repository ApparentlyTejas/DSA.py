A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
import heapq
print('heapify')
heapq.heapify(A)
print(A)
print('heappush')
heapq.heappush(A,4)
print(A)
print('heappop')
minn = heapq.heappop(A)
print(A, minn)

print('heapsort')
def heapsort(arr):
    heapq.heapify(arr)
    n = len(A)
    new_list= [0] * n
    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i]= minn
    return new_list
print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

print('Max heap')
B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)
for i in range(n):
    B[i] = -B[i]
heapq.heapify(B)
print(B)

print('largest in max heap')
largest = -heapq.heappop(B)
print(largest)

print('make a new heap from scratch')
C = [-5, 4, 2, 1, 7, 0, 3]
heap = []
for x in C:
    heapq.heappush(heap, x)
    print(heap, len(heap))

print('putting tuples of items in heap')
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]
from collections import Counter
Counter = Counter(D)
print(Counter)

heap=[]
for k,v in Counter.items():
    heapq.heappush(heap, (k,v))
print(heap)

