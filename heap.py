import heapq
from collections import Counter
def heapify(arr,n,idx):
    l=2*idx+1
    r=2*idx+2
    largest=idx
    if l<n and arr[l] >  arr[idx]:
        largest=l
    if r< n and arr[r] > arr[largest]:
        largest=r
    if largest != idx :
        arr[idx], arr[largest] = arr[largest], arr[idx]
        heapify(arr,n,largest)
def getmin(arr):
    return arr[0]
def heapsort(arr):
    l=len(arr)
    for i in range(l//2,-1,-1):
        heapify(arr,l,i)
    for i in range(l-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
def minimumcost(arr):
    total_cost=0
    while len(arr) !=1:
        f,s=0,0
        heapq.heapify(arr)
        f=heapq.heappop(arr)
        s=heapq.heappop(arr)
        total_cost+=f+s
        heapq.heappush(arr,f+s)
    return total_cost

def cookies(k, A):
    heapq.heapify(A)
    ts=0
    count=0
    while len(A)!=1 and A[0]<k:
        if A:
            f = heapq.heappop(A)
        if A:
            l=heapq.heappop(A)
        else:
            l=0
        s=1*f+2*l
        ts+=s
        count+=1

    if ts<k:
        return -1
    else:
        return count


def maxnumber(m,k):
    arr=[0,0,0,0,0]
    for i in range(m):
        a,b=input().split(' ')
        a,b=int(a),int(b)
        arr[a]+=100
        arr[b+1]-=100
        arr=prefix(arr)
    return max(arr)
def prefix(arr):
    presum=[0 for i in range(len(arr))]
    presum[0]=arr[0]
    for i in range(1,len(arr)):
        presum[i]=presum[i-1]+presum[i]
    return presum



def value

if __name__ == "__main__":
    pass
