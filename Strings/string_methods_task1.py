def trim(input_str):
    s = input_str.strip()
    return s

def exists(input_str, sub_str):
    s = input_str.find(sub_str)
    return s

def titleIt(input_str):
    s = input_str.title()
    return s


def casesSwap(input_str):
    s = input_str.swapcase()
    return s


input_str_trim = "  hello  "
input_str = "hello"
sub_str = "llo"
print(trim(input_str_trim))
print(exists(input_str, sub_str))
print(titleIt(input_str))
print(casesSwap(input_str))
