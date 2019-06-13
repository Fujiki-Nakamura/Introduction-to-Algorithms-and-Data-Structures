def max_heapify(heap, i):
    left_i, right_i = 2 * i, 2 * i + 1
    largest_i = i
    if left_i <= H and heap[left_i] > heap[i]:
        largest_i = left_i
    else:
        largest_i = i
    if right_i <= H and heap[right_i] > heap[largest_i]:
        largest_i = right_i

    if largest_i != i:
        heap[i], heap[largest_i] = heap[largest_i], heap[i]
        heap = max_heapify(heap, largest_i)
    return heap


H = int(input())
inputs = list(map(int, input().split()))
heap = [-1] * (H + 1)

for i in range(H):
    heap[i + 1] = inputs[i]

for i in reversed(range(1, H // 2 + 1)):
    heap = max_heapify(heap, i)

print(' ' + ' '.join([str(e) for e in heap[1:]]))
