def sup(s,i,n):
    if n==0:
        if s//10>0:
            sup(0,i,s)
        else:
            return sup(eval())

    else:
        return sup(s+n%10,n//10)
def stringprint(s,l,r):
    if l<=r:
        printfunction(l,r)
    if l>r:
        return
    else:
        stringprint(s,l+1,r)
        stringprint(s,l,r-1)
        stringprint(s,l+1,r-1)
def printfunction(l,r):
    print(l,r)

def mw(i,j,n,m,mat):
    if i > n or j > m:
        return 0
    if mat[i][j]==0:
        return 0
    if i==n and j==m:
        return 1
    else:
        return mw(i+mat[i][j],j,n,m,mat)+mw(i,j+mat[i][j],n,m,mat)
def stepsCount(n):
    count=0
    a=0
    while  a<=n:
        a+=1
        count+=1
        if a>=n:
            break
        a*=2
        count+=1
        if a>n:
            break
    return count
def stepsCountR(a,n):
    if a==n:
        return 1
    if a>n:
        return 0
    else:
        return stepsCountR(a+1,n)+stepsCountR(a*2,n)
def newNumber(no):
    div=1
    n=no
    while n>10:
        div*=10
        n=n//10
    nn=0
    while no>=0 and div>=1:
        r=no//div
        nn=nn*10+(9-r)
        no %=div
        div //= 10

    return nn
def getOccurence(n,d):
    result=0
    itr=d
    while itr <=n :
        if itr%10==d:
            result+=1
        if itr!=0 and itr//10==d:
            result+=1
            itr+=1
        elif itr//10==d-1:
            itr=itr+(10-d)
        else:
            itr+=10
    return result

def m(a):
    if a==0 or a<0 :
        print(a)
    else:
        print(a)
        m(a-5)
        print(a)

def search(a):
    pass

if __name__=="__main__":

    s="abcde"
   # matrix=[[1,0,2],[1,1,1],[2,0,1]]
    #print(mw(0,0,2,2,matrix))
    #stringprint(s,0,5)
    #print(stepsCountR(1,3))
    #print(newNumber(210))
   #3 print(getOccurence(123,2))
    print(m(16))