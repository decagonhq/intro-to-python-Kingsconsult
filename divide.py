def divide(a, b, floor=True):
    try:
        if floor == True:
            # print(a // b)
            return (a // b)
        else:
            # print(a / b)
            return (a / b)
    except TypeError:
        print("You should enter two integers as positional arguments and then either True or False")
        
        
# divide(1, '2', False)