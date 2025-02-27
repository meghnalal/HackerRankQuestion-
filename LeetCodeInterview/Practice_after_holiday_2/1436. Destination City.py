'''
1436. Destination City
'''

'''
You are given the array paths, where paths[i] = [cityAi, cityBi] 
means there exists a direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, 
there will be exactly one destination city.
'''

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
start= set()
end= set()
for s,e in paths:
    start.add(s)
    end.add(e)

for ends in end:
    if ends not in start:
        print(ends)
#  the solution editorial created only one set with the outgoing
has_outgoing = set()
for i in range(len(paths)):
    has_outgoing.add(paths[i][0])

for i in range(len(paths)):
    candidate = paths[i][1]
    if candidate not in has_outgoing:
        print(candidate)

print ("")