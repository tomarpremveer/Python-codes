from heapq import heapify,heappop,heappush

class minHeap:
    def __init__(self):
        self.heap=[]
    def parent(self,i):
        return (i-1)//2