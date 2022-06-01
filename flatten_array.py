def flatten(iterable):
    output = []
    for i in iterable:
        if type(i) is int or type(i) is str:
            output.append(i)
        elif type(i) is list:
            output = output + flatten(i)
    return output
    
