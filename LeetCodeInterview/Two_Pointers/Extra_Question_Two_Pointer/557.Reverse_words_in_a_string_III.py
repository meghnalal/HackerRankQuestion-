''' 557. Reverse Words in a String III '''
'''
Given a string s, reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order.
Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''
s = "Mr Ding"
splitted_array=s.split()
ans= ""

''' convert in array  '''

def convertstringarray(s,left,right):
    arr=[]
    for c in s:
        arr.append(c)
    while left< right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return "".join(arr)


arr2=''
for c in splitted_array:
   arr = convertstringarray(c,0,len(c)-1)
   arr2 = arr2 + " " + arr
print(arr2.strip())


'''someone better solution '''
''' i[::-1] prints reverse of a string'''
s = "Mr Ding"
l = s.split()
s = ''
for i in l:
    s = s + ' ' + i[::-1]
print (s.strip())