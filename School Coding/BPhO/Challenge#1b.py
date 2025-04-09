import matplotlib.pyplot as plt
def determineColour(f): # f for frequency
    if f < 405:
        colour_str = 'Infra Red'
    elif (f>=405) and ( f < 480 ):
        colour_str = 'Red'
    elif (f>=480) and ( f < 510 ):
        colour_str = 'Orange'
    elif (f>=510) and ( f < 530 ):
        colour_str = 'Yellow'
    elif (f>=530) and ( f < 600 ):
        colour_str = 'Green'
    elif (f>=600) and ( f < 620 ):
        colour_str = 'Cyan'
    elif (f>=620) and ( f < 680 ):
        colour_str = 'Blue'
    elif (f>=680) and ( f <= 790 ):
        colour_str = 'Violet'
    else:
        colour_str = 'Ultra Violet'

