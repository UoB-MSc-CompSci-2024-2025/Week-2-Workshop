def find_min_max(*args):
    maximum = max(args)
    minimum = min(args)
    return minimum, maximum

minimum, maximum = find_min_max(1, 5, 24, 7, 87, 23, 45, 9)
print(minimum, maximum)