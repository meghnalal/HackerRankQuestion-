'''
1436. Destination City
'''

'''
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from 
cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly 
one destination city.
'''
from collections import defaultdict

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

dictout= set()
dictin= set()
for o, i in paths:
    dictout.add(o)
    dictin.add(i)
for i in dictin:
    if i not in dictout:
        print(i)

