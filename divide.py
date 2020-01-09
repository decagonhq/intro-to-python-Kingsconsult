def divide(a, b, floor=True):
    try:
        if floor == True:
            # print(a // b)
            return (a // b)
        else:
            # print(a / b)
            return (a / b)
    except TypeError as error:
        print(error)
        print("You should enter two integers as positional arguments and then either True or False")
    else:
        # print('Executing the else clause.')
        if !a or !b:
            
        
        
divide(1, '2', False)