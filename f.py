def median(arr):
    l=len(arr)
    arr=sorted(arr)
    if l%2==0:
        return (arr[l//2]+arr[(l-1)//2])/2.0
    else:
        return arr[l//2]
def activityNotifications(expenditure, d):
    s=[]
    noti=0
    for i in range(d,len(expenditure)):
        s = expenditure[i-d:i]
        m=median(s)
        if 2*m<=expenditure[i]:
            noti+=1
    return noti

def maxsum(arr,n,i,s,maxs):

    if s>=maxs:
        maxs=s
    if i==n:
        return maxs
    else:
       return maxsum(arr,n,i+1,s+arr[i],maxs)
       return maxsum(arr,n,i+1,s,maxs)


if __name__=="__main__":
    arr=[7,5,-2,3,1]
    d=3
    maxs=0
    s=0
    print(maxsum(arr,len(arr),0,s,maxs))
    print(arr)