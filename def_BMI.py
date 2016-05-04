import math

#Jon
class OutOfRangeError(ValueError):
    pass

class DivideByZero(ValueError):
    pass

#evan
def convert_inch_meters(inch):
    if (inch < 0):
        raise OutOfRangeError('cannot enter neagive number')   
    return (inch * 0.025)

#evan
def convert_lb_kg(lb):
    if (lb < 0):
        raise OutOfRangeError('cannot enter neagive number')
    return (lb * 0.45)


#corey
def square(value):
    
    return value * value

#corey
def ft_to_in(value):
    if (value < 0):
        raise OutOfRangeError('cannot enter neagive number')
    
        
    return (value * 12)

#corey
def divide(value1,value2):
    if (value1 < 0):
        raise OutOfRangeError('cannot enter neagive number')
    if (value2 == 0):
        raise DivideByZero('cannot divide by zero')
    if (value2 < 0):
        raise OutOfRangeError('cannot enter neagive number')
    return value1/value2





