#list of numbers, make total

def number_totaller(list_):  #number_totaller takes one argument, in this case a list
    output = 0               #define a variable, set to zero
    for number in list_ :    #for every number in the list: 
       output += number      #add number to variable 
        
    return output            # return our variable
       

print(number_totaller([1,2,3,4,5,6,7,8]))   #call of number_totaller 


