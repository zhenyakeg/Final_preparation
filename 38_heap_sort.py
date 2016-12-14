class Heap:
    def __init__(self):
        self.body = []
    def heap_push(self, x):
        self.body.append(x)
        i = len(self.body) - 1
        while i != 0:
            ip = (i-1) // 2
            if self.body[i] <= self.body[ip]:
                break
            else:
                self.body[i], self.body[ip] = self.body[ip], self.body[i]
                i = ip
    def heap_pop(self):
        assert  len(self.body) > 0
        result = self.body[0]
        i = 0
        while i * 2 + 1 < len(self.body): #есть левый
            if i*2+2 >= len(self.body): #нет правого
                self.body[i] = self.body[i*2+1]
                return  result
            if self.body[i*2+1] > self.body[i*2+2]:
                self.body[i*2 + 1], self.body[i] = self.body[i], self.body[2*i +1]
                i = i*2 + 1
            else:
                self.body[i*2+2], self.body[i] = self.body[i], self.body[i*2+1]
                i = i*2 + 2
        self.body[i] = self.body.pop()
        while i !=0:
            ip = (i - 1) // 2
            if self.body[i] <= self.body[ip]:
                break
            else:
                self.body[i], self.body[ip] = self.body[ip], self.body[i]
                i = ip
        return result
def heap_sort(A):
    H = Heap()
    for x in A:
        H.heap_push(x)
    for i in range(len(A)-1):
        A[i] = H.heap_pop()
print(heap_sort([i for i in range(1,100)]))