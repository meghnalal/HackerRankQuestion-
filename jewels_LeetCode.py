jewels='aA'
stones='aAAbbb'
count=0
for i in stones:
    if i in jewels:
        count= count+1
print(count)

'''make this solution better'''
'''this solution takes more time technically not sure if its better '''
jewels='aA'
stones='aAAbbb'
jset = set(jewels)
count=0
for i in stones:
    if i in jset:
        count= count+1
print(count)