def binarySearchL(l,r, n):
    if l <= r:
        m = l + (r - l) // 2
        prod = (m * (m + 1)) // 2
        if prod == n:
            return "YES"
        if prod > n:
            return binarySearchL(l,m-1,n)+binarySearchL(m+1,r,n)
        else:
            return binarySearchL(m+1,m,n)+binarySearchL(l, m - 1, n)
    return "NO"

def solve(A):
    mid = (0 + A) // 2
    return binarySearchL(0, mid, A, A)
if __name__=="__main__":
    A=256
    print(solve(A))
