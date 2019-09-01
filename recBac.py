import time
def fibonacci(n):
    fib=[0 for i in range(n)]
    fib[0],fib[1]=0,1
    if fib[n-1]!=0:
        return fib[n-1]
    else:
        for i in range(2,n):
            fib[i]=fib[i-1]+fib[i-2]
        return fib[n-1]



def exp(n):
    # stack memory used is O(n)
    if n < 0:
        return -1
    if n == 0:
        return 1
    else:
        return 2 * exp(n - 1)


def expoo(n, k, d):
    ##to find the pow(n,k)%d. optimized method
    if k < 0:
        return -1
    if k == 1:
        return n % d
    elif k % 2 == 0:
        t = k // 2
        return (expoo(n, t, d) % d * expoo(n, t, d) % d) % d
    else:
        t = k // 2
        return (expoo(n, t, d) % d * expoo(n, t + 1, d) % d) % d




def subset(arr):
    #to print all the subsets using bit manipulation
    for i in range(0, 1 << len(arr)):
        for j in range(len(arr)):
            if (i & 1 << j) > 0:
                print(arr[j], end=" ")
        print("\n")


def expo(k):
    #to find the pow(n,k)%d
    if k == 1:
        return n % d
    else:
        return ((n % d) * expo(k - 1)) % d


def ss(arr, n, i, s, m):
    #to generate all the subset of a set
    if i == n:
        print(s)
    else:
        ss(arr, n, i + 1, s, m)
        s[m] = arr[i]
        ss(arr, n, i + 1, s, m + 1)


def sumsubset(arr, n, i, s):
    #to find the sum of all the subsets of an array
    if i == n:
        print(s)
    else:
        sumsubset(arr, n, i + 1, s + arr[i])
        sumsubset(arr, n, i + 1, s)


def countsumsubset(arr, n, i, s, x):
    #count the number of subset having sum equal to x
    if i == n:
        if s == x:
            return 1
        else:
            return 0
    else:
        return countsumsubset(arr, n, i + 1, s + arr[i], x) + countsumsubset(arr, n, i + 1, s, x)


def stepPerms(n):
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    res[2] = 2
    for i in range(3, n + 1):
        res[i] = res[i - 1] + res[i - 2]+res[i-3]

    return res[n]
def countsumsubsetR(arr, n, i, s, x):
    #function to find the count of the subset having sum equal to x and if number can be repeated
    if i == n:
        if s == x:
            return 1
        else:
            return 0
    if s==x:
        return 1
    if s > x:
        return 0
    else:
        return countsumsubsetR(arr, n, i, s + arr[i], x) + countsumsubsetR(arr, n, i + 1, s, x)


def prints(s):
    for i in s:
        if i not in []:
            print(i, end=" ")
    print("\n")


def thrsum(arr, x):
    arr = sorted(arr)
    for i in range(0, len(arr) - 2):
        l = i + 1
        r = len(arr) - 1
        while l <= r:
            s = arr[l] + arr[r] + arr[i]
            if s == x:
                return 1
            elif s < x:
                l += 1
            else:
                r -= 1
        return -1

def per(a,l,r):
    if l==r:
        print(a)
    else:
        for i in range(l,r+1):
            swap(a,l,i)
            per(a,l+1,r)
            swap(a,l,i)

def swap(a,i,r):
    a[i],a[r]=a[r],a[i]


def countStep(k):
    if k==0 or k==1:
        return 1
    elif k==2:
        return 2
    else:
        return countStep(k-1)+countStep(k-2)+countStep(k-3)
def steps(n):
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    res[2]=2
    if n==0:
        return res[n]
    if n==1:
        return res[n]

    for i in range(3, n + 1):
        res[i] = steps(i-1) + steps(i-2) + steps(i - 3)
    return res[n-1]

    return res[n]

def countM(l,u,d,r):
    if d==l and r==u:
        return 1
    if d > l or r> u:
        return 0
    else:
       return countM(l,u,d+1,r)+countM(l,u,d,r+1)

    def btm(p,q):
        if p==0 and q==0:
            return 1
        if p<0 or q<0:
            return 0
        else:
            return btm(p-1,q)+btm(p,q-1)

if __name__ == "__main__":
    # print(exp(0))

    # print(expoo(2, 3, 3))
    # print(s1ubset([1,2,3]))
    arr = [1, 2]
    # s = [[]]*(1<<len(arr))
    x = 2
    s = 0
    c = 0
    l = len(arr)
    #a = [557, 217, 627, 358, 527, 358, 338, 272, 870, 362, 897, 23, 618, 113, 718, 697, 586, 42, 424, 130, 230, 566,
        # 560, 933]
    #print(countsumsubsetR(arr, l, 0, s, x))
    ##print(thrsum(a,986))
    ##ss(arr, len(arr), 0, s,0)
    ##print("the sum of all the subsets of the array is" )
    ##sumsubset(arr,3,0,0)
    s=["a","b","c"]
    #per(s,0,2)
    a=0
    #start=time.time()
    #print(countStep(35))
    #end=time.time()
    #print(end-start)
    #start=time.time()
    #print(steps(35))
    #end=time.time()
    print(stepPerms(4))

    #print(end-start)
    #print(countM(2,2,0,0))
    #print(btm(2,2))
    #print(fibonacci(5))