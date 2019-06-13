def max_heapify(heap, i):
    heap_size = len(heap) - 1
    left_i, right_i = 2 * i, 2 * i + 1
    largest_i = i
    if left_i <= heap_size and heap[left_i] > heap[i]:
        largest_i = left_i
    else:
        largest_i = i
    if right_i <= heap_size and heap[right_i] > heap[largest_i]:
        largest_i = right_i

    if largest_i != i:
        heap[i], heap[largest_i] = heap[largest_i], heap[i]
        heap = max_heapify(heap, largest_i)
    return heap


def insert(heap, k):
    heap.append(k)
    heap_size = len(heap) - 1
    for i in range(heap_size, 0, -1):
        heap = max_heapify(heap, i)
    return heap


def extract(heap):
    root = heap[1]
    heap[1] = heap.pop()

    heap_size = len(heap) - 1
    for i in range(heap_size, 0, -1):
        heap = max_heapify(heap, i)

    return root, heap


if __name__ == '__main__':
    n_operations = 2000000
    dummy = -1
    heap = [dummy]

    results = []
    for _ in range(n_operations):
        operation = input()
        if operation.startswith('end'):
            break
        if operation.startswith('insert'):
            operation, k = operation.split()
            k = int(k)
            heap = insert(heap, k)
        elif operation.startswith('extract'):
            root, heap = extract(heap)
            results.append(root)

    for result in results:
        print(result)
