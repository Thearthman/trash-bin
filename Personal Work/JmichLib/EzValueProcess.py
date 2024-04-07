# Library for processing values.
# warp,
def warp(value, from_low, from_high, to_low, to_high):
    if value < from_low:
        return to_low
    elif value > from_high:
        return to_high
    else:
        from_range = from_high - from_low
        to_range = to_high - to_low
        scaled_value = (value - from_low) / from_range
        return to_low + scaled_value * to_range


def constrain(value, lower_limit, upper_limit):
    if value < lower_limit:
        return lower_limit
    elif value > upper_limit:
        return upper_limit
    else:
        return value


# def value