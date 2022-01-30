def signe(val):
    if val < 0 :
        return -1
    elif val > 0 :
        return 1
    else :
        return 0

def swap_chars(p1,p2):
    p1,p2 = p2,p1
    p1.color,p2.color = p2.color,p1.color
    p1.number,p2.number = p2.number,p1.number

    return p1,p2

