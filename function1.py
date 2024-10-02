def addfunc(x,y):
    """
    Add two numbers together
    
    Parameters
    ----------
    x : number
    y : number
    """
    return x+y

def subfunc(x,y):
    """
    Subtract two numbers together
    
    Parameters
    ----------
    x : number
    y : number
    """
    return x-y

def mulfunc(x,y):
    """
    Multiply two numbers together
    
    Parameters
    ----------
    x : number
    y : number
    
    Returns
    -------
    number
        The product of x and y
    """
    return x*y


def main():
    print(addfunc(1,2))
    print(subfunc(1,2))
    print(mulfunc(1,2))
    return


if __name__ == "__main__":
    main()