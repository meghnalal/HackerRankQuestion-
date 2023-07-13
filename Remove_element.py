'''naive solution'''
'''Remember doing reverse safer to iterate in reverse order 
   to avoid skipping elements or encountering index errors.'''
nums = [0,1,2,2,3,0,4,2]
val=2

for i in range(len(nums)-1,-1,-1):
    if nums[i] == val :
        del nums[i]

nums.sort()

k=len(nums)

nums = [0,1,2,2,3,0,4,2]
val=2
''' it needs the k never needed the sorting so this solution is on '''
k = 0  # Variable to track the count of elements not equal to val

for i in range(len(nums)):
    if nums[i] != val:
            nums[k] = nums[i]
            k += 1

print (k)


'''parralel'''

import threading
import time

# Function 1
def function1():
    print("Function 1 started")
    start_time = time.time()
    # Add your code for function 1 here
    time.sleep(3)  # Simulating some work
    end_time = time.time()
    print("Function 1 completed in", start_time, "seconds")

# Function 2
def function2():
    print("Function 2 started")
    start_time = time.time()
    # Add your code for function 2 here
    time.sleep(2)  # Simulating some work
    end_time = time.time()
    print("Function 2 completed in",start_time, "seconds")

# Create threads for each function
thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

# Execution continues once both threads have completed
print("Both functions have completed")

''' process the array of element'''

import threading
import time

# Function to process an element
def process_element(element):
    print("Processing element", element)
    start_time = time.time()
    # Add your code to process the element here
    result = element + 10
    time.sleep(3)  # Simulating some work
    end_time = time.time()

    print("Element", element, "processed in",  start_time, "seconds",result)

# List of elements
elements = [1, 2, 3, 4, 5]

# Create threads for each element processing
threads = []
for element in elements:
    thread = threading.Thread(target=process_element, args=(element,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Execution continues once all threads have completed
print("All elements processed")


'''creating panda series '''

import pandas as pd

''' without pandas'''
population = {
    'USA' : 3333,
    "CHINA" : 222,
    "ITALY" : 234
}

usa_population = population['USA']
total_population = sum(population.values())

''' with pandas great forr vectorize operation '''
population_series =pd.Series(population)
total_population_pd = population_series.sum()

'''with filterng '''
large_population = population_series[population_series > 222]

'''STRING '''
string = ['aaple','banana','orange']
seriesstring =pd.Series(string)

'''type of series'''
series_dtype =seriesstring.dtype
print(series_dtype)

series_dtype =pd.Series(string , dtype=str)


series= pd.Series(pd.array(string))