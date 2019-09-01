def elementFrequency(arr,l,m,r,x):
    n1=m - l +1
    L=[0]*n1

    for i in L:
        if i==x:
            return 1
        else:
            return 0

def eleme(arr,l,r,x):
    if l <r:
        mid=(l+r)//2
        eleme(arr,l,mid,x)
        eleme(arr,mid+1,r,x)
        return elementFrequency(arr,l,mid,r,x)
if __name__=="__main__":
    arr=[1,2,2,2,3,4]
    n=len(arr)

    print(eleme(arr,0,n-1,2))
