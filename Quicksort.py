#imports
from random import randint
import time

#function definition
def quicksort(lst,L,R):
    if L<R:        
        partition_pos = partition(lst,L,R)    #changes pivot possition (where the list is partitioned)
        quicksort(lst,L,partition_pos-1)      #calls quicksort for the sublist left of the pivot
        quicksort(lst,partition_pos+1,R)      #calls quicksort for the sublist right of the pivot

def partition(lst,L,R):
    i=L                                       #defines i scanner
    j=R-1                                     #defines j scanner
    pivot = lst[R]                            #defines pivot point

    while i<j:                                #while the i scanner is before the j scanner    
        while i<R and lst[i]<pivot:           #while i is to the left and is not at the pivot point
            i+=1                              #move the scanner to the right
        while j>L and lst[j]>=pivot:          #while the j scanner is to the right and is not at the pivot point
            j-=1                              #move the scanner to the left
        if i<j:                               #if i and j have not crossed
            lst[i],lst[j] = lst[j],lst[i]     #switch the i element with the j element
    
    if lst[i]>pivot:                          #if the i scanners element is larger than the pivot (the sorting has finished)
        lst[i],lst[R] = lst[R],lst[i]         #then i is swapped with the pivot

    return i                                  #i is returned as the new pivot point               

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
