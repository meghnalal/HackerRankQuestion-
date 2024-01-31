from collections import Counter
stones = "aAAbbbb"
jewels = "aA"
count = Counter(stones)
result = 0

for i ,c in count.items():
    if i in jewels:
        result += c
print(result)


