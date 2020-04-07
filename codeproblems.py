
def find_smallest_num(list):
#Create a function that takes a list of numbers  and returns the smallest number in the list
   
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min

print(find_smallest_num([1, 2, -8, 0]))



def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
 
