s = input()
stack = []
pair = {')':'(', '}':'{', ']':'['}
flag = True

for ch in s:
    if ch in "({[":
        stack.append(ch)
    elif ch in ")}]":
        if not stack or stack.pop() != pair[ch]:
            flag = False
            break

print("Balanced" if flag and not stack else "Not Balanced")
