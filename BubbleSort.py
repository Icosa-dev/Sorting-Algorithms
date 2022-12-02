#imports
from random import randint
import time

#function definition
def bubblesort(lst):
    n = len(lst)
    swapped = False                           
    for i in range(n-1):                          #for every element
        for j in range(0, n-i-1):                 #for j in range 0 to n-i-1
            if lst[j] > lst[j + 1]:               #if the element j is larger than the element after it
                swapped = True                    
                lst[j], lst[j + 1] = lst[j + 1], lst[j]             #swap element j with j+1
         
        if not swapped:                                             #if swapped is False
            return                                                  #stop sorting
    
#assigning values to the variables	
List = []                                         #variables for adding random elements to the list (optional, set all to 0 to not add random elements
rangeMin = 0
rangeMax = 0
elementMin = 0
elementMax = 0

for i in range(rangeMin,rangeMax):
	List.append(randint(elementMin,elementMax)

#output				
start_time = time.time()                                  #starting time (optional)
bubblesort(List)                                          #sorts list
print(str(List))                                          #prints sorted list (optional)
print(f"Execution time: {time.time()-start_time}s")       #prints execution time (optional)
