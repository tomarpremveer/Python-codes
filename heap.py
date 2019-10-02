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
if __name__ == "__main__":
    arr=[3,9,6,1,0,5]
    heapsort(arr)
    print(arr)