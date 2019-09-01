def binarySearch(l, r, A, B, C, D, E):
    if l <= r:
        mid = l + (r - l) // 2
        d = mid * D + A
        e = (C - mid) * E + B
        if d == e:
            return C - mid
        if d < e:
            binarySearch(mid + 1, r, A, B, C, D, E)
        else:
            binarySearch(l, mid - 1, A, B, C, D, E)
    return -1


def solve(A, B, C, D, E):
    return binarySearch(0, C, A, B, C, D, E)
if __name__=="__main__":
    A=5923
    B=4426260
    C=1304761587
    D=412
    E=219
    print(solve(A,B,C,D,E))