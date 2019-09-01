def soe(n, isPrime):
    isPrime[0] = isPrime[1] = False
    for i in range(2, n + 1):
        isPrime[i] = True

    p = 2
    while (p * p <= n):
        if isPrime[p] == True:
            i = p * p
            while (i <= n):
                isPrime[i] = False
                i += p
        p = p + 1
def countPair(a):
    count=0
    if len(a)==1:
        return 0
    b = [0]*(2*len(a))
    b=[2*a[i] for i in range(0,len(a))]
    for i in range(0,len(a)-1):
        if b[i]> a[i+1]:
            count+=1
    return count




def primesum(A):
    isPrime = [0] * (A + 1)
    soe(A, isPrime)
    for i in range(0, A):
        if isPrime[i] and isPrime[A - i]:
            return [i, A - i]
def mergerArr(a ,b):
    i,j=0,0
    n,m=len(a),len(b)
    while i<n and j<m:
        if a[i] < b[j]:
            i+=1
        else:
            a[i],b[j]=b[j],a[i]
            h=j
            swap=False
            while h < m-1 :
                if b[h] > b[h+1]:
                    b[h], b[h+1] = b[h+1], b[h]
                    swap = True
                else:
                    swap=False
                if(swap == False):
                    break
                h += 1
            i += 1


def subsum(arr):
    count=0
    prefixsum = [0]*len(arr)
    prefixsum[0] = arr[0]
    for i in range(1,len(arr)):
        prefixsum[i]=prefixsum[i-1]+arr[i]
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            sub_sum=prefixsum[j]-prefixsum[i]+arr[i]
            if sub_sum > 2 and sub_sum < 6:
                count+=1
    return count






if __name__=="__main__":
    a=[1,3,6,6,7,12]
    b=[2,4,5,8,9,13,14,15,16]
##    mergerArr(a,b)
    arr=[2,1,5,1,3]
    #print(a)
    #print(b)
    #print(countPair(arr))
    print(subsum(arr))
