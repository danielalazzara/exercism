def slices(series, length):
    list = []
    if series == "":
        raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    
        
    for i in range(len(series)):
        if (i + length) <= len(series):
            list.append(series[i:i+length]) 
    return list
  
