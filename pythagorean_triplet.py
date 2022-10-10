import math

def triplets_with_sum(number):
    triplet = []
    for a in range(0, number//3 + 1):
        for b in range(a + 1, (number - a) // 2 + 1):
            c = number - b - a
            if a < b < c:
                if a * a + b * b == c * c:
                    triplet.append([a,b,c])
    return triplet
  
