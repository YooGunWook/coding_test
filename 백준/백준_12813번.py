a = list(str(input()))
b = list(str(input()))


def and_bit(a, b):
    bit_res = ""
    for i in range(len(a)):
        if a[i] == "1" and b[i] == "1":
            bit_res += "1"
        else:
            bit_res += "0"
    return bit_res


def or_bit(a, b):
    bit_res = ""
    for i in range(len(a)):
        if a[i] == "1" or b[i] == "1":
            bit_res += "1"
        else:
            bit_res += "0"
    return bit_res


def xor_bit(a, b):
    bit_res = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            bit_res += "1"
        else:
            bit_res += "0"
    return bit_res


def not_bit(a):
    bit_res = ""
    for i in range(len(a)):
        if a[i] == "1":
            bit_res += "0"
        else:
            bit_res += "1"
    return bit_res


print(and_bit(a, b))
print(or_bit(a, b))
print(xor_bit(a, b))
print(not_bit(a))
print(not_bit(b))
