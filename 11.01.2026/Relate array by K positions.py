arr = list(map(int, input().split()))
k = int(input())
k = k % len(arr)

print(arr[-k:] + arr[:-k])
