from collections import Counter
import heapq

class Node:
    def __init__(self,freq,char):
        self.freq=freq
        self.char=char
    def __cmp__(self, other):
        return self.freq < other.freq
heapq._
class Heap:
    def __init__(self,arr):
        self.dic=Counter(arr)
        self.heap=[Node(i,v) for (i,v) in self.dic.items()]
        heapq._heapify_max(self.heap)
    def maxdist(self,k):
        while k > 0:
            v=heapq._heappop_max(self.heap)
            v-=1
            if v != 0:
                heapq.heappush(self.heap,v)
                heapq._heapify_max(self.heap)
            k-=1
        return len(self.heap)




if __name__ == "__main__":
    heap=Heap([1,2,2,2])
    k=1
    print(heap.maxdist(k))