# MAKES TWENTY: Given two integers, 
# return True if the sum of the integers is 20 
# or if one of the integers is 20. 
# If not, return False


def makes_twenty(n1,n2):
    if 20 in (n1,n2):
        return True
    
    if (n1 + n2) == 20:
        return True
    
    else:
        return False
    

makes_twenty(10,10)


    
