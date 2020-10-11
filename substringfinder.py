s = input()
t = input()

k = 0
for i in range(len(s)):
    if len(t) <= len(s) and i + len(t) <= len(s):
        if s[i : i + len(t)] == t:
            k += 1

print(k)