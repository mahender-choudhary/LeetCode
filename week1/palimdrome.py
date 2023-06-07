x = 1211
y = str(x)
for i in range(0, len(y)//2):
    if y[i] != y[- i - 1]:
        print(False)

return True