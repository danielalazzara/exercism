def transform(legacy_data):
    result = {}
    for l in legacy_data:
        for w in legacy_data[l]:
            result[w.lower()] = l
    return result
    
