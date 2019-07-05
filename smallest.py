smallest_so_far = None
print('Before')
for the_num in [9,41,12,3,74,15,3.0,2.0] :
    if smallest_so_far is None :
        smallest_so_far = the_num
    elif the_num < smallest_so_far :
        smallest_so_far = the_num
    print('smallest number so far is :',smallest_so_far,'number tested in list is:',the_num) 

print('smallest number in the set is:', smallest_so_far)         
    