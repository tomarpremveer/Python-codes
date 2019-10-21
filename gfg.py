import time
def p(a,n):
    if n==1:
        return 2
    t=n//2
    if n%2==0:
        return p(a,t)*p(a,t)
    else:
        return p(a,t)*p(a,t+1)
def dp(n):
    d=[0]*(n+1)
    d[0]=1
    for i in range(1,n+1):
        d[i]=d[i-1]*2
    return d[n]

def removeduplicates(arr):
    j=0
    for i in range(0,len(arr)-1):
        if arr[i]!= arr[i+1]:
            arr[j]=arr[i]
            j+=1
    arr[j]=arr[len(arr)-1]
    print(arr)

def plusone(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        if digits[i] % 10 == 0 and digits[i]!=0:
            digits[i] = 0
            carry = 1
        else:
            carry = 0
    if carry:
        digits.insert(0, carry)
    return digits

if __name__=="__main__":
    arr=[1,0,0,0,0]
    print(plusone(arr))

