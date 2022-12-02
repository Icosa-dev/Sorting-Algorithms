#imports
from random import randint
import time

#function definition
def mergesort(lst):
    if len(lst)>1:                                  #if the list is not just 1 element
        leftLst = lst[:len(lst)//2]                 #split it in half into a left side
        rightLst = lst[len(lst)//2:]                #and a right side
        
        MergeSort(leftLst)                          #then mergesort the two sides
        MergeSort(rightLst)

        i = 0                                       #left list index
        j = 0                                       #right list index
        k = 0                                       #primary list index

        while i<len(leftLst) and j<len(rightLst):   #while i and j arnt at the ends of their lists
            if leftLst[i]<rightLst[j]:              #if i's element is smaller than j's
                lst[k] = leftLst[i]                 #override k's element with i's
                i+=1                                #increment i
            else:                                   #otherwise if i's element is larger than j's
                lst[k] = rightLst[j]                #override k's element with j
                j+=1                                #increment j
            k+=1                                    #increment k
        
        while i<len(leftLst):                       #while i is not at the end of its list
            lst[k] = leftLst[i]                     #override k's element with i's
            i+=1                                    #increment i
            k+=1                                    #and k
        while j<len(rightLst):                      #while j is not at the end of its list
            lst[k] = rightLst[j]                    #override k's element with j's
            j+=1                                    #increment j
            k+=1                                    #and k 
            
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
mergesort(List)                                           #sorts list
print(str(List))                                          #prints sorted list (optional)
print(f"Execution time: {time.time()-start_time}s")       #prints execution time (optional)
