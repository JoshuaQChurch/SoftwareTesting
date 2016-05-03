def take_percentage(value, percent):
    return value * percent


def double(value):
    return value * 2


def aging(value):
    return value + 1


def retirement(age, annual_salary, percentage_saved, goal):

    total_savings = 0

    while total_savings < goal:
        total_savings += double(take_percentage(annual_salary, percentage_saved))
        age = aging(age)

        if age >= 100:
            break

    return age
