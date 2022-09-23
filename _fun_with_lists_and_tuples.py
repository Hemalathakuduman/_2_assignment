def sort_tuple(my_tup):

   my_len = len(my_tup)
   for i in range(0, my_len):

      for j in range(0, my_len-i-1):
         if (my_tup[j][-1] > my_tup[j + 1][-1]):
            temp = my_tup[j]
            my_tup[j]= my_tup[j + 1]
            my_tup[j + 1]= temp
   return my_tup

lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("The lst is :")
print(lst)

print("The sorted list of tuples are : ")
print(sort_tuple(lst))
