a = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

def productSum(array):
    return go(array, 2)

def go(array, level):
    s =  0
    for el in array:
        if type(el) is int:
            s += el
        else:
            s += level * go(el, level+1)
        print(el, s, level)
    return s


