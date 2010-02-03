"""
From Wikipedia:

function quicksort(array)
    var list less, greater
    if length(array) ≤ 1  
        return array  
    select and remove a pivot value pivot from array
    for each x in array
        if x ≤ pivot then append x to less
        else append x to greater
    return concatenate(quicksort(less), pivot, quicksort(greater))

Make this a valid Python program and test it.
"""
