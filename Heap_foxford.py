import heapq,random
def add(Heap, x):
    Heap.append(x)
    i = len(Heap) - 1
    while i != 0:
        ip = (i-1) // 2
        if Heap[i] <= Heap[ip]:
            break
        else:
            Heap[i], Heap[ip] = Heap[ip], Heap[i]
            i = ip

def pop(Heap):
    if len(Heap) == 1:
        return Heap.pop()
    retval = Heap[0]
    Heap[0] = Heap.pop()
    i = 0
    while 2 * i + 2 < len(Heap) \
          and Heap[i] < max(Heap[2 * i+1], Heap[2 * i + 2]):
        if Heap[2 * i+1] > Heap[2 * i + 2]:
            Heap[i], Heap[2 * i+1] = Heap[2 * i+1], Heap[i]
            i = 2 * i+1
        else:
            Heap[i], Heap[2 * i + 2] = Heap[2 * i + 2], Heap[i]
            i = 2 * i + 2
    if 2 * i +1 == len(Heap) - 1 and Heap[i] < Heap[2 * i]:
        Heap[i], Heap[2 * i+1] = Heap[2 * i+1], Heap[i]
    return retval
