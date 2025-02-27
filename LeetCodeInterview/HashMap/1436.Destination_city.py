''''''


'''You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct 
path going from cityAi to cityBi. Return the destination city, 
that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, 
therefore, there will be exactly one destination city.

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city.
 Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
'''
paths = [["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]
''' not in order '''

setzero= set()
for i in paths:
    if i[0] not in setzero:
        setzero.add(i[0])

for z in paths:
    if z[1] not in setzero:
        ans=z[1]
print(ans)

''' technically better solution but took longer ? so not sure '''

startDestination = set()
endDestination = set ()
for s, e in paths:
    startDestination.add(s)
    endDestination.add(e)

for enddest in endDestination:
    if enddest not in startDestination:
        ans=enddest
print(ans)
