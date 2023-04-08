'''o(n2)'''
arr = [1, 2, 3, 4, 5]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        print(arr[i], arr[j])



'''this O(n)'''
arr= [1,3,4,5,7,8]

left = 0
right = 1

while left < len(arr) - 1:
    print(arr[left], arr[right])
    right += 1
    if right == len(arr):
        left += 1
        right = left + 1