#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is within valid range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Delete the element at the specified index without using pop()
    new_list = my_list[:idx] + my_list[idx + 1:]

    return new_list
