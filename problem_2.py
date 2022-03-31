
def Intersection(lst1, lst2):
    """
    

    Parameters
    ----------
    lst1 : type list
        A list of numbers.
    lst2 : type list
        A list of numbers.

    Returns
    -------
    list
        It return the intersection of the two lists.
        We create a set with the first list and then we
        call the built in intersection function and pass
        as parameter the second list. A set is returned and
        we turn that set into a list and we return it

    """
    return list(set(lst1).intersection(lst2))
     
# We create our lists below
lst1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91] 
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))