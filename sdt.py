def maxksum(arr, k):
	mx = float('-inf')
	for i in range(len(arr) - k + 1):
		mx = max(mx, sum(arr[i:i + k]))
	return mx


if __name__ == "__main__":
	arr = [100, 200, 300, 400]
	k = 2
	print(maxksum(arr, k))
