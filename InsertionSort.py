#imports
from random import randint
import time

#function definition
def InsertionSort(lst):
    for i in range(1,len(lst)):                   #for i in range 1 to len(lst) (every index exept the 0th)
        j=i                                       
        while lst[j-1]>lst[j] and j>0:            #while the element before the jth element is larger than j itself
            lst[j-1],lst[j] = lst[j],lst[j-1]     #swap the elements
            j-=1
    
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
insertionsort(List)                                       #sorts list
print(str(List))                                          #prints sorted list (optional)
print(f"Execution time: {time.time()-start_time}s")       #prints execution time (optional)
