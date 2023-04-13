input=['{','}','[',']','(',')']


s = "[]()"
#print(s[1])

if len(s) <= 1:
    print('false')


for i in range(0, len(s), 2):
    index = (input.index(s[i]))+1
    print(index)
    if input[index]==s[i+1]:
        print('true')
    else:
        print('false')
