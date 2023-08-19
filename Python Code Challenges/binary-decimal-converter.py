# Convert binary to decimal
def binary_to_decimal(x):
    return sum([(2**(i) * int(str(x)[::-1][i])) for i in range(len(str(x)))])

print(binary_to_decimal(11101101))


# Convert decimal to binary
def decimal_to_binary(x):
    num = x
    mods = []
    while num > 0:
        mods.append(num % 2)
        num = int(num / 2)

    return int(''.join([str(m) for m in mods[::-1]]))

print(decimal_to_binary(293))
