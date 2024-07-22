def is_square(n):
#     Checking less than 0 use cases
    if n < 0:
        return False
    else:
#         Checking if the square root converted to an integer matched the raw result of a square root operation
        if int(n ** 0.5) == (n ** 0.5):
            return True
        else:
            return False
