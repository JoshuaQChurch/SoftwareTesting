class OutOfRangeError(ValueError):
    pass


def take_percentage(value, percent):
    if (value < 0 or percent < 0):
        raise OutOfRangeError('cannot enter neagive number')
    
    return value * percent


def double(value):
    if (value < 0 ):
        raise OutOfRangeError('cannot enter neagive number')
    
    return value * 2


def aging(value):
    if (value < 0 ):
        raise OutOfRangeError('cannot enter neagive number')
    return value + 1


def retirement(age, annual_salary, percentage_saved, goal):

    total_savings = 0

    if (goal < 0 ):
        raise OutOfRangeError('cannot enter neagive number')

    while total_savings < goal:
        total_savings += double(take_percentage(annual_salary, percentage_saved))
        age = aging(age)

        if age >= 100:
            break

    return age
