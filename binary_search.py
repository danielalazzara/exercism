def find(search_list, value):
    if not search_list:
        raise ValueError("value not in array")

    element = len(search_list) // 2
    
    if search_list[element] > value:
        return find(search_list[:element], value)
    if search_list[element] == value:
        return element
    if search_list[element] < value:
        return find(search_list[element + 1:], value) + (element + 1)
      
