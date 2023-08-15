#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
<<<<<<< HEAD
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    del_value = my_list[idx]
    for i in range(idx + 1, len(my_list)):
        my_list[i - 1] = my_list[i]

    del(my_list[-1])
    return my_list
=======
	if idx < 0 or idx > len(my_list) - 1:
		return my_list

	del_value = my_list[idx]
	for i in range(idx + 1, len(my_list)):
	my_list[i - 1] = my_list[i]

del(my_list[-1])
return my_list
>>>>>>> ab979adf2d4b06e5e37246661606c941d32d746f
