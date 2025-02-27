'''
1732. Find the Highest Altitude
'''
'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between 
points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
'''

gain = [44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]
prefix=[0]

max_altitude=0

for i in range(0,len(gain)):
    prefix.append(gain[i]+prefix[-1])
    if prefix[-1] >max_altitude:
        max_altitude = prefix[-1]
print(max_altitude)