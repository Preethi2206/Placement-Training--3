arr = list(map(int, input().split()))
n = len(arr)

for i in range(1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])
    print(subset)
