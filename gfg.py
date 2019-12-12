import time
import math


def p(a, n):
    if n == 1:
        return 2
    t = n // 2
    if n % 2 == 0:
        return p(a, t) * p(a, t)
    else:
        return p(a, t) * p(a, t + 1)


def dp(n):
    d = [0] * (n + 1)
    d[0] = 1
    for i in range(1, n + 1):
        d[i] = d[i - 1] * 2
    return d[n]


def removeduplicates(arr):
    j = 0
    for i in range(0, len(arr) - 1):
        if arr[i] != arr[i + 1]:
            arr[j] = arr[i]
            j += 1
    arr[j] = arr[len(arr) - 1]
    print(arr)


def plusone(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        if digits[i] % 10 == 0 and digits[i] != 0:
            digits[i] = 0
            carry = 1
        else:
            carry = 0
    if carry:
        digits.insert(0, carry)
    return digits


def cherryPickup(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    r = len(grid)
    c = [0]
    return getch(0, 0, r, grid, c)


def getch(n, m, r, grid, c):
    if n >= r or m >= r:
        return 0
    if grid[n][m] == -1:
        return 0
    if grid[n][m] == 1:
        return 1
    return getch(n + 1, m, r, grid, c) + getch(n, m + 1, r, grid, c)


def pivot(l, h, arr):
    if h == l:
        return l
    if l < h:
        mid = l + (h - l) // 2
        if mid < h and arr[mid] > arr[mid + 1]:
            return mid
        if mid > l and arr[mid] < arr[mid - 1]:
            return mid - 1
        if arr[l] >= arr[mid]:
            return pivot(l, mid - 1, arr)
        else:
            return pivot(mid + 1, h, arr)
    return -1


def sqrt(n):
    start = 1
    end = n
    while start <= end:

        mid = (start + end) // 2

        if mid * mid == n:
            return mid
        if mid * mid < n:
            start = mid + 1
            ans = mid
        else:

            end = mid - 1
    return ans


def maximumsumsubarray(arr):
    maxs, maxsofar = arr[0], arr[0]

    for i in range(1, len(arr)):
        maxsofar = max(maxsofar + arr[i], arr[i])
        maxs = max(maxsofar, maxs)
    return maxs


def findPosition(l, h, arr, t):
    if l <= h:
        mid = (l + h) // 2

        if (mid != 0 and mid != h) and (arr[mid - 1] < t and arr[mid + 1] > t):
            return mid
        if mid == 0 and arr[mid + 1] > t:
            return mid
        if mid == h and arr[mid - 1] < t:
            return mid + 1
        if arr[mid] < t:
            return findPosition(mid + 1, h, arr, t)
        else:
            return findPosition(l, mid - 1, arr, t)

def dup(arr):
    i=1
    j=2
    while j < len(arr):
        if arr[j] == arr[i]  and arr[j]==arr[i-1]:
            j+=1
        else:
            i+=1
            arr[i]=arr[j]
            j+=1
    return i+1



if __name__ == "__main__":
    arr=[ 0, 0, 1, 1, 2, 2, 3, 3]

    #print(findPosition(0,len(arr)-1,arr,902))
    print(arr[:dup(arr)])