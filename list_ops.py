def append(list1, list2):
    return list1 + list2


def concat(lists):
    return [x for list in lists for x in list]


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    return len(list)


def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial):
    for i in list:
        initial = function(initial, i)
    return initial    


def foldr(function, list, initial):
    for i in list[::-1]:
        initial = function(i, initial)
    return initial
    
