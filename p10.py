def lattice(a1,a2,y):
    if a1==a2:
        if y ==90:
            return "square"
        elif y ==120:
            return "hexagonal"
    else:
        if y==90:
            return "rectangular"
        elif y==120:
            return "centered rectangular"
        else:
            return "oblique"
        
