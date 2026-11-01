class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = [0]
        for num in self.nums:
            self.push(num)        

    def add(self, val: int) -> int:
        self.push(val)
        while len(self.heap) - 1 > self.k:
            self.pop()
        return self.heap[1]

    def push(self, val):
        print(self.heap)
        self.heap.append(val)
        index = len(self.heap) - 1
        while index > 1 and self.heap[index] < self.heap[index // 2]:
            temp = self.heap[index]
            self.heap[index] = self.heap[index // 2]
            self.heap[index // 2] = temp
            index = index // 2
    
    def pop(self):
        pop_value = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap = self.heap[:-1]
        index = 1
        while index * 2 < len(self.heap):
            if index * 2 + 1 < len(self.heap) and self.heap[index * 2 + 1] < self.heap[index * 2]:
                temp = self.heap[index]
                self.heap[index] = self.heap[index * 2 + 1]
                self.heap[index * 2 + 1] = temp
                index = index * 2 + 1
            elif self.heap[index * 2] < self.heap[index]:
                temp = self.heap[index]
                self.heap[index] = self.heap[index * 2]
                self.heap[index * 2] = temp
                index = index * 2
            else:
                break
        return pop_value
        
