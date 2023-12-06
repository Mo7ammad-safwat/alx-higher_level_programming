#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is not None
    if a_dictionary is not None:
        # Find the key with the maximum value
        max_key = max(a_dictionary, key=a_dictionary.get, default=None)
        return max_key
    else:
        return None
