def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError: # Input validation, can be used with being defined to catch all errors.
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
