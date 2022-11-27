def power(base, exponent):
    assert int(exponent) == exponent, "Exponent must be an integer."
  
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1/base * power(base, exponent+1)
    return base * power(base, exponent-1)


# result = power(4, 3)
# print(result)



base, exp = input("Enter the base and exponent values: "). split()
result = power(float(base), int(exp))
print(result)