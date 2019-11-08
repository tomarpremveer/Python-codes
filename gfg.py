import time


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


if __name__ == "__main__":
    grid=[[0,1,-1],[1,0,-1],[1,1,1]]
    print(cherryPickup(grid))