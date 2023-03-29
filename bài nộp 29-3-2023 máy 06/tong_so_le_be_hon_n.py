n = int(input())
s = 0
i = 0
while (i < n):
    if n % 2 == 1:
        s += i
    i += 1
print(s)
