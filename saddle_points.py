def saddle_points(matrix):
    if len(set(map(len, matrix))) > 1: 
        raise ValueError("irregular matrix")
    saddle = []
    for i, mat in enumerate(matrix):
        for k, v in enumerate(mat):
            if v == max(mat) and v == min([mat[k] for mat in matrix]):
                saddle.append({'row': i + 1, 'column': k + 1})
    return saddle
    
