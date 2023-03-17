s = [1, 2, 1, 3, 2]
d = 3
m = 2

count = 0

for i in range(len(s)-m+1):
    print((len(s)-m+1))
    seg_sum = sum(s[i:i+m])
    print(seg_sum)
    if seg_sum == d:
        count += 1
print(count)

def birthday(s, d, m):
    count = 0

    for i in range(len(s)-m+1):
        seg_sum = sum(s[i:i+m])
        if seg_sum == d:
            count += 1

    return count