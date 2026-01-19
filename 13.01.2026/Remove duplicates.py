lst = list(map(int, input().split()))
res = []

for x in lst:
    if x not in res:
        res.append(x)

print(res)
