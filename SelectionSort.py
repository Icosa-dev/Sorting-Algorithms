#imports
from random import randint
import time

#function definition
def selectionsort(lst):
	def smallestnum(lst):
		smallestNum = lst[0]             #assume the smallest number is the first 
		for num in lst:                  #for all element in the list
			if num<smallestNum:          #if there exists a number smaller than the current smallest number
				smallestNum = num        #set it as the new smallest number
		return smallestNum               #return the smallest number of the list
	
	sortedlst = []                       #assign an empty list for the sorted list
	for i in range(0,len(lst)):          #for i in range 0 to the length of the list
		sortedlst.append(smallestnum(lst))            #append the smallest number to the sorted list
		lst.pop(lst.index(smallestnum(lst)))          #and take out the smallest number from the initial list
				
	return sortedlst
			
    
#assigning values to the variables	
List = [1,5,2,7,4,6,9]                                         #variables for adding random elements to the list (optional, set all to 0 to not add random elements
rangeMin = 0
rangeMax = 0
elementMin = 0
elementMax = 0

for i in range(rangeMin,rangeMax):
	List.append(randint(elementMin,elementMax))

#output				
start_time = time.time()                                  #starting time (optional)
output = selectionsort(List)                              #sorts list
print(str(output))                                        #prints sorted list (optional)
print(f"Execution time: {time.time()-start_time}s")       #prints execution time (optional)
