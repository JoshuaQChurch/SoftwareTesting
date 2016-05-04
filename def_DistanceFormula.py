import math

def subtract_x_values(x_point1, x_point2):  # subtract X values
    return x_point2 - x_point1

def subtract_y_values(y_point1, y_point2):  # subtract Y Values
    return y_point2 - y_point1

def square_x_value(x_value):  # square X Values
    return x_value * x_value

def square_y_value(y_value):  # square Y Values
    return y_value * y_value

def add_value(x_squared, y_squared):  # add squared values together
    return x_squared + y_squared

def get_distance(total_before_squaring):  # get square root of distance
    return math.sqrt(total_before_squaring)

def distance_formula(x1_value, y1_value, x2_value, y2_value):  # aggregate functions to perform distance formula
    first_parenthesis = subtract_x_values(x1_value, x2_value)
    second_parenthesis = subtract_y_values(y1_value, y2_value)
    square_first_parenthesis = square_x_value(first_parenthesis)
    square_second_parenthesis = square_y_value(second_parenthesis)
    total_values = add_value(square_first_parenthesis, square_second_parenthesis)
    final_distance = get_distance(total_values)
    return final_distance
