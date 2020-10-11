s = input()
a = input()
b = input()

k = 0
for i in range(1001):
    if s.__contains__(a):
        s = s.replace(a, b)
        k += 1
if k >= 1000:
    print("Impossible")
else:
    print(k)
