list = []
s = "IVC"
values = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
for i in range(0, len(s)):
    for j in range(i + 1, len(s)):
        if i < j:
            list.append(j - i)
        else:
            list.append(i + j)

print(list)